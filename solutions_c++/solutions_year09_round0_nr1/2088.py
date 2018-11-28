#include <iostream> 
#include <vector>
#include <string>
#include <string.h>
#include <algorithm> 
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <bitset>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cfloat>
#include <bitset> 

using namespace std;

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
map<string,bool> esta;
map <string,bool> vale;
int L,D,N;
long long res;
int main()
{
    cin>>L>>D>>N;
    string cad,cad2,aa="";
    for(int i=0;i<D;i++)
    {   aa="";
        cin>>cad;
        for(int j=1;j<=cad.size();j++)
        {   aa+=cad[j-1];
            vale[aa]=true;
        }
        esta[cad]=true;
        vale[cad]=true;
    }

    
    for(int i=0;i<N;i++)
    {
        res=0;
        cin>>cad;
        vector <string> todos;
       
        int j;
        bool sal=false;
        for(j=0;j<cad.size()&&!sal;j++)
        {
            if(cad[j]=='(')
            {
                string nodo="";
                while(cad[j]!=')')
                        {
                            nodo+=cad[j];
                            if(vale[nodo])
                            todos.push_back(nodo);
                            nodo="";   
                            j++;
                        } 
                    j++;
                    break;    
            }
            else
            {
                        string no="";
                        no+=cad[j];
                        todos.push_back(no);
                        j++;
                        break;
            }
        
        }
        if(todos.size()==0)
            sal=true;
        for(;j<cad.size()&&!sal;j++)
        {
                    
                    if(cad[j]=='(')
                    {
                        j++;
                        int pos1=j;
                        int pos2=0;
                        vector <string> todos2;
                        string nodo="";
                        while(cad[j]!=')')
                        {
                            for(int ii=0;ii<todos.size();ii++)
                            {   nodo=(todos[ii]+cad[j]);
                                if(vale[nodo]&&(nodo.size()<=L))
                                todos2.push_back(nodo);
                                nodo="";
                            
                            }
                            j++;
                        }
                        if(todos2.size()==0)
                            sal=true;
                        else
                        todos=todos2;
                    }
                    else
                    {
                            bool entro=false;
                            string nodo="";
                             vector <string> todos2;
                            for(int ii=0;ii<todos.size();ii++)
                            {   nodo=todos[ii]+cad[j];
                                if(vale[nodo]&&nodo.size()<=L)
                                {
                                    todos2.push_back(nodo);
                                }
                                nodo="";
                                
                            }
                            if(todos2.size()==0)
                            sal=true;
                            else
                           todos=todos2;
                            
                            
                    }
        }
        if(!sal)
        {
            for(int ii=0;ii<todos.size();ii++)
            {
                if(esta[todos[ii]])
                    res++;
            }
        }
        cout<<"Case #"<<i+1<<": "<<res<<endl;
    }
    
return 0;
}
