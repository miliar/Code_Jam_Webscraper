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

const int maxn = 128;

int a[maxn], d[maxn*maxn];

int main()
{
   freopen("input.txt" ,"rt", stdin); freopen("output.txt", "wt", stdout);
   
   int T, sc;
   cin >> T;
   for (sc = 0; sc < T; sc++) {
      int i, j, k;
      TT L;
      int n;
      cin >> L >> n;
      for (i = 0; i < n; i++) cin >> a[i];
      sort(a+0, a+n);
      
      TT ans = 0;
      if (L > 11000) {
         ans = (L-11000) / a[n-1] + 1;
         L -= ans * a[n-1];
      }
      
      memset(d, 255, sizeof(d));
      d[0] = 0;
      for (i = 0; i < L; i++) 
         if (d[i] >= 0) 
            for (j = 0; j < n; j++) {
               k = i + a[j];
               if (d[k] < 0 || d[k] > d[i] + 1) d[k] = d[i] + 1;
            }      

      cout << "Case #" << sc+1 << ": ";
      if (d[L] > 0) cout << d[L] + ans; else cout << "IMPOSSIBLE";
      cout << endl;
   }
   

   fclose(stdin); fclose(stdout);
   return 0;   
}