#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
#include <queue>
#include <math.h>

using namespace std;

char mat[105][105];

double wp[105], owp[105], oowp[105], res[105];

int main(){

    freopen("A-large.IN", "r", stdin );
    freopen("sol.txt", "w", stdout );


    int t;
    scanf("%d", &t );

    for(int test = 1; test <= t; ++test ){

        int n;
        scanf("%d", &n );

        for(int i = 0; i < n; ++i )
           scanf("%s", mat[i] );

        for(int r = 0; r < n; ++r ){
         int tot = 0, w = 0;
         for(int c = 0; c < n; ++c )
         {
            if( mat[r][c] == '1' ) ++w, ++tot;
            if( mat[r][c] == '0' ) ++tot;
         }
          wp[r] = w / (double)tot;
        }

        for(int i = 0; i < n; ++i ){

          double avr = 0.; int ply = 0;
          for(int r = 0; r < n; ++r )
          {
           if( mat[i][r] == '.' )continue;
           int tot = 0, w = 0;
           for(int c = 0; c < n; ++c ){
              if( c == i ) continue;
              if( mat[r][c] == '1' ) ++w, ++tot;
              if( mat[r][c] == '0' ) ++tot;
           }
           avr += w / (double)tot;
           ++ ply;
          }

          owp[i] = avr / (double)ply;
        }

        for(int i = 0; i < n; ++i ){
         double avr = 0.; int ply = 0;
         for(int j = 0; j < n; ++j ){
          if( mat[i][j] == '.' ) continue;
          avr += owp[j]; ++ ply;
         }
         oowp[i] = avr / (double)ply;
        }

        for(int i = 0; i < n; ++i )
          res[i] = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];

        printf("Case #%d:\n", test );
        for(int i = 0; i < n; ++i )
          printf("%.9lf\n", res[i] );
    }

  return 0;
}


