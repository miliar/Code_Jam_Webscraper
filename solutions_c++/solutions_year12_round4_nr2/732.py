#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

typedef long long LL;

const int MAXN = 1010;

struct Vec2
{
  int x, y;
} pos[MAXN];

int n, W, L;
int R[MAXN];
int vis[MAXN];

void init()
{
  scanf("%d%d%d", &n, &W, &L);
  for (int i = 0; i < n; ++i) scanf("%d", R + i);
}

LL sqr(int x)
{
  return (LL)x*x;
}

LL dist(int x0, int y0,  int x1, int y1)
{
  return sqr(x0 - x1) + sqr(y0 - y1);
}

int check(int x, int y, int l, int idx[])
{
  for (int i = 0; i < l; ++i)
    if (dist(x, y, pos[idx[i]].x, pos[idx[i]].y) < sqr(R[idx[i]] + R[idx[l]])) return 0;

  return 1;
}

int get_left(int i, int j, int &x, int &y)
{
  x = pos[j].x + R[i] + R[j];
  y = pos[j].y;

  return x <= W && y <= L;
}

int get_right(int i, int j, int &x, int &y)
{
  x = pos[j].x;
  y = pos[j].y + R[i] + R[j];

  return x <= W && y <= L;
}

int cal(int idx[])
{
  pos[idx[0]].x = 0;
  pos[idx[0]].y = 0;

  int x, y, flag;
  for (int i = 1; i < n; ++i) {

    flag = 0;
    for (int j = 0; j < i; ++j) {
      if (get_left(idx[i], idx[j], x, y)) {
	if (check(x, y, i, idx)) {
	  pos[idx[i]].x = x;
	  pos[idx[i]].y = y;
	  flag = 1;
	  break;
	}
      }
      if (get_right(idx[i], idx[j], x, y)) {
	if (check(x, y, i, idx)) {
	  pos[idx[i]].x = x;
	  pos[idx[i]].y = y;
	  flag = 1;
	  break;
	}
      }
    }

    if (!flag) return 0;
  }
  return 1;
}

void solve()
{
  int permu[11], flag = 0;
  for (int i = 0; i < n; ++i) permu[i] = i;

  do {
    if (cal(permu)) { flag = 1; break; }
  } while (next_permutation(permu, permu+n));
  flag = 1/flag;

  for (int i = 0; i < n; ++i) printf("%d %d%c", pos[i].x, pos[i].y,
				       i == n-1 ? '\n' : ' ');
}

int main()
{
  int t;
  scanf("%d", &t);
  for (int l = 1; l <= t; ++l) {
    init();
    printf("Case #%d: ", l);
    solve();
  }
  return 0;
}
