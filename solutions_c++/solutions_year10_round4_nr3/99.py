#include <cstdio>

int C;
int R;
int A[101][101];
int B[101][101];
int alive;

//#define pr printf
#define pr(...) (0)

int main() {
  int x,y;
  scanf("%d", &C);
  for(int tc=1;tc<=C;tc++) {
    scanf("%d", &R);
    for(x=0; x<101;x++) for(y=0;y<101;y++) A[x][y] = 0;
    alive=0;
    for(int i=0;i<R;i++) {
      int x1,y1,x2,y2;
      scanf("%d %d %d %d", &x1, &y1, &x2, &y2); x2++; y2++;
      for(x=x1; x<x2; x++) for(y=y1; y<y2; y++) A[x][y] = 1, alive++;
    }
    int t;
    for(t=0; alive; t++) {
      pr("t=%d: %d alive\n", t, alive);
      for(x = 1; x < 101; x++) for(y = 1; y < 101; y++)
        B[x][y] = A[x][y] ? (A[x][y-1] || A[x-1][y]) : (A[x][y-1] && A[x-1][y]);
      alive = 0;
      for(x = 1; x < 101; x++) for(y = 1; y < 101; y++)
        alive += (A[x][y] = B[x][y]);
    }
    printf("Case #%d: %d\n", tc, t);
  }
}


