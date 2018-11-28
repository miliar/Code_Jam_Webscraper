#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <ctime>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <string.h>
#include <sstream>
#include <bitset>
#include <algorithm>
#include <numeric>
#define TASK "A-large"
#define Max 100
using namespace std;

int T,N,R[Max][Max];//1 = win, -1 = loss, 0 = not played
int Played[Max],Won[Max];

double WP[Max],OWP[Max],OOWP[Max];

void Init()
{
    memset(R,0,sizeof(R));
    memset(Played,0,sizeof(Played));
    memset(Won,0,sizeof(Won));
    memset(WP,0,sizeof(WP));
    memset(OWP,0,sizeof(OWP));
    memset(OOWP,0,sizeof(OOWP));
}

int main()
{
    freopen(TASK".in","r",stdin);
    freopen(TASK".out","w",stdout);
    
    cin>>T;
    
    for(int t=0; t<T; t++)
    {
        Init();
        
        cin>>N;
        
        for(int i=0; i<N; i++)
        {
            for(int j=0; j<N; j++)
            {
                char ch;
                cin>>ch;
                if(ch=='1')//Won
                {
                    R[i][j]=1;
                    Won[i]++;
                    Played[i]++;
                }
                else if(ch=='0')//Lost
                {
                    R[i][j]=-1;
                    Played[i]++;
                }
                else//Not played
                {
                    R[i][j]=0;
                }
            }
            
            WP[i]=double(Won[i])/Played[i];
        }
        
        //OWP
        for(int i=0; i<N; i++)
        {
            int op=0;
            
            for(int j=0; j<N; j++)
            {
                if(R[i][j]!=0)//If j is opponent of i
                {
                    op++;
                    int wins=0,total=0;
                    for(int k=0; k<N; k++)
                    {
                        if(R[j][k]!=0 && k!=i)
                        {
                            wins+=bool(R[j][k]==1);
                            total++;
                        }
                    }
                    OWP[i]+=double(wins)/total;
                }
            }
            OWP[i]/=op;//Average
        }
        
        //OOWP
        for(int i=0; i<N; i++)
        {
            double owp=0.0;
            int op=0;
            
            for(int j=0; j<N; j++)
            {
                if(R[i][j]!=0)
                {
                    owp+=OWP[j];
                    op++;
                }
            }
            OOWP[i]=owp/op;
        }
        
        cout<<"Case #"<<t+1<<":"<<endl;
        for(int i=0; i<N; i++)
        {
            double RPI=0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i];
            cout<<RPI<<endl;
        }
        
    }
    
    
    
    fclose(stdin);
    fclose(stdout);
    
    return 0;
}
