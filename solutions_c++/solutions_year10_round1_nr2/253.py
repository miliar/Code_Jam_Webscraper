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

int D, I, M, N;
int a[100];
int dp[101][256];

int get(int A, int prev) {
   if (A == N) return 0;
   if (dp[A][prev] != -1) return dp[A][prev];
   dp[A][prev] = inf;
   for (int i = 0; i < 256; i++) {
      if (abs(i-prev) > M) continue;
      dp[A][prev] = min(dp[A][prev], get(A+1, i) + abs(i-a[A])); // change it
      dp[A][prev] = min(dp[A][prev], get(A, i) + I); // ins before
   }
   dp[A][prev] = min(dp[A][prev], get(A+1, prev) + D); // del it
   return dp[A][prev];
}

void solution(int test)
{
   memset(dp, -1, sizeof(dp));
   scanf("%d %d %d %d", &D, &I, &M, &N);
   for (int i = 0; i < N; i++)
      scanf("%d", a+i);
   int ret = inf;
   for (int i = 0; i < 256; i++) {
      int cur = get(0, i);
      ret = min(ret, cur);
   }
   printf("Case #%d: %d\n", test, ret);
}

#define NAME "B-large"
   
int main()
{
   freopen(NAME".in", "rt", stdin);
   freopen(NAME".out", "wt", stdout);
   int tests;
   scanf("%d", &tests);
   for (int i = 0; i < tests; i++) {
      cerr << i << endl;
      solution(i+1);
   }
   return 0;
}
