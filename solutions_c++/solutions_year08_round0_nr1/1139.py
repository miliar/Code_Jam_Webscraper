#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

struct SE
{
       string name;
       int i;
       SE()
       {
           i=0;
           name="";
       }
};

vector<SE> available;
vector<string> queries;
int change=0;

void check(string s)
{
    int j;
  /*  SE temp;
    temp.name=s;
    temp.i=0;*/
    
    for(j=0;j<available.size();j++)
            if(available[j].name == s)
                            break;
    
    int flag=1;
    if( j < available.size() )
    {
        available[j].i=1;
        for( int k=0;k<available.size();k++)
        {
             if(available[k].i != 1)
             {
                                  flag=0;
                                  break;
             }
        }
        if(flag==1)
        {
                   change++;
                   for(int m=0;m<available.size();m++)
                   {
                           if(m != j)
                           {
                                available[m].i = 0;
                           }
                   }
        }
    }
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("o.txt","w",stdout);
    
    //int j;
    //j=find(queries.begin(),queries.end(),"hi")-queries.begin();
    
    SE searchEngine;
    int n;
    int m;
    int no_queries;
    string Qry;
    cin>>n;
    for(int i=0;i<n;i++)
    {
            cin>>m;
            cin.get();
            for(int j=0;j<m;j++)
            {
                   getline(cin,searchEngine.name,'\n');
                   //cout<<searchEngine.name<<endl;
                   available.push_back(searchEngine);
            }
            cin>>no_queries;
            cin.get();
            for(int k=0;k<no_queries;k++)
            {
                    getline(cin,Qry,'\n');
                    check(Qry);
                    queries.push_back(Qry);
            }
            cout<<"Case #"<<i+1<<": "<<change<<endl;
            
            change=0;
            available.clear();
            queries.clear();
    }
    
    return 0;
}
