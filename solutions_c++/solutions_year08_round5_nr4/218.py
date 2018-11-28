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
const int MOD = 10007;
const int N = 128;
int dx[] = {1,2};
int dy[] = {2,1};

int table[N][N];
int dp[N][N];
int n, m, r;

int rec(int x, int y) {
  if (x+1 == n && y+1 == m) return 1;
  if (x >= n || y >= m) return 0;
  int& ret = dp[x][y];
  if (ret != -1) return ret;
  ret = 0;
  REP(i,2) {
    int nx = x+dx[i];
    int ny = y+dy[i];
    if (table[nx][ny]) continue;
    ret = (ret + rec(nx, ny))%MOD;
  }

  return ret;
}

int solve() {
  CLR(dp, 0xff);
  int ans = rec(0, 0);
  return ans;
}


int main() {
  freopen("D.in", "r", stdin);
  freopen("D.out", "w", stdout);

  int T;
  scanf("%d", &T);

  FOR(NT,1,T+1) {

    scanf("%d %d %d", &n, &m, &r);
    CLR(table, 0);
    for (int i = 0; i < r; ++i) {
      int x, y;
      scanf("%d %d", &x, &y);
      table[x-1][y-1] = 1;
    }
    int ans = solve();
    printf("Case #%d: %d\n", NT, ans);
  }


  return 0;
}