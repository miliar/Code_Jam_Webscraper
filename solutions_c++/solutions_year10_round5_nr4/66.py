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

const int m = 1000000007;

int n, b;
int vis[10][10];

TT rec(int st, int s)
{
   if (s == n) return 1;
   TT ans = 0;
   for (int i = st; i+s <= n; i++) {
      int j = i;
      int k = 0;
      int ok = 1;
      int kk = -1;
      while (j) {
         if (vis[k][j % b]) {ok = 0; break;}
         vis[k][j % b] = 1;
         kk = k;
         j /= b;
         k++;
      }

      if (ok) ans = (ans + rec(i+1, s+i)) % m;

      j = i;
      k = 0;
      while (k <= kk) {
         vis[k][j % b] = 0;
         j /= b;
         k++;
      }   
   }
   return ans;
}


int main()
{
   freopen("input.txt" ,"rt", stdin); freopen("output.txt", "wt", stdout);
   
   int T, sc;
   cin >> T;
   for (sc = 0; sc < T; sc++) {
      cin >> n >> b;

      cout << "Case #" << sc+1 << ": ";
      cout << rec(1, 0);
      cout << endl;
   }
   

   fclose(stdin); fclose(stdout);
   return 0;   
}