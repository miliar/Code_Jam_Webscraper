#include<cstdio>
#include<cstring>
#include<vector>
#include<algorithm>
#define infile "dancing.in"
#define outfile "dancing.out"

using namespace std;

pair <int, int> computeFor(int s) {
  pair <int, int> r = pair<int, int>(-1, -1);
  for(int le = 0; le <= s; ++le) {
    for(int ri = le; le + ri <= s; ++ri) {
      int mi = s - le - ri;
      if(mi < le || mi > ri) continue;
      if(ri - le == 2) r.first = max(r.first, ri);
      if(ri - le < 2) r.second = max(r.second, ri);
    }
  }
  return r;
}

void solve(int test) {

  int n, s, p;
  scanf("%d %d %d", &n, &s, &p);

  int v[n];
  for(int i = 0; i < n; ++i) {
    scanf("%d", &v[i]);
  }

  vector < pair<int, int> > w;
  for(int i = 0; i < n; ++i) {
    w.push_back(computeFor(v[i]));
    //printf("%d %d\n", w.back().first, w.back().second);
  }

  int dp[n+1][s+1]; memset(dp, 0, sizeof(dp));
  for(int i = 1; i <= n; ++i) {
    for(int j = 0; j <= s; ++j) {
      dp[i][j] = max(dp[i][j], dp[i-1][j] + (w[i-1].second >= p));
      if(j && w[i-1].first != -1) dp[i][j] = max(dp[i][j], dp[i-1][j-1] + (w[i-1].first >= p));
    }
  }

  printf("Case #%d: %d\n", test, dp[n][s]);
}

int main() {
  freopen(infile, "r", stdin);
  freopen(outfile, "w", stdout);

  int t;
  scanf("%d\n", &t);

  for(int test = 1; test <= t; ++test) {
    solve(test);
  }

  fclose(stdin);
  fclose(stdout);
  return 0;
}
