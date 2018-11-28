#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;

const int N = 40;

int n,k;
int wei[N];

    void init()
    {
        wei[0] = 1;
        for ( int i=1;i<=30;i++ )
        {
            wei[i] = 2*wei[i-1];
        }
    }

    int work()
    {
        k -= wei[n]-1;
//        printf("k  = %d\n",k);//debug
        if ( k<0 )
        return 0;
        k %= wei[n];
        if ( 0 == k )
        return 1;
        return 0;
    }


int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int cas;
    init();
    scanf("%d",&cas);
    for ( int i=1;i<=cas;i++ )
    {
        scanf("%d %d",&n,&k);
        if (work())
        printf("Case #%d: ON\n",i);
        else printf("Case #%d: OFF\n",i);
    }
    return 0;
}
