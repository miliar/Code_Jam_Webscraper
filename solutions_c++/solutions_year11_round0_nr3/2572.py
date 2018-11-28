#include<cstdio>
#include<cstring>
#include<algorithm>
#define infile "c.in"
#define outfile "c.out"
#define nMax 1013
#define sMax 1000013
#define inf (~(1<<31))

using namespace std;

int dp[2][sMax];
int v[nMax];
int n, sum, sum2, sol;

void init() {
  sum = sum2 = 0;
  sol = inf;
  for(int i = 0; i < 2; ++i)
    for(int j = 0; j < sMax; ++j)
      dp[i][j] = inf;
}

void read() {
  scanf("%d\n", &n);
  for(int i = 1; i <= n; ++i) {
    scanf("%d", &v[i]);
    sum ^= v[i];
    sum2 += v[i];
  }
}

void solve() {
  dp[0][0] = 0;
  int x;

  for(int i = 1; i <= n; ++i) {
    int cur = i&1;
    int prv = !cur;
    memcpy(dp[cur], dp[prv], sizeof(dp[prv]));
    for(int j = 0; j < sMax; ++j) {
      x = j ^ v[i];
      if(x < sMax && dp[prv][x]!=inf) {
        dp[cur][j] = min(dp[cur][j], dp[prv][x] + v[i]);
        if(j == (sum^j) && dp[cur][j]) sol = min(sol, dp[cur][j]);
      }
    }
  }
}

void write(int t) {
  printf("Case #%d: ", t);
  if(sol == inf) printf("NO");
  else printf("%d", sum2 - sol);
  printf("\n");
}

int main() {
  freopen(infile, "r", stdin);
  freopen(outfile, "w", stdout);

  int t;
  scanf("%d\n", &t);
  for(int i = 1; i <= t; ++i) {
    init();
    read();
    solve();
    write(i);
  }

  fclose(stdin);
  fclose(stdout);
  return 0;
}
