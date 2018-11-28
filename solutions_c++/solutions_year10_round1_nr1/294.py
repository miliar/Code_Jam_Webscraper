#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <queue>
#include <list>
#include <stack>
#include <string>
#include <fstream>
#include <math.h>
#include <limits>
#include <set>
#include <map>
#include <sstream>
#include <stdio.h>
#include <time.h>
#include <memory.h>
#include <cassert>
using namespace std;

///////////////// macros and typedefs ///////////////////
#define rep(i, n) for (int i = 0, _n = (n); i <= _n; ++i)
#define repd(i, n) for (int i = (n)-1; i >= 0; --i)
#define DEB(k) cerr<<"debug: "#k<<"="<<k<<endl;
#define clear(a) memset((a), 0, sizeof(a));
#define all(c) (c).begin(), (c).end()
#define mp(a, b) make_pair(a, b)
#define l(c) (int)((c).size())
#define sqr(a) ((a)*(a))
#define inf 0x7f7f7f7f
#define pb push_back
#define ppb pop_back
#define y second
#define x first
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;

int n, k;
char t[50][51];
char t2[50][51];

void rot() {
   for (int i = 0; i < n; i++) {
      int cur = n-1;
      for (int j = n-1; j >= 0; j--)
         if (t[i][j] != '.') t2[i][cur] = t[i][j], cur--;
      for (int j = 0; j <= cur; j++) t2[i][j] = '.';
      t2[i][n] = 0;
   }
}

bool can(int I, int J) {
   char c = t2[I][J];
   int v = 0, h = 0, d = 0, d2 = 0;
   for (int i = I; i < n; i++)
      if (t2[i][J] != c) break;
      else v++;
   if (v >= k) return true;
   for (int j = J; j < n; j++)
      if (t2[I][j] != c) break;
      else h++;
   if (h >= k) return true;
   for (int i = I, j = J; i < n && j < n; i++, j++)
      if (t2[i][j] != c) break;
      else d++;
   if (d >= k) return true;
   for (int i = I, j = J; i >= 0 && j < n; i--, j++)
      if (t2[i][j] != c) break;
      else d2++;
   if (d2 >= k) return true;
   return false;
}

void check(bool& r, bool& b) {
   for (int i = 0; i < n; i++)
      for (int j = 0; j < n; j++)
         if (t2[i][j] != '.')
            if (can(i, j)) {
               if (t2[i][j] == 'R') r = true;
               else b = true;
            }
}

void solution(int test)
{
   scanf("%d %d\n", &n, &k);
   for (int i = 0; i < n; i++)
      gets(t[i]);
   rot();
   bool wR = 0, wB = 0;
   check(wR, wB);
   printf("Case #%d: ", test);
   if (wR && !wB) puts("Red");
   else if (!wR && wB) puts("Blue");
   else if (wR && wB) puts("Both");
   else puts("Neither");
}

#define NAME "A-large"
   
int main()
{
   freopen(NAME".in", "rt", stdin);
   freopen(NAME".out", "wt", stdout);
   int tests;
   scanf("%d", &tests);
   for (int i = 0; i < tests; i++)
      solution(i+1);
   return 0;
}
