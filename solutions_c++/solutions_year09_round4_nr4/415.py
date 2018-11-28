#include <stdio.h>
#include <cmath>
#include <algorithm>
using namespace std;

int N;
double A[100];
double B[100];
double C[100];

#define SQR(a) ((a)*(a))
#define DIST(x1,y1,x2,y2) sqrt(SQR(x1-x2)+SQR(y1-y2))

int main() {
  int T;
  scanf("%d", &T);
  for (int tc = 1; tc <= T; tc++) {
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
      scanf("%lf%lf%lf", &A[i], &B[i], &C[i]);
    }
    printf("Case #%d: ", tc);
    if (N == 1) {
      printf("%lf\n", C[0]);
    } else if (N == 2) {
      printf("%lf\n", max(C[0], C[1]));
    } else if (N == 3) {
      double R = 123456789.0;
      for (int i = 0; i < 3; i++) {
        int j = (i+1) % 3;
        int k = (i+2) % 3;
        R = min(R, max((DIST(A[i], B[i], A[j], B[j])+C[i]+C[j])/2.0, C[k]));
      }
      printf("%lf\n", R);
    }
  }
}
