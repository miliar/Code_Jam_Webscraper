#include<iostream>
using namespace std;

int cd, ci, m, n, ans;
int a[200];
int f[300][300];

void work()
{
  for (int i = 1; i <= n; ++i) {
    for (int j = 0; j <= 255; ++j) {
      f[i][j] = 10000000;
      f[i][j] <?= f[i-1][j]+cd;
      int l = j-m, r = j+m;
      if (l < 0) l = 0;
      if (r > 255) r = 255;
      for (int k = l; k <= r; ++k)
        f[i][j] <?= f[i-1][k]+abs(a[i]-j);
    }
    if (m != 0)
    for (int j = 0; j <= 255; ++j)
      f[i][j] <?= f[i][a[i]]+((abs(j-a[i])+m-1)/m)*ci;
  }
  ans = 10000000;
  for (int i = 0; i <= 255; ++i) ans <?= f[n][i];
}

int main()
{
  freopen("B-small-attempt1.in", "rt", stdin);
  freopen("B-small.out", "wt", stdout);
  int t; cin >> t;
  for (int i = 1; i <= t; ++i) {
    cin >> cd >> ci >> m >> n;
    for (int j = 1; j <= n; ++j) cin >> a[j];
    work();
    cout << "Case #" << i << ": " << ans << endl;
  }
  return 0;
}
