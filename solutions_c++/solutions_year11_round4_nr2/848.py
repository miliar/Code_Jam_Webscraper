#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>

using namespace std;

const double EPS = 1E-6;
inline int cmp(double a, double b=0) {
  if(fabs(a-b)<=EPS) return 0;
  if(a<b) return -1;
  return 1;
}

struct point {
  double x,y;
  point(double x=0, double y=0): x(x), y(y) {}

  point operator +(point q){ return point(x+q.x, y+q.y); }
  point operator -(point q){ return point(x-q.x, y-q.y); }
  point operator *(point q){ return x*q.x + y*q.y; }
  point operator *(double t){ return point(x*t, y*t); }
};

const int N = 16;

int nt, nt0;
int r, c, d;
int t[N][N];
int ans;

bool iscentroid(int x, int y, int k) {
  point cm = point(x-0.5+double(k)/2.0, y-0.5+double(k)/2.0);
  point p;

  for(int i=x ; i<x+k ; i++)
    for(int j=y ; j<y+k ; j++)
      p = p + (point(i,j) - cm) * t[i][j];

  p = p - (point(x,y) - cm) * t[x][y];
  p = p - (point(x+k-1,y) - cm) * t[x+k-1][y];
  p = p - (point(x,y+k-1) - cm) * t[x][y+k-1];
  p = p - (point(x+k-1,y+k-1) - cm) * t[x+k-1][y+k-1];

  return (cmp(p.x)==0 && cmp(p.y)==0);
}

int main() {
  scanf(" %d", &nt0);
  for(nt = 1 ; nt <= nt0 ; nt++) {
    scanf(" %d %d %d", &r, &c, &d);
    for(int i=0 ; i<r ; i++)
      for(int j=0 ; j<c ; j++)
	scanf(" %1d", &t[i][j]);

    ans = -1;
    int m = min(r,c);
    for(int k=m ; k>=3 ; k--)
      for(int i=0 ; i<r-k+1 ; i++)
	for(int j=0 ; j<c-k+1 ; j++)
	  if(iscentroid(i,j,k)) {
	    ans = k;
	    goto END;
	  }

  END:
    printf("Case #%d: ", nt);
    if(ans == -1) puts("IMPOSSIBLE");
    else printf("%d\n", ans);
  }
  return 0;
}
