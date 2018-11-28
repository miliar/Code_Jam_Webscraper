#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

#define MAX_N 128
#define MAX_M 32

#define EPS 1e-7

struct point
{
  double x, y;
  
  point() {}
  point(double x, double y) : x(x), y(y) {}
};

point  operator - (point a, point b) { return point(a.x - b.x, a.y - b.y); }
double operator * (point a, point b) { return a.x * b.y - b.x * a.y; } 

void input(void);
void solve(void);

int dfs(int x);

int ccw(point a, point b, point c);
int between(point a, point b, point c);
int seg_intersect(point a, point b, point c, point d);
int do_intersect(int a, int b);

int n, m;
double P[MAX_N][MAX_M];
//int can[MAX_N][MAX_N];

int adj[MAX_N][MAX_N];
int used[MAX_N];
int skoj[MAX_N];

int case_cnt = 1;

int main(void)
{
  int t;
  scanf("%d", &t);
  while(t--) {
    input();
    solve();
  }
    
  return 0;
}

void input(void)
{
  scanf("%d %d", &n, &m);
  for(int i = 0; i < n; i++) 
    for(int j = 0; j < m; j++) scanf("%lf", &P[i][j]);
}

void solve(void)
{
  /*
  for(int i = 0; i < n; i++)
    for(int j = 0; j < n; j++) {
      if(i == j) { can[i][j] = 1; continue; }
      can[i][j] = !do_intersect(i, j);
    }
  */
  
  for(int i = 0; i < n; i++)
    for(int j = 0; j < n; j++) {
      adj[i][j] = 0;
      if(!do_intersect(i, j) && P[i][0] < P[j][0]) adj[i][j] = 1;
    }
    
  int res = 0;
  memset(skoj, -1, sizeof(skoj));
  for(int i = 0; i < n; i++) {
    memset(used, 0, sizeof(used));
    res += dfs(i);
  }
  
  printf("Case #%d: %d\n", case_cnt++, n - res);
}

int dfs(int x)
{
  if(used[x]++) return 0;
  for(int i = 0; i < n; i++) {
    if(!adj[x][i]) continue;
    if(skoj[i] == -1 || dfs(skoj[i])) {
      skoj[i] = x;
      return 1;
    }
  }
  return 0;
}

int ccw(point a, point b, point c)
{
  double v = ((b - a) * (c - a));
  
  if(v < -EPS) return -1;
  if(v > +EPS) return +1;
  return 0;
}

int between(point a, point b, point c)
{
  if(ccw(a, b, c) != 0) return 0;
  
  if(c.x < min(a.x, b.x) || c.x > max(a.x, b.x)) return 0;
  if(c.y < min(a.y, b.y) || c.y > max(a.y, b.y)) return 0;
  
  return 1;
}

int seg_intersect(point a, point b, point c, point d)
{
  if(between(a, b, c)) return 1;
  if(between(a, b, d)) return 1;
  if(between(c, d, a)) return 1;
  if(between(c, d, b)) return 1;
  
  return ccw(a, b, c) * ccw(a, b, d) + ccw(c, d, a) * ccw(c, d, b) == -2;
}

int do_intersect(int a, int b)
{
  for(int i = 0; i + 1 < m; i++)
    for(int j = 0; j + 1 < m; j++) 
      if(seg_intersect(point(i, P[a][i]), point(i + 1, P[a][i + 1]),
                       point(j, P[b][j]), point(j + 1, P[b][j + 1]))) return 1;
  return 0;
}


