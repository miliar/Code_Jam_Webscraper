#include <cstdio>
#include <cmath>

using namespace std;

char lines[512][512];
double sumX[512][512];
double sumY[512][512];
double sum[512][512];

double box(int i, int j, double a[][512]) {
  if (i < 0 || j < 0) return 0;
  else return a[i][j];
}

double mass(int i, int j, int k, double a[][512]) {
  return box(i+k-1, j+k-1, a) - box(i-1, j+k-1, a) - box(i+k-1, j-1, a) + box(i-1, j-1, a);
}

double corners(int i, int j, int k, double a[][512]) {
  return mass(i, j, 1, a) + mass(i+k-1, j, 1, a) + mass(i, j+k-1, 1, a) + mass(i+k-1, j+k-1, 1, a);
}

int main() {
  int T; scanf("%d", &T);
  for(int t=1; t<=T; ++t) {
    int r, c, D; scanf("%d%d%d", &r, &c, &D);
    for(int i=0; i<r; ++i) {
      scanf(" %s", lines[i]);
    }
    sumX[0][0]   = 0;
    sumY[0][0]   = 0;
    sum[0][0]    = lines[0][0]-'0' + D;
    for(int j=1; j<c; ++j) {
      sumX[0][j] = sumX[0][j-1] + j*(lines[0][j]-'0' + D);				   
      sumY[0][j] = 0;
      sum[0][j]  = sum[0][j-1]  + lines[0][j]-'0' + D;
    }
    for(int i=1; i<r; ++i) {
      sumX[i][0] = 0;
      sumY[i][0] = sumY[i-1][0] + i*(lines[i][0]-'0' + D);
      sum[i][0]  = sum[i-1][0]  + lines[i][0]-'0' + D;
      for(int j=1; j<c; ++j) {
	sumX[i][j] = sumX[i-1][j] + sumX[i][j-1] - sumX[i-1][j-1] + j*(lines[i][j]-'0'+D);
	sumY[i][j] = sumY[i-1][j] + sumY[i][j-1] - sumY[i-1][j-1] + i*(lines[i][j]-'0'+D);
	sum[i][j]  = sum[i-1][j]  + sum[i][j-1]  - sum[i-1][j-1]  + lines[i][j]-'0'+D;
      }
    }
    for(int k=r<c?r:c; k>=3; --k) {
      for(int i=0; i+k<=r; ++i) {
	for(int j=0; j+k<=c; ++j) {
	  double m  = mass(i, j, k, sum) - corners(i, j, k, sum);
	  double cx = (mass(i, j, k, sumX) - corners(i, j, k, sumX))/m;
	  double cy = (mass(i, j, k, sumY) - corners(i, j, k, sumY))/m;
	  //printf("i=%d j=%d k=%d cx=%g cy=%g\n", i, j, k, cx, cy);
	  if (fabs(cy - (i + i+k-1)/2.) < 1e-6 &&
	      fabs(cx - (j + j+k-1)/2.) < 1e-6) {
	    printf("Case #%d: %d\n", t, k);
	    goto out;
	  }
	}
      }
    }
    printf("Case #%d: IMPOSSIBLE\n", t);
  out:;
  }
}
