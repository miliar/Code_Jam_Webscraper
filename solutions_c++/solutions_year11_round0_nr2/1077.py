#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <map>
#define TASK "B-large"
#define Max
using namespace std;

int T,C,D,N;
char ch;
string tmp;

vector<char> List;
map<char,map<char,bool> > Combinable;
map<char,map<char,char> > Combine;
map<char,map<char,bool> > Oppose;

void Init()
{
    List.clear();
    Combinable.clear();
    Combine.clear();
    Oppose.clear();
}

void Print()
{
    cout<<"[";
    for(int i=0; i<List.size(); i++)
    {
        cout<<List[i];
        if(i<List.size()-1)cout<<", ";
    }
    cout<<"]"<<endl;
}

int main()
{
    freopen(TASK".in","r",stdin);
    freopen(TASK".out","w",stdout);
    
    cin>>T;
    
    for(int i=0; i<T; i++)
    {
        Init();
        
        cin>>C;
        for(int j=0; j<C; j++)
        {
            cin>>tmp;
            Combinable[tmp[0]][tmp[1]]=Combinable[tmp[1]][tmp[0]]=true;
            Combine[tmp[0]][tmp[1]]=Combine[tmp[1]][tmp[0]]=tmp[2];
        }
        
        cin>>D;
        for(int j=0; j<D; j++)
        {
            cin>>tmp;
            Oppose[tmp[0]][tmp[1]]=Oppose[tmp[1]][tmp[0]]=true;
        }
        
        cin>>N;
        for(int j=0; j<N; j++)
        {
            cin>>ch;
            if(List.size()==0)
            {
                List.push_back(ch);
            }
            else
            {
                //Combine
                while(List.size()>0)
                {
                    char last=List[List.size()-1];
                    if(Combinable[last][ch])
                    {
                        ch=Combine[last][ch];
                        List.pop_back();
                    }
                    else
                    {
                        break;
                    }
                }
                List.push_back(ch);
                
                //Oppose
                for(int i=0; i<List.size(); i++)
                {
                    for(int j=i+1; j<List.size(); j++)
                    {
                        if(Oppose[List[i]][List[j]])
                        {
                            List.clear();
                        }
                    }
                }
            }
        }
        
        cout<<"Case #"<<i+1<<": ";   Print();
    }
    
    fclose(stdin);
    fclose(stdout);
    
    return 0;
}
