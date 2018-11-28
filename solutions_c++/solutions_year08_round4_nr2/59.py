#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <cctype>
#include <vector>
#include <map>

using namespace std;

#define rep(i,n) for (int i=0;i<(n);i++)
#define foru(i,a,b) for (int i=(a);i<=(b);i++)
#define ford(i,a,b) for (int i=(a);i>=(b);i--)

int cas, A, ax, ay, bx, by, cx, cy, mix, miy, mx, my, n, m, p1x,p2x,p3x,p1y,p2y,p3y;

void solve() {
  ax = ay = 0;
  for (bx = 0; bx <= n; bx++) for (by = 0; by <= m; by++) if (bx != ax || by != ay) 
    for (cx = bx; cx <= n; cx++) for (cy = 0; cy <= m; cy++) if (cx != ax || cy != ay)
      if (cx != bx || cy != by) {
	mix = min(min(ax, bx), cx);
	miy = min(min(ay, by), cy);
	mx = max(max(ax, bx), cx);
	my = max(max(ay, by), cy);
	if (mx - mix <= n && my - miy <= m) {
	  p1x = ax - mix; p1y = ay - miy;
	  p2x = bx - mix; p2y = by - miy;
	  p3x = cx - mix; p3y = cy - miy;
	  if (abs((p2x - p1x) * (p3y - p1y) - (p2y - p1y) * (p3x - p1x)) == A) {
	    printf("%d %d %d %d %d %d\n", ax - mix, ay - miy, bx - mix, by - miy, cx - mix, cy - miy);
	    return;
	  }	
	}  
      }
  printf("IMPOSSIBLE\n");
}

int main() {
  cin >> cas;
  rep(tt, cas) {
    cin >>  n >> m >> A;
    printf("Case #%d: ", tt + 1);
    solve();
  }
  
}
