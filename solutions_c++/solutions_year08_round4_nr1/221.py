#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>

using namespace std;

const int INF = 1<<30;                
const double EPS = 1e-9;
const double PI = acos(-1.0);

typedef vector<int> VI;
typedef vector<string> VS;
typedef long long LL;
typedef long double LD;

#define ALL(a) a.begin(),a.end()
#define PB push_back
#define MP make_pair
#define SZ(a) (int)a.size()
#define CLR(a,v) memset((a),(v),sizeof(a))
#define FOR(i,a,n) for(int i=(a);i<(n);++i)
#define FORD(i,a,n) for(int i=(a);i>=(n);--i)
#define REP(i,n) FOR(i,0,n) 



/// CODE HERE

const int N = 10005;
typedef pair<int,int> P;

int G[N]; // type
int C[N]; // val
LL dp[N][2];
int n, nneed;

LL rec(int x, int need) {
  if (2*x+1 >= n) return (C[x]==need ? 0 : INF);
  LL& ret = dp[x][need];
  if (ret != -1) return ret;
  ret = INF;
  int left = 2*x+1, right = 2*x+2;
  if (need == 1) {
    if (C[x]) { // can
      if (G[x]) { // and
        ret = min(ret, rec(left, 1)+rec(right, 1));
        ret = min(ret, 1+rec(left, 1)+rec(right, 0));
        ret = min(ret, 1+rec(left, 0)+rec(right, 1));
        ret = min(ret, 1+rec(left, 1)+rec(right, 1));
      } else { // or
        ret = min(ret, rec(left, 1)+rec(right, 0));
        ret = min(ret, rec(left, 0)+rec(right, 1));
        ret = min(ret, rec(left, 1)+rec(right, 1));
        ret = min(ret, 1+rec(left, 1)+rec(right, 1));
      }
    } else {
      if (G[x]) {
        ret = min(ret, rec(left, 1)+rec(right, 1));      
      } else {
        ret = min(ret, rec(left, 1)+rec(right, 0));
        ret = min(ret, rec(left, 0)+rec(right, 1));
        ret = min(ret, rec(left, 1)+rec(right, 1));
      }
    }
  } else {
    if (C[x]) { // can
      if (G[x]) {
        ret = min(ret, rec(left, 0)+rec(right, 1));
        ret = min(ret, rec(left, 1)+rec(right, 0));
        ret = min(ret, rec(left, 0)+rec(right, 0));
        ret = min(ret, 1+rec(left, 0)+rec(right, 0));
      } else {
        ret = min(ret, rec(left, 0)+rec(right, 0));
        ret = min(ret, 1+rec(left, 1)+rec(right, 0));
        ret = min(ret, 1+rec(left, 0)+rec(right, 1));
        ret = min(ret, 1+rec(left, 0)+rec(right, 0));
      }
    } else {
      if (G[x]) {
        ret = min(ret, rec(left, 1)+rec(right, 0));
        ret = min(ret, rec(left, 0)+rec(right, 1));
        ret = min(ret, rec(left, 0)+rec(right, 0));
      } else {
        ret = min(ret, rec(left, 0)+rec(right, 0));
      }
    }
  }
  return ret;
}

int main() {
  freopen("A.in", "r", stdin);
  freopen("A.out", "w", stdout);

  int T;
  scanf("%d", &T);

  FOR(NT,1,T+1) {
    scanf("%d %d", &n, &nneed);
    REP(i,(n-1)/2) scanf("%d %d", G+i, C+i);
    FOR(i,(n-1)/2,n) scanf("%d", C+i);
    CLR(dp, 0xff);
    LL ans = rec(0, nneed);
    printf("Case #%d: ", NT);
    if (ans >= INF) printf("IMPOSSIBLE");
    else printf("%I64d", ans);
    printf("\n");
    
  }


  return 0;
}