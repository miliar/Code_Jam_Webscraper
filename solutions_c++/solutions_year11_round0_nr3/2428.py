#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
#include <stack>
#include <math.h>

using namespace std;

int main(){

    freopen("C-large.IN", "r", stdin );
    freopen("sol.txt", "w", stdout );

    int test;
    scanf("%d", &test );

    for(int t = 1; t <= test; ++t ){

        int n, x = 0, sum = 0;
        int mn = 1<<20, v;
        scanf("%d", &n );

        for(int i = 0; i < n; ++i ){
          scanf("%d", &v );
          x ^= v, sum += v;
          mn = min( mn, v );
        }

        if( x == 0 ) printf("Case #%d: %d\n", t, sum - mn );
        else printf("Case #%d: NO\n", t);
    }

    return 0;
}
