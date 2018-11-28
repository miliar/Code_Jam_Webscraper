#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <assert.h>
using namespace std;
#define maxh 100
#define maxw 100
#define maxn ((maxh+2)*maxw)
int parent[maxn], rank[maxn], M[maxw+5][maxh+5], h, w;
inline int c2n(int x, int y) { return x*(maxh+2)+y; }
inline pair<int, int> n2c(int x) { return make_pair(x/(maxh+2), x%(maxh+2)); }
void makeset(int x) {
  parent[x] = x;
  rank[x] = 0;
}
int f(int x) {
  if (parent[x] == x)
    return x;
  else
    return parent[x] = f(parent[x]);
}
void make_union(int x, int y) {
  int xr = f(x), yr = f(y);
  if (rank[xr] > rank[yr])
    parent[yr] = xr;
  else if (rank[xr] < rank[yr])
    parent[xr] = yr;
  else if (xr != yr)
    parent[yr] = xr, rank[xr]++;
}
void set_next(int x, int y) {
  int dx[4] = {0, -1, 1, 0};
  int dy[4] = {1, 0, 0, -1};
  int lowest = M[x][y], lx = -1, ly = -1;
  for (int d = 0; d < 4; ++d) {
    int nx = x+dx[d], ny = y+dy[d];      
    if (nx<0 || nx>=w || ny>=h || ny<0)
      continue;
    int childn = M[nx][ny];
    if (childn >= lowest)
      continue;
    lowest = childn;
    lx = nx, ly = ny;
  }
  if (lx != -1)
    make_union(c2n(x,y), c2n(lx,ly));
}
int main() {
  int nocases;
  cin >> nocases;
  for (int rr = 1; rr <= nocases; ++rr) {
    cin >> h >> w;
    for (int i = h-1; i >= 0; --i)
      for (int j = 0; j < w; ++j) {
	int x;
	cin >> x;
	M[j][i] = x;
      }
    for (int i = 0; i < w; ++i)
      for (int j = 0; j < h; ++j)
	makeset(c2n(i, j));
    for (int i = 0; i < w; ++i)
      for (int j = 0; j < h; ++j)
	set_next(i, j);
    char c2l[maxn];
    char at = 'a';
    memset(c2l, -1, sizeof(c2l));
    printf("Case #%d:\n", rr);
    for (int y = h-1; y >= 0; --y) {
      for (int x = 0; x < w; ++x) {
	int q = f(c2n(x,y));
	if (x)
	  cout << " ";
	if (c2l[q] != -1) 
	  cout << c2l[q];
	else {
	  c2l[q] = at;
	  cout << at++;
	}
      }
      cout << endl;
    }	  
  }
  return 0;
}
