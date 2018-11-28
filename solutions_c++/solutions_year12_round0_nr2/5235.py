#include <algorithm>
#include <iostream>
#include <cstring>
#include <vector>
#include <cstdio>
#include <math.h>

using namespace std;

int g[105];
bool use[105];

int main(){

    freopen("B-small-attempt0.IN", "r", stdin);
    freopen("sol.txt", "w", stdout);

    int test;
    scanf("%d", &test);
    for(int t = 1; t <= test; ++t){
        memset(use, 0, sizeof(use));
        int n, s, p, sol = 0;
        scanf("%d%d%d", &n, &s, &p );
        for(int i = 0; i < n; ++i)
           scanf("%d", &g[i] );

        int l = n - s;
        for(int i = 0; i < n && l; ++i)
           if( g[i] < 2 ){  --l;
             int c;
             for(int j = 0; j <= 2; ++j)
             if( g[i] - j >= 0 && ((g[i] - j) % 3 == 0) )
               c = (g[i] - j)/3 + int(j > 0);

             if(c >= p){ use[i] = 1; ++sol; }
        }

        for(int i = 0; i < n && l; ++i){
          if( use[i] )continue;
          int c;
          for(int j = 0; j <= 2; ++j)
            if( g[i] - j >= 0 && ((g[i] - j) % 3 == 0) )
               c = (g[i] - j)/3 + int(j > 0);

            if(c >= p){
                 use[i] = 1;
                 ++sol, --l;
            }
        }

        for(int i = 0; i < n && s; ++i){
          if( use[i] )continue;
          int c;
          for(int j = 2; j <= 4; ++j){
            if( g[i] - j >= 0 && ((g[i] - j) % 3 == 0) )
              c = (g[i] - j)/3 + 2;
          }
          if(c >= p)++sol, --s;
        }

        printf("Case #%d: %d\n", t, sol );
    }

    return 0;
}


