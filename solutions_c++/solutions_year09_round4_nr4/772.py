#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

int n;
int s[][3] = {{0,1,2},{1,0,2},{2,0,1}};
double r[5], p[5][2];

double norma(double *p) {
  return sqrt(p[0]*p[0] + p[1]*p[1]);
}

double dist(double *p, double *q) {
  return sqrt((p[0]-q[0])*(p[0]-q[0]) +
	      (p[1]-q[1])*(p[1]-q[1]));
}

int main() {
  int nt;
  int cases = 1;

  scanf(" %d", &nt);
  while (nt--) {
    double res = 1e100;
    double vet[2], pp[2], qq[2];

    scanf(" %d", &n);
    for (int i = 0; i < n; i++)
      scanf(" %lf%lf%lf", &p[i][0], &p[i][1], &r[i]);

    if (n == 1) {
      printf("Case #%d: %lf\n", cases++, r[0]);
      continue;
    }

    if (n == 2) {
      printf("Case #%d: %lf\n", cases++, max(r[0],r[1]));
      continue;
    }

    for (int i = 0; i < 3; i++) {
      double nrm;
      int j = s[i][1], k = s[i][2];

      vet[0] = p[k][0] - p[j][0];
      vet[1] = p[k][1] - p[j][1];

      nrm = norma(vet);
      vet[0] /= nrm; vet[1] /= nrm;
      
      pp[0] = -vet[0] * r[j] + p[j][0];
      pp[1] = -vet[1] * r[j] + p[j][1];

      qq[0] = vet[0] * r[k] + p[k][0];
      qq[1] = vet[1] * r[k] + p[k][1];

      res = min(res, max(r[s[i][0]], 0.5 * dist(pp, qq)));
    }

    printf("Case #%d: %lf\n", cases++, res);
  }

  return 0;
}
