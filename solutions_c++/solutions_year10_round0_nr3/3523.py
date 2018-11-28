#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char *argv[])
{
    opterr = 0;
    char *filename = NULL;
    int c;

    while (( c = getopt(argc, argv, "hf:")) != -1)
    {
        switch(c)
        {
            case 'h':
            {
                cout << "Usage: snapper -f <FILENAME>";
                exit(0);
            }
            case 'f':
            {
                filename = optarg;
                break;
            }
        }
    }

    if(!filename)
    {
        cout << "Usage: snapper -f <FILENAME>";
        exit(0);
    }
    ifstream inputsrc(filename);

    char buff[1024];

    inputsrc.getline(buff, 1024);
    
    int cases = atoi(buff);
    int loops = 1;
    
    while(cases > 0)
    {
        int runs;
        int slots;
        int gnum;
        char *token;
        int tok;
        
        inputsrc.getline(buff, 1024);
        string ln(buff);

        token = strtok (const_cast<char *>(ln.c_str()), " ");
        tok = 0;
        while (token != NULL)
        {
            switch(tok)
            {
                case 0:
                    runs = atoi(token);
                    break;
                case 1:
                    slots = atoi(token);
                    break;
                case 2:
                    gnum = atoi(token);
                    break;
            }
            ++tok;
            token = strtok (NULL, " ");
        }
        
        inputsrc.getline(buff, 1024);
        ln.clear();
        ln.assign(buff);
        
        unsigned int *groups = new unsigned int[gnum];
        
        tok = 0;
        token = strtok (const_cast<char *>(ln.c_str()), " ");
        while(token != NULL)
        {
            groups[tok] = atoi(token);
            ++tok;
            token = strtok (NULL, " ");
        }
        
        int linehead = 0;
    
        unsigned int mint = 0;
        
        for(int i=0; i<runs; ++i)
        {
            unsigned int onBoard = 0;
            int linebegin = linehead;
            while(onBoard < slots)
            {
                onBoard += groups[linehead];
                linehead++;
                
                if(linehead >= gnum)
                {
                    linehead = 0;
                }
                
                if(linebegin == linehead)
                {
                    break;
                }
            }
            if(onBoard > slots)
            {
                --linehead;
                if(linehead < 0)
                {
                    linehead = gnum-1;
                }
                onBoard -= groups[linehead];
            }
            
            mint += onBoard;
        }

        cout << "Case #" << loops  << ": " << mint << endl;

        delete [] groups;
        groups = NULL;
        --cases;
        ++loops;
    }
}
