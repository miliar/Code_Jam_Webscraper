#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <string.h>
#include <set>
using namespace std;

int n;
int v[1005];

int main(){
    freopen("Ulaz.txt","r",stdin);
    freopen("Izlaz2.txt","w",stdout);

    int tests; scanf("%d",&tests);
    for( int t = 1; t <= tests; ++t ){

        scanf("%d",&n);
        int xr=0;
        for( int i = 0; i < n; ++i ){
            scanf("%d",&v[i]);
            xr ^= v[i];
        }

        if( xr ){
            printf("Case #%d: NO\n",t);
            continue;
        }

        int s = 1000000 + 55,sum(0);
        for( int i = 0; i < n; ++i ){
            s = min( s , v[i] );
            sum += v[i];
        }

        printf("Case #%d: %d\n",t,sum-s);
    }

    return 0;
}
