#include <cstdio>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

const int N = 105;
const int M = 1005;
const int INF = 1<<30;

map<string,int> ID;
int n, m;
int a[M];
char s[1024];

int dp[N][M];

int rec(int cur, int pos) {
  if (pos >= m) return 0;
  int& ret = dp[cur][pos];
  if (ret != -1) return ret;
  ret = INF;
  for (int i = 0; i < n; ++i) {
    if (i != a[pos]) {
      ret = min(ret, rec(i, pos+1) + int(i!=cur));
    }
  }
  return ret;
}



int main() {
 // freopen("A.in", "r", stdin);
 // freopen("A.out", "w", stdout);

  int T;
  scanf("%d", &T);

  for (int t = 1; t <= T; ++t) {
    ID.clear();
    scanf("%d", &n);
    getchar();
    for (int i = 0; i < n; ++i) {
      gets(s);
      ID[s] = i;
    }
    scanf("%d", &m);
    getchar();
    for (int i = 0; i < m; ++i) {
      gets(s);
      if (ID.count(s)) a[i] = ID[s];
      else a[i] = n;
    }
    memset(dp, 0xff, sizeof(dp));
    int ans = INF;
    for (int i = 0; i < n; ++i)
      ans = min(ans, rec(i, 0));

    printf("Case #%d: %d\n", t, ans);


  }

  return 0;
}