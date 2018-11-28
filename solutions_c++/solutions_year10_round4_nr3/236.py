#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#include <vector>
#include <string>
#include <iostream>
#include <cctype>
#include <sstream>
#include <algorithm>
#include <iomanip>
#include <set>
#include <queue>

using namespace std;

typedef long double real;
typedef long long TT;

#define PB push_back
#define SQR(x) ((x)*(x))
#define PII pair<int, int>
#define VI vector<int>
#define VVI vector<VI >
#define VS vector<string>
#define VTT vector<TT>
#define VR vector<real>
#define A first
#define B second

const int maxn = 128;

int a[maxn][maxn], b[maxn][maxn];

int main()
{
   freopen("input.txt" ,"rt", stdin); freopen("output.txt", "wt", stdout);
   
   int T, sc;
   cin >> T;
   for (sc = 0; sc < T; sc++) {
      memset(a, 0, sizeof(a));
      int r;
      cin >> r;
      int X1 = maxn, Y1 = maxn, X2 = 0, Y2 = 0;
      int i, j, k, cnt = 0;
      for (i = 0; i < r; i++) {
         int x1, y1, x2, y2;
         cin >> x1 >> y1 >> x2 >> y2;
         if (x1 < X1) X1 = x1;
         if (x2 > X2) X2 = x2;
         if (y1 < Y1) Y1 = y1;
         if (y2 > Y2) Y2 = y2;
         for (j = x1; j <= x2; j++)
            for (k = y1; k <= y2; k++) {
               if (!a[j][k]) cnt++;
               a[j][k] = 1;
            }   
      }
      
      int ans = 0;
      while (cnt) {
         memcpy(b, a, sizeof(a));
         for (i = X1; i <= X2; i++)
            for (j = Y1; j <= Y2; j++) {
               if (a[i][j] && !a[i-1][j] && !a[i][j-1]) {
                  cnt--;
                  b[i][j] = 0;
               }   
               if (!a[i][j] && a[i-1][j] && a[i][j-1]) {
                  cnt++;
                  b[i][j] = 1;
               }
            }
         
        /* for (i = X1; i <= X2; i++) {
            for (j = Y1; j <= Y2; j++) {
               cout << b[i][j];
            }
            cout << endl;
         }   
         cout << endl;*/
            
         ans++;
         if (!cnt) break;
         memcpy(a, b, sizeof(b));
      }

      cout << "Case #" << sc+1 << ": ";
      cout << ans;
      cout << endl;
   }
   

   fclose(stdin); fclose(stdout);
   return 0;   
}