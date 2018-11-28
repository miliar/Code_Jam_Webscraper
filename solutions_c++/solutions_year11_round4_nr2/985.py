#undef DEBUG

#ifdef DEBUG
#define debug(...) fprintf(stderr, __VA_ARGS__)
#else
#define debug(...) do ; while(0)
#define NDEBUG
#endif

#include <assert.h>
#include <stdbool.h>
#include <stdio.h>
#include <math.h>

using namespace std;

#define EPSILON 1e-6

int main ()
{
  int T;

  scanf("%d\n", &T);
  for (int test=1; test<=T; test++) {
    // input
    int R, C, D;
    scanf("%d %d %d\n", &R, &C, &D);
    int d[R+1][C+1];
    unsigned long long w[R+1][C+1];
    double x[R+1][C+1], y[R+1][C+1];
    for (int r=0; r<=R; r++) {
      w[r][0] = 0; x[r][0] = y[r][0] = 0.0;
    }
    for (int c=1; c<=C; c++) {
      w[0][c] = 0; x[0][c] = y[0][c] = 0.0;
    }
    for (int r=1; r<=R; r++) {
      for (int c=1; c<=C; c++) {
        d[r][c] = getchar() - '0';
        w[r][c] = w[r-1][c] + w[r][c-1] - w[r-1][c-1] + D + d[r][c];
        x[r][c] = x[r-1][c] * w[r-1][c] + x[r][c-1] * w[r][c-1]
          - x[r-1][c-1] * w[r-1][c-1] + (r - 0.5) * (D + d[r][c]);
        x[r][c] /= w[r][c];
        y[r][c] = y[r-1][c] * w[r-1][c] + y[r][c-1] * w[r][c-1]
          - y[r-1][c-1] * w[r-1][c-1] + (c - 0.5) * (D + d[r][c]);
        y[r][c] /= w[r][c];
      }
      scanf("\n");
    }
#ifdef DEBUG
    for (int r=1; r<=R; r++) {
      for (int c=1; c<=C; c++)
        debug("%llu ", w[r][c]);
      debug("\n");
    }   
    for (int r=1; r<=R; r++) {
      for (int c=1; c<=C; c++)
        debug("(%0.3lf, %0.3lf) ", x[r][c], y[r][c]);
      debug("\n");
    }   
#endif
    // calculate
    int k = R > C ? C : R;
    while (k >= 3) {
      debug("trying k=%d\n", k);
      for (int r=1; r<=R-k+1; r++)
        for (int c=1; c<=C-k+1; c++) {
          int rp=r-1;
          int cp=c-1;
          int rk=r+k-1;
          int ck=c+k-1;
          debug("trying (%d,%d) - (%d,%d), ", r, c, rk, ck);
          double cx = x[rk][ck] * w[rk][ck] - x[rp][ck] * w[rp][ck]
            - x[rk][cp] * w[rk][cp] + x[rp][cp] * w[rp][cp];
          double cy = y[rk][ck] * w[rk][ck] - y[rp][ck] * w[rp][ck]
            - y[rk][cp] * w[rk][cp] + y[rp][cp] * w[rp][cp];
          cx -= d[r][c] * (r - 0.5) + d[rk][c] * (rk - 0.5)
            + d[r][ck] * (r - 0.5) + d[rk][ck] * (rk - 0.5);
          cy -= d[r][c] * (c - 0.5) + d[rk][c] * (c - 0.5)
            + d[r][ck] * (ck - 0.5) + d[rk][ck] * (ck - 0.5);
          unsigned long long ww = w[rk][ck] - w[rp][ck] - w[rk][cp]
            + w[rp][cp] - d[r][c] - d[rk][c] - d[r][ck] - d[rk][ck];
          cx /= ww;
          cy /= ww;
          debug("center (%0.6lf, %0.6lf)\n", cx, cy);
          debug("wanted (%0.6lf, %0.6lf)\n", (r+rk-1) / 2.0, (c+ck-1) / 2.0);
          if (fabs(cx - (r+rk-1) / 2.0) < EPSILON &&
              fabs(cy - (c+ck-1) / 2.0) < EPSILON) {
            printf("Case #%d: %d\n", test, k);
            goto next;
          }
        }
      k--;
    }          
    // negative answer
    printf("Case #%d: IMPOSSIBLE\n", test);
  next:
    ;
  }
  return 0;
}
