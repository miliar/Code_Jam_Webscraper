#include <stdio.h>
#include <math.h>

int N;
int u[40];
int p[40][3]; // X,Y,R
//int e[40][40];
#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))

double dist(int i, int j) {
  double x = p[i][0] - p[j][0];
  double y = p[i][1] - p[j][1];
  x *= x;
  y *= y;

  return (sqrt(x+y) + (double)p[i][2] + (double)p[j][2])/2.0;
}

/*
void flood(int i, int t) {
  u[i] = t;
  for (int j=0; j<N; j++) {
    if (
}*/

int main() {
  int C;
  scanf("%d", &C);

  for (int cs=1; cs<=C; cs++) {
    scanf("%d", &N);
    for (int i=0; i<N; i++)
      scanf("%d %d %d", p[i], p[i]+1, p[i]+2);

    /*
    double mr = 100000000.0;
    double min = 0.0;
    while (mr - min < 0.000001) {
      double nr = (mr + min) / 2.0
    }
    */

    double mr = 0.0;
    if (N > 2) {
      mr = dist(0,1);
      for (int i=0; i<N; i++)
        for (int j=i+1; j<N; j++) {
          double r = dist(i,j);
          if ((double)p[3-i-j][2] > r)
            r = (double)p[3-j-i][2];
          mr = min(mr, r);
        }
    } else {
      for (int i=0; i<N; i++) {
        double r = (double)p[i][2];
        mr = max(r,mr);
      }
    }
    printf("Case #%d: %.06f\n", cs, mr);
  }

  return 0;
}
