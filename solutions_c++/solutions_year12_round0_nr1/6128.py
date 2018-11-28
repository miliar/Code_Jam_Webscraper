#include <iostream>
#include <map>
#include <string>
#include <fstream>

#include <pthread.h>
#include <getopt.h>

using namespace std;

map<char, char>    decoder;

pthread_mutex_t     mutex;
pthread_cond_t      cond;

map<int, string>   inputq;
map<int, string>   result;

bool tend = false;

void usage(char *prgname)
{
    cout << prgname << " -f INPUT_FILE -t THRD_NUM" << endl;
}

void parseFile(const char *ifile)
{
    string line;
    ifstream ins(ifile);
    if(ins.is_open())
    {
        getline(ins, line);
        cout << "READING: " << line << " LINES" << endl;
        int ref = 1;
        while(ins.good())
        {
            getline(ins, line);

            pthread_mutex_lock(&mutex);
            inputq.insert(make_pair(ref, line));
            pthread_cond_signal(&cond);
            pthread_mutex_unlock(&mutex);
            
            ++ref;
        }
        ins.close();
    }
    else
    {
        cout << ifile << " did not open" << endl;
    }
}

void *worker(void *)
{
    pthread_mutex_lock(&mutex);
    while (tend == false) 
    {
        if(inputq.size() > 0)
        {
            map<int, string>::iterator iter = inputq.begin();
            if(iter == inputq.end())
            {
                pthread_mutex_unlock(&mutex);
                continue;
            }
            int ref = iter->first;
            string code = iter->second;
            
            inputq.erase(iter);
            pthread_mutex_unlock(&mutex);
            
            string decode = code;
            for (int i = 0; i < code.length(); ++i)
            {
                decode[i] = decoder[code[i]];
            }
            result.insert(make_pair(ref, decode));
        }
        else 
        {
            struct timespec to;
            memset(&to, 0, sizeof to);
            to.tv_sec = time(0) + 1;
            to.tv_nsec = 0;
            
            pthread_cond_timedwait(&cond, &mutex, &to);
        }

    }
    pthread_mutex_unlock(&mutex);
}

void setup()
{
    string code = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
    string uncode = "our language is impossible to understand";
    for (int i = 0; i < code.length(); ++i) 
    {
        decoder.insert(make_pair(code[i], uncode[i]));
    }
    
    code = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    uncode = "there are twenty six factorial possibilities";
    for (int i = 0; i < code.length(); ++i) 
    {
        decoder.insert(make_pair(code[i], uncode[i]));
    }
    
    code = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
    uncode = "so it is okay if you want to just give up";
    for (int i = 0; i < code.length(); ++i) 
    {
        decoder.insert(make_pair(code[i], uncode[i]));
    }
    decoder.insert(make_pair('z', 'q'));
    decoder.insert(make_pair('q', 'z'));
}

int main(int argc, char * argv[])
{
    static struct option long_options[] =
    {
       	{"file", required_argument, 0, 'f'},
       	{"thread", required_argument, 0, 't'}
    };
    
    int option_index = 0;
    int c;
    
    char *ifile     = NULL;
    int thrdCount   = 1;
    
    c = getopt_long (argc, argv, "f:t:", 
                     long_options, &option_index);
    while(c != -1)
    {          
        switch (c)
        {
           	case 'f':
           	{
           	    cout << "IN F" << endl;
           	    ifile = optarg;
           	    break;
           	}
           	case 't':
           	{
           	    cout << "IN T" << endl;
           	    thrdCount = atoi(optarg);
           	    if(thrdCount < 1)
           	    {
           	        thrdCount = 1;
           	    }
           	    break;
           	}
           	default:
           	{
           		usage(argv[0]);
           		abort();
           	}
        }
        c = getopt_long (argc, argv, "f:t:",
                         long_options, &option_index);
    }
    
    if(ifile == NULL)
    {
        usage(argv[0]);
        abort();
    }
    
    setup();
    
    pthread_t threads[thrdCount];
    pthread_attr_t attr;
    
    pthread_mutex_init(&mutex, NULL);
    pthread_cond_init (&cond, NULL);
    
    pthread_attr_init(&attr);
    pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_JOINABLE);
    
    for(int i = 0; i < thrdCount; ++i)
    {
        pthread_create(&threads[i], &attr, worker, NULL);
    }
    
    parseFile(ifile);
    tend = true;
    
    for (int i=0; i < thrdCount; i++) 
    {
        pthread_join(threads[i], NULL);
    }
    
    for(map<int, string>::iterator walker = result.begin(); walker != result.end(); ++walker)
    {
        cout << "Case #" << walker->first << ": " << walker->second << endl;
    }
    
    pthread_attr_destroy(&attr);
    pthread_mutex_destroy(&mutex);
    pthread_cond_destroy(&cond);
    
    
    
        
}