#include <iostream>
#include <stdio.h>
#include <cstring>
using namespace std;

#define MaxN 1010

int T,n;
int a[MaxN];
int b[MaxN];
bool mark[MaxN];

double Solve( int p )
{
    if ( mark[p] ) return 0.0;

    mark[p] = true;
    return Solve( b[p] ) + 1.0;
}

int main()
{
    freopen("test4.in","r",stdin);
    freopen("test4.out","w",stdout);

    scanf("%d",&T);
    for (int t = 0; t < T; ++t) {
        scanf("%d",&n);
        for (int i = 0; i < n; ++i) {
            scanf("%d",&a[i]);
            a[i]--;
            b[ a[i] ] = i;
        }

        memset(mark, 0, sizeof(mark));
        double ret = 0.0;

        for (int i = 0; i < n; ++i) {
            if ( mark[i] ) continue;
            if ( a[i] == i ) continue;

            ret += Solve( i );
        }


        printf("Case #%d: %lf\n",t+1,ret);
    }

    return 0;
}
