#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;
//const int maxR = 13, maxC=9;
const int INF = 100000;
class SaveUniverse;
class Server
{
    char *name;
    int first_query;

public:
    Server()
    {
        name = NULL;
        first_query = INF;
    }
    Server(char *s)
    {
        name = new char[strlen(s)+1];
        strcpy(name,s);
        first_query = INF;
    }

    ~Server()
    {
        delete name;
    }

    friend class SaveUniverse;

};

class Query
{
    char* q;
    int server;

public:
    Query()
    {
        q = NULL;
        server = -1;
    }
    Query(char *s, int ser)
    {
        q = new char[strlen(s)+1];
        strcpy(q,s);
        server = ser;
    }

    ~Query()
    {
        delete q;
    }

    friend class SaveUniverse;
};

class SaveUniverse
{
    Server *servers[101];
    int num_s;
    Query *queries[1001];
    int num_q;
    int switches;

public:

    SaveUniverse()
    {
        num_s = 0;
        switches = 0;
        num_q = 0;
        //servers= NULL;
        //queries=NULL;
    }

    SaveUniverse(ifstream &fin)
    {
        char temp[101];
        int i=0;
        fin.getline(temp,100);
        num_s = atoi(temp);
        for(i=0;i<num_s;i++)
        {
            fin.getline(temp,100);
            servers[i] = new Server(temp);
        }
        fin.getline(temp,100);
        num_q = atoi(temp);
        for(i=0;i<num_q;i++)
        {
            fin.getline(temp,100);
            for(int j=0;j<num_s;j++)
            {
                if(strcmp(servers[j]->name,temp)==0)
                {
                    if(servers[j]->first_query == INF)
                        servers[j]->first_query = i;
                    break;
                }
            }
            queries[i] = new Query(temp,j);
        }
    }

    void display()
    {
        int i=0;
        cout<<"\nServers : \n";
        for(i=0;i<num_s;i++)
        {
            cout<<servers[i]->name<<" "<<servers[i]->first_query<<endl;
        }
        cout<<"\nQueries : \n";
        for(i = 0; i< num_q; i++)
        {
            cout<<queries[i]->q<<" "<<queries[i]->server<<endl;
        }
    }


    int result()
    {
        int server = 0;
        server = getServer();
        switches = 0;
        for(int i = 0; i< num_q; i++)
        {
            if(servers[server]->first_query == i)
            {
                switches++;
                refresh(i);
                server = getServer();
            }
            servers[queries[i]->server]->first_query = INF;
        }
        return switches;
    }

    void refresh(int pos)
    {
        for(int i=pos;i<num_q;i++)
        {
            if(servers[queries[i]->server]->first_query > i)
                servers[queries[i]->server]->first_query = i;
        }
    }

    int getServer()
    {
        int maxpos=-1,ser=0;
        for(int i = 0; i<num_s;i++)
        {
            if(maxpos < servers[i]->first_query)
            {
                maxpos = servers[i]->first_query;
                ser = i;
            }
        }
        return ser;
    }

    ~SaveUniverse()
    {
        int i=0;
        for(i=0;i<num_s;i++)
        {
            if(servers[i])
                delete servers[i];
        }
        for(i=0;i<num_q;i++)
        {
            if(queries[i])
                delete queries[i];
        }
    }


};
int main(int argc, char *argv[])
{
    char filename[200]= "A-small.in";
    if(argc == 2)
    {
        strcpy(filename,argv[1]);
    }
    else if (argc>2)
    {
        cout<<"Too many arguments..."<<endl;
        cout<<"USAGE :: saveUniverse A-small.in\n";
        return 0;
    }
    ifstream fin(filename);
    int n=0;
    char temp[101];
    fin.getline(temp,100);
    n = atoi(temp);
    for(int i=1;i<=n;i++)
    {
        SaveUniverse sUniv(fin);
     //   sUniv.display();
        cout<<"Case #"<< i << ": "<<sUniv.result()<<endl;
        sUniv.result();
    }
    
   //system("PAUSE");
    return 0;
}
