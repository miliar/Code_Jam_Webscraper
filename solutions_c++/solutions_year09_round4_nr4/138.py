#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

#define SQR(a) ((a) * (a))

int case_cnt = 1;
int x[3];
int y[3];
int r[3];

double dist(double x1, double y1, double x2, double y2)
{
  return sqrt(SQR(x1 - x2) + SQR(y1 - y2));
}

int main(void)
{
  int t;
  scanf("%d", &t);
  while(t--) {
    int n;
    scanf("%d", &n);
    for(int i = 0; i < n; i++) {
      scanf("%d %d %d", &x[i], &y[i], &r[i]);
    }
    double res = 1e9;
    if(n == 1) { 
      res = r[0];
    }
    else if(n == 2) {
      res = max(r[0], r[1]);
    }
    else {
      for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
          if(i == j) continue;
          double tmp = (dist(x[i], y[i], x[j], y[j]) + r[i] + r[j]) / 2.0;
          for(int k = 0; k < n; k++) {
            if(k == i || k == j) continue;
            res = min(res, max((double) r[k], tmp));
          }
        }
      }
    }
    printf("Case #%d: %lf\n", case_cnt++, res);
  }  
    
  return 0;
}


