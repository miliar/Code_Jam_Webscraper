#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <vector>

using namespace std;

template<typename T, typename U> inline void relaxmax( T &res, const U &x ) { if ( x > res ) res = x; }
#define ZERO(v) memset(v, 0, sizeof v)

const int MAXN = 105;
char grid[MAXN][MAXN], old[MAXN][MAXN];

int main(void) { 
   cin.sync_with_stdio(0);

   int CASES; cin >> CASES;
   for (int tt=1; tt<=CASES; ++tt) { // caret here
      int R; cin >> R;

      ZERO(grid);
      int n = 0;
      for (int i=0; i<R; ++i) {
         int x1, x2, y1, y2; cin >> x1 >> y1 >> x2 >> y2;
         relaxmax(n, x2);
         relaxmax(n, y2);
         for (int x=x1; x<=x2; ++x) {
            for (int y=y1; y<=y2; ++y) {
               grid[y][x] = 1;
            }
         }
      }

      int ans;
      for (ans=0;; ++ans) {
         bool alive = false;
         for (int y=1; y<=n; ++y) {
            for (int x=1; x<=n; ++x) {
               old[y][x] = grid[y][x];
               alive |= grid[y][x];
            }
         }
         if (!alive) {
            break;
         }

         for (int y=1; y<=n; ++y) {
            for (int x=1; x<=n; ++x) {
               if (!old[y-1][x] && !old[y][x-1]) {
                  grid[y][x] = 0;
               } else if (old[y-1][x] && old[y][x-1]) {
                  grid[y][x] = 1;
               }
            }
         }

         // for (int i=1; i<=n; ++i) {
         //    for (int j=1; j<=n; ++j) {
         //       fprintf(stderr, "%d", int(grid[i][j]));
         //    }
         //    fprintf(stderr, "\n");
         // }
         // fprintf(stderr, "\n");
      }

      cout << "Case #" << tt << ": " << ans << endl;
   }

   return 0;
} 
