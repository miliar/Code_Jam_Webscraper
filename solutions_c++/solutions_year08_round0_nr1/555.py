# include <cstdio>
# include <map>
# include <string>
# include <algorithm>

using namespace std;

const int maxn = 200, maxm = 1100, infi = 1000000000;

int n, m, num, a[maxm];
int f[maxm][maxn];
map<string, int> hash;
char s[1000];

int find(char*s) {
  map<string, int>::iterator it = hash.find((string)s);
  if (it != hash.end()) return it->second;
  return hash[(string)s] = num++;
}

void init() {
  scanf("%d", &n);
  num = 0; hash.clear(); gets(s);
  for (int i = 0; i < n; ++i) {
    gets(s);
    find(s);
  }
  scanf("%d", &m); gets(s);
  for (int i = 0; i < m; ++i) {
    gets(s);
    a[i] = find(s);
  }
}

void solve() {
  fill_n(f[0], maxn * maxm, infi);
  for (int i = 0; i < n; ++i) if (a[0] != i) f[0][i] = 0;
  for (int i = 0; i < m - 1; ++i) 
    for (int j = 0, t; j < n; ++j) if ((t = f[i][j]) != infi) 
      if (a[i + 1] == j) {
	for (int k = 0; k < n; ++k)
	  if (a[i + 1] != k) 
	    f[i + 1][k] <?= t + 1;
      }
      else f[i + 1][j] <?= t;

  int res = infi;
  for (int i = 0; i < n; ++i) res <?= f[m - 1][i];
  printf("%d\n", res);
}

int main() {
  int tt, i;
  for (scanf("%d", &tt), i = 1; i <= tt; ++i) {
    printf("Case #%d: ", i);
    init();
    solve();
  }

  return 0;
}
