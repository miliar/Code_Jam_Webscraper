#include <cstdio>

int main()
{
  int C;
  scanf("%d", &C);
  for(int nc=1; nc<=C; ++nc) {
    int N, M, A;
    scanf("%d%d%d", &N, &M, &A);
    int xb, yb, xc, yc;
    for(xb = 0; xb <= N; ++xb) {
      for(xc = 0; xc <= N; ++xc) {
	for(yb = 0; yb <= M; ++yb) {
	  for(yc = 0; yc <= M; ++yc)
	    if(xb*yc - xc*yb == A) {
	      printf("Case #%d: 0 0 %d %d %d %d\n", nc, xb, yb, xc, yc);
	      goto done;
	    }
	}
      }
    }
    printf("Case #%d: IMPOSSIBLE\n", nc);
    continue;
  done:{}
  }
  return 0;
}
