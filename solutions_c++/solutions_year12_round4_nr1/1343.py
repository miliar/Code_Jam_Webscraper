#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>

using namespace std;

#define f(i, a, b) for(int i = a; i < b; i++)
#define rep(i, n)  f(i, 0, n)

const int N = 10005;
int n, D;
int d[N], l[N];
map<int, int> dp[N];

int solve(int from, int i) {
  int dist = min(d[i] - from, l[i]);
  if(d[i] + dist >= D) return 1;
  if(dp[i].count(from)) return dp[i][from];
  for(int j = i + 1; j < n && d[j] <= d[i] + dist; j++) {
    if(solve(d[i], j)) return dp[i][from] = 1;
  }
  return dp[i][from] = 0;
}

int main(){
  int T; scanf("%d", &T); for(int test = 1; test <= T; test++) {
    printf("Case #%d: ", test);
    cin >> n;
    rep(i, n) {
      cin >> d[i] >> l[i];
      dp[i].clear();
    }
    cin >> D;
    printf("%s\n", solve(0, 0) ? "YES" : "NO");
  }
}
