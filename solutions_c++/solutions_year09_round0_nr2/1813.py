#include <cstdio>
#include <cstring>
#include <string.h>
using namespace std;

const int MAXN = 100, MAXM = 100, MAXH = 10000;
int cases, n, m, map[MAXN + 2][MAXM + 2], res[MAXN + 2][MAXM + 2];
int ch[256];
char ich;
struct alt_list {
  int x, y;
  alt_list* next;
};
alt_list* height[MAXH];
char used[MAXN*MAXM];

int main () {
  int i, h, u, v, min;
  alt_list* p;

  for (i = 0; i < MAXH; ++i)
    height[i] = NULL;
  scanf("%d", &cases);
  for (i = 1; i <= cases; ++i) {
    printf("Case #%d:\n", i);
    scanf("%d %d", &n, &m);
    for (u = 1; u <= n; ++u)
      for (v = 1; v <= m; ++v) {
	scanf("%d", map[u]+v);
	p = new alt_list;
	p->x = u;
	p->y = v;
	p->next = height[map[u][v]];
	height[map[u][v]] = p;
	res[u][v] = (u - 1) * m + v - 1;
      }
    for (u = 0; u <= n + 1; u += n + 1)
      for (v = 0; v <= m + 1; ++v)
	map[u][v] = MAXH + 1;
    for (v = 0; v <= m + 1; v += m + 1)
      for (u = 0; u <= n + 1; ++u)
	map[u][v] = MAXH + 1;
    
    for (h = 0; h < MAXH; ++h) {
      for (p = height[h]; p != NULL; p = p->next) {
	u = p->x; v = p->y;
	min = MAXH;
	min = (map[u - 1][v] < min)?map[u - 1][v]:min;
	min = (map[u][v - 1] < min)?map[u][v - 1]:min;
	min = (map[u][v + 1] < min)?map[u][v + 1]:min;
	min = (map[u + 1][v] < min)?map[u + 1][v]:min;
	if (map[u][v] <= min)
	  continue;
	if (min == map[u - 1][v])
	  res[u][v] = res[u - 1][v];
	else if (min == map[u][v - 1])
	  res[u][v] = res[u][v - 1];
	else if (min == map[u][v + 1])
	  res[u][v] = res[u][v + 1];
	else if (min == map[u + 1][v])
	  res[u][v] = res[u + 1][v];
      }
      for (p = height[h]; p != NULL; height[h] = p = p->next)
	delete height[h];
      height[h] = NULL;
    }

    for (h = 0; h < MAXN*MAXM; ++h)
      used[h] = 0;
    ich = 'a' - 1;
    for (u = 1; u <= n; ++u)
      for (v = 1; v <= m; ++v) {
	if (!used[res[u][v]]) {
	  ++ich; used[res[u][v]] = ich;
	}
	printf("%c", used[res[u][v]]);
	if (v == m) 
	  printf("\n");
	else 
	  printf(" ");
      }
  }
}
