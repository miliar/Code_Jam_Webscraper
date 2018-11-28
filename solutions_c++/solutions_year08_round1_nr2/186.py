# include <cstdio>
# include <cstring>

int n, m;
int like[110][20], malted[110][20], tot[110];

void init() {
  scanf("%d%d", &n, &m);
  for (int i = 0; i < m; ++i) {
    scanf("%d", tot + i);
    for (int j = 0; j < tot[i]; ++j)
      scanf("%d%d", like[i] + j, malted[i] + j), like[i][j]--;
  }
}

void solve() {
  int best = n + 1, res;
  for (int i = 0; i < (1 << n); ++i) {
    int count = 0, sat = 0;
    for (int j = 0; j < n; ++j) if (i& (1<<j)) count++;
    for (int j = 0; j < m; ++j) {
      for (int k = 0; k < tot[j]; ++k) {
	if ((i & (1 << like[j][k])) > 0 && malted[j][k] 
	    || (i & (1 << like[j][k])) == 0 && !malted[j][k]) {
	  sat++;
	  break;
	}
      }
    }
    if (sat == m) {
      if (count < best) best = count, res = i;
    }
  }

  if (best > n) printf(" IMPOSSIBLE\n");
  else {
    for (int i = 0; i < n; ++i) if (res & (1 << i)) printf(" 1");
    else printf(" 0");
    puts("");
  }
}

int main() {
  int n, i;
  for (scanf("%d", &n), i = 1; i <= n; ++i) {
    printf("Case #%d:", i);
    init();
    solve();
  }
}
