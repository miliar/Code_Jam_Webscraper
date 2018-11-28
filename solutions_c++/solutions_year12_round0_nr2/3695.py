#include <vector>
#include <list>
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <memory.h>
#include <cmath>

using namespace std;

int maxScore(int t,int s)
{
    if( s==0 )
    {
        switch( t%3 )
        {
            case 0: return t/3;
            case 1: return (t-1)/3+1;
            case 2: return (t-2)/3+1;
        }
    }
    else
    {
        switch( t%3 )
        {
            case 0: return t>=3?t/3 +1:0;
            case 1: return t>=4?(t-1)/3+1:0;
            case 2: return (t-2)/3+2;
        }
    }
}

int d[110][110];
int ts[110];
int N,S,P;

int solve()
{
    memset(d,0,sizeof(int)*110*110);
    for( int i=1; i<=N; i++)
    {
        //cout<<maxScore(ts[i],0)<<endl;
        d[i][0] = d[i-1][0] + (maxScore(ts[i],0)>=P?1:0);
        for( int j=1; j<=min(i,S); j++)
        {
            d[i][j] = max(d[i-1][j-1]+ (maxScore(ts[i],1)>=P?1:0), d[i-1][j] + (maxScore(ts[i],0)>=P?1:0));
        }
    }
    return d[N][S];
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    cin>>T;

    for( int i=1; i<=T; i++)
    {
        cin>>N>>S>>P;
        for( int j=1; j<=N; j++)
            cin>>ts[j];
        cout<<"Case #"<<i<<": "<<solve()<<endl;
    }
    return 0;
}
