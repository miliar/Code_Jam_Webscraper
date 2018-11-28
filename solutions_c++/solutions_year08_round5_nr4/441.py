#include <cstdio>

typedef long long LL;

const LL M = 10007;

int main() {
  int T; scanf("%d", &T);
  for(int t=1; t<=T; ++t) {
    int w, h, r; scanf("%d%d%d", &h, &w, &r);
    LL A[101][101] = {0};
    while(r--) {
      int y, x; scanf("%d%d", &y, &x);
      A[y-1][x-1] = -1;
    }
    A[h-1][w-1] = 1;
    for(int y=h; y--;) {
      for(int x=w; x--;) {
	if (A[y][x] == -1) {
	  A[y][x] = 0;
	} else {
	  if (y+1 < h && x+2 < w && A[y+1][x+2] > 0) {
	    A[y][x] += A[y+1][x+2];
	    A[y][x] %= M;
	  }
	  if (y+2 < h && x+1 < w && A[y+2][x+1] > 0) {
	    A[y][x] += A[y+2][x+1];
	    A[y][x] %= M;
	  }
	}
      }
    }
    printf("Case #%d: %lld\n", t, A[0][0]); 
  }
}
