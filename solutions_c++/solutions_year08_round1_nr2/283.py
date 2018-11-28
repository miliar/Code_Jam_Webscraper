#include<string>
#include<iostream>
#include<sstream>
#include<assert.h>
#include<cstdio>
#include<map>
#include<algorithm>
#include<bitset>
#include<cmath>
#include<queue>
#include<functional>


using namespace std;

int N;
int res[2000];
int M;
int wanted[2000][2000];

bool solve()
{
    int bestcount=-1;
    int best=-1;

    for (int i=0;(i<(1<<N));i++)
    {

        bool allhappy=true;
        for (int j=0;j<M;j++)
        {
            bool thisishappy=false;
            for(int k=0;k<N;k++) if(wanted[j][k]!=-1)
            {
                 thisishappy=(thisishappy || ( (((1<<k)&i)>0 )==wanted[j][k]) );
            }
                 
            allhappy&=thisishappy;
        }
        if(allhappy)
        {
            int count=0;
            for (int j=0;j<N;j++) if ( (1<<j)&i) count++;
            if( (bestcount==-1) || (bestcount>count) )
            {
                best=i;
                bestcount=count;
                
            }
        }
    }
    if(bestcount!=-1)
    {
        for (int j=0;j<N;j++) res[j]=(( (1<<j)&best)>0);
    }
    return (bestcount!=-1);
}

//=========================================================
// I/O:
//
int main()
{
    int C; cin>>C;
    for (int i=1;i<=C;i++)
    {
        memset(wanted,-1,sizeof(wanted));

        cin>>N>>M;

        for (int j=0;j<M;j++)
        {
            int T;
            cin>>T;
            for (int k=0;k<T;k++)
            {
                int f;
                cin>>f;
                cin>>wanted[j][f-1];
            }
        }
        bool bres=solve();
        cout<<"Case #"<<i<<": ";
        if(bres)
        {
            cout<<res[0];
            for (int j=1;j<N;j++) cout<<" "<<res[j];
            
        }
        else cout<<"IMPOSSIBLE";
        cout<<endl;
        
    }
    return 0;
}
