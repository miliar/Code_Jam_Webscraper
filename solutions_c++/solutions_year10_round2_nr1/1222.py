#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

#include <string.h>

using namespace std;

typedef long long int64;

typedef struct {
    char name[102];
    int child;
    int next;
} dirs_t;
dirs_t dirs[5000];
int end;

int addtree(char* name, int& current)
{
    if(!dirs[current].child)
    {
        dirs[current].child = end;
        current = end++;
        strcpy(dirs[current].name, name);
        dirs[current].child = 0;
        dirs[current].next = 0;
	return 1;
    }
    else
    {
        current = dirs[current].child;
        do
        {
    	    if(strcmp(dirs[current].name, name) == 0)
    	    {
		return 0;
	    }
	    else
	    {
		if(!dirs[current].next)
		{
                    dirs[current].next = end;
                    current = end++;
                    strcpy(dirs[current].name, name);
                    dirs[current].child = 0;
                    dirs[current].next = 0;
		    return 1;
		}
		else
		{
		    current = dirs[current].next;
		}
	    }
        } while(1);
    }
}

int handle_case(ifstream& infile)
{

    int N, M;
    int current;
    char buff[102];

    dirs[0].child=0;
    dirs[0].next=0;
    dirs[0].name[0]='\0';
    end = 1;

    infile >> N >> M;
    infile.getline(buff, 101);

    for(int i=0; i<N; i++)
    {
	infile.getline(buff, 101);
	char* p = buff;
	char* q = ++p;
	current = 0;
	while(*p != '\0' && *p != '\n')
	{ 
            if(*p == '/')
            {
                *p = '\0';
		//cout << q << endl;
                addtree(q, current);
	        q = ++p;
	    }
	    p++;
	}
	*p = '\0';
	//cout << q << endl;
	addtree(q, current);
    }

    //for(int i=0; i<end; i++)
    //{
    //    cout << dirs[i].name << "  " << dirs[i].child << " " << dirs[i].next << endl;
    //}

    int total = 0;
    for(int i=0; i<M; i++)
    {
	infile.getline(buff, 101);
	char* p = buff;
	char* q = ++p;
	current = 0;
	while(*p != '\0' && *p != '\n')
	{ 
            if(*p == '/')
            {
                *p = '\0';
                total += addtree(q, current);
	        q = ++p;
	    }
	    p++;
	}
	*p = '\0';
	total += addtree(q, current);
    }

    //for(int i=0; i<end; i++)
    //{
    //    cout << dirs[i].name << "  " << dirs[i].child << " " << dirs[i].next << endl;
    //}

    return total;
}

int main(int argc, char* argv[])
{
    int Ncases, result;
    if(argc < 2)
    {
        cout << "Usage: ./code <infile>" << endl;
        exit(1);
    }

    ifstream infile(argv[1]);
    if(infile.is_open())
    {
        infile >> Ncases;
	for(int i=0; i<Ncases; i++)
	{
            result = handle_case(infile);
	    cout << "Case #" << (i+1) << ": " << result << endl;
	}
    }
    else
    {
        cout << "error opening" << argv[1] << endl;
	return 1;
    }
    return 0;
}

