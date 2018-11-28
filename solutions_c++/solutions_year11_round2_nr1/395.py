#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
#include <cmath>
using namespace std;

const int MAXN = 210;

char mp[MAXN][MAXN];
int n;
double wp[MAXN], owp[MAXN], oowp[MAXN];

void init()
{
  scanf("%d", &n);
  for (int i = 0; i < n; ++i) scanf("%s", mp[i]);
}

void solve()
{
  for (int win, tot, i = 0; i < n; ++i) {
    win = tot = 0;
    for (int j = 0; j < n; ++j) {
      win += (mp[i][j] == '1');
      tot += (mp[i][j] != '.');
    }
    wp[i] = (double)win/tot; 
  }

  for (int otot, i = 0; i < n; ++i) {
    owp[i] = 0.0;
    otot = 0;

    for (int win, tot, j = 0; j < n; ++j) {
      if (mp[i][j] == '.') continue;
      ++otot;
      win = tot = 0;
      for (int l = 0; l < n; ++l) {
	if (l == i) continue;
	win += (mp[j][l] == '1');
	tot += (mp[j][l] != '.');
      }
      owp[i] += (double)win/tot;
    }

    owp[i] /= (double)otot;
  }

  for (int otot, i = 0; i < n; ++i) {
    oowp[i] = 0.0;
    otot = 0;
    for (int j = 0; j < n; ++j) 
      if (mp[i][j] != '.') ++otot, oowp[i] += owp[j];
    oowp[i] /= (double)otot;
  }

  for (int i = 0; i < n; ++i) 
    printf("%.9lf\n", 0.25*wp[i] +0.5*owp[i] + 0.25*oowp[i]);
}

int main()
{
  int t;
  scanf("%d", &t);
  for (int l = 1; l <= t; ++l) {
    printf("Case #%d:\n", l);
    init();
    solve();
  }
  return 0;
}
