#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#include <vector>
#include <string>
#include <iostream>
#include <cmath>
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

const int maxn = 1024;

TT g[maxn];
TT vis[maxn];

int main()
{
   freopen("input.txt" ,"rt", stdin); freopen("output.txt", "wt", stdout);
   
   int T, sc;
   cin >> T;
   for (sc = 0; sc < T; sc++) {
      TT R, k, N, i, j;
      cin >> R >> k >> N;
      for (i = 0; i < N; i++) cin >> g[i];
      
      memset(vis, 0, sizeof(vis));
      TT passed = 0;
      TT cur = 0;
      VTT earn(1);
      int was = 0;
      TT ans = 0;
      for (i = 1; i <= R; i++) {       
         if (vis[cur] && !was) {
            was = 1;
            TT len = i-vis[cur];
            TT num = (R-i+1) / len;
            TT s = 0;
            for (j = vis[cur]; j < i; j++) s += earn[j];
            ans += s * num;
            i += len * num - 1;
         } else {
            vis[cur] = i;
            TT s = 0;
            for (j = 0; j < N; j++)
               if (s + g[(j+cur)%N] <= k) s += g[(j+cur)%N]; else break;
            if (!was) earn.PB(s);
            ans += s;
            cur = (cur + j) % N;
         }
      }
      
      cout << "Case #" << sc+1 << ": ";
      cout << ans;
      cout << endl;
   }
   

   fclose(stdin); fclose(stdout);
   return 0;   
}