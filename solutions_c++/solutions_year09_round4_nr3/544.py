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
#include<set>

using namespace std;

//=========================================================
// program:
//
int N, K;
int stock[16][25];

char possible[1<<16];

int isPossible(int mask)
{
    char &r = possible[mask];
    if(r==-1)
    {
        r = 0;
        vector< pair<int,int> > vec;
        for (int i=0;i<N; i++)
            if(mask&(1<<i) )
                vec.push_back( make_pair(stock[i][0], i ) );
        sort(vec.begin(), vec.end());
        //cout<<mask<<" is possible? "<<vec.size()<<endl;
        for (int i=0; i<K; i++)
            for (int j=0; j<vec.size()-1; j++)
                if( stock[ vec[j].second ][i] >= stock[ vec[j+1].second ][i] )
                    return (r=0);
        //cout<<mask<<" is possible "<<endl;
        r= 1;
        
        //vector<int> 
    }
    return r;
}

int mem[1<<16];

int rec(int mask)
{
    if(mask==0) return 0;
    int & res = mem[mask];
    if(res!=-1) return res;
    
    res = N+1;
    for (int i=mask; i>0; i=( (i-1)&mask) )
        if(isPossible(i))
            res = std::min(res, 1 + rec(mask-i) );
    return res;
     
}

int solve()
{
    memset(possible, -1, sizeof(possible) );
    memset(mem, -1, sizeof(mem) );
    return rec( (1<<N) -1 );
}


inline void init(){}
//=========================================================
// I/O:
//
int main()
{
    init();
    int C; cin>>C;
    for (int i=1;i<=C;i++)
    {
        cin>>N>>K;
        for (int j=0; j<N; j++)
            for (int k=0; k<K; k++)
                cin>>stock[j][k];
                
        cerr<<"["<<i<<" / "<<C<<"]"<<endl;
        cout<<"Case #"<<i<<": " <<solve()  << endl;
        
    }
    return 0;
}
