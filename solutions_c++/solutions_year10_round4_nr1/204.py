#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <vector>

using namespace std;

template<typename T> inline T sqr( const T &a ) { return a*a; }
#define MINUS1(v) memset(v, -1, sizeof v)

struct point { int x, y; };

int n;
int table[105][105], tn[105][105];

point flip1(int n, point p) {
   return (point){p.y, p.x};
}

point flip2(int n, point p) {
   int o = p.x+p.y-n+1;
   return (point){p.x-o, p.y-o};
}

void put(int y, int x, int value) {
   if (tn[y][x] != -1 && tn[y][x] != value) {
      throw 1;
   }
   tn[y][x] = value;
}

void put(point p, int value) {
   put(p.y, p.x, value);
}

void noconflicts(int y1, int x1, int w) {
   for (int i=0; i<w; ++i) {
      MINUS1(tn[i]);
   }

   for (int i=0; i<n; ++i) {
      for (int j=0; j<n; ++j) {
         int v = table[i][j];
         point p = {j-y1, i-x1};
         put(p, v);
         put(flip1(w, p), v);
         put(flip2(w, p), v);
         put(flip1(w, flip2(w, p)), v);
      }
   }
}

int main(void) { 
   cin.sync_with_stdio(0);

   int CASES; cin >> CASES;
   for (int tt=1; tt<=CASES; ++tt) { // caret here
      cin >> n;
      for (int i=0; i<n; ++i) {
         for (int j=0; j<=i; ++j) {
            cin >> table[i-j][j];
         }
      }
      for (int i=n; i<2*n-1; ++i) {
         int w = 2*n-1-i;
         for (int j=0; j<w; ++j) {
            cin >> table[n-1-j][i-n+1+j];
         }
      }

      // for (int i=0; i<n; ++i) {
      //    for (int j=0; j<n; ++j) {
      //       fprintf(stderr, " %d", table[i][j]);
      //    }
      //    fprintf(stderr, "\n");
      // }

      int ans = 999999999;
      for (int w=n; w<=3*n+3; ++w) {
         bool found = false;
         for (int y1=0; y1>=-w; --y1) {
            for (int x1=0; x1>=-w; --x1) {
               try {
                  noconflicts(y1, x1, w);
                  found = true;
                  goto out;
               } catch (int e) { }
            }
         }
      out:
         if (found) {
            ans = sqr(w) - sqr(n);
            break;
         }
      }

      cout << "Case #" << tt << ": " << ans << endl;
   }

   return 0;
} 
