#include <cstdio>
#include <set>
#include <cmath>
#include <string>
#include <cstring>

using namespace std;

const int MAX = 42;
const double EPS = 1e-9;

int n;
double xs[MAX], ys[MAX], rs[MAX];

int mnum;
long long masks[10000];

double dist2(double x1, double y1, double x2, double y2){
  return ((x1-x2)*(x1-x2) +  (y1-y2)*(y1-y2));
}

void add_mask(double x, double y, double R){
  long long cmask = 0;
  int i;
  for (i=0; i<n; i++){
    if (sqrt(dist2(xs[i], ys[i], x, y)) + rs[i] <= R + EPS) cmask |= (1LL<<i);
  }
  masks[mnum++] = cmask;
}

int check(double R){
  mnum = 0;
  int i, j;
  for (i=0; i<n; i++){
    add_mask(xs[i], ys[i], R);
  }
  for (i=0; i<n; i++){
    for (j=i+1; j<n; j++){
      double d = sqrt(dist2(xs[i], ys[i], xs[j], ys[j]));
      if (d + rs[i] + rs[j] > 2*R + EPS) continue;
      if (d < EPS) continue;
      double pd = ((rs[i]*rs[i] - rs[j]*rs[j]) + d*d + 2*R*(rs[j]-rs[i])) / 2 / d;
      double h2 = (R-rs[i])*(R-rs[i]) - pd*pd;
      if (h2<0) h2=0;
      double h = sqrt(h2);
      double vx = (xs[j]-xs[i])/d;
      double vy = (ys[j]-ys[i])/d;
      add_mask(xs[i] + vx*pd - vy*h, ys[i] + vy*pd + vx*h, R);
      add_mask(xs[i] + vx*pd + vy*h, ys[i] + vy*pd - vx*h,R);
    }
  }
  for (i=0; i<mnum; i++){
    for (j=i+1; j<mnum; j++){
      if ((masks[i] | masks[j]) == ((1LL << n) - 1)) return 1;
    }
  }
  return 0;
}

int main(){
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int tn, t;
  scanf("%d", &tn);
  for (t=1; t<=tn; t++){
    printf("Case #%d: ", t);
    scanf("%d", &n);
    int i;
    for (i=0; i<n; i++){
      scanf("%lf%lf%lf", &xs[i], &ys[i], &rs[i]);
    }
    double l = 0, r = 5000;
    while (r - l > 1e-7){
      double q = (l+r)/2;
      if (check(q)) r = q;
      else l = q;
    }
    if (n==1){
      l=r=rs[0];
    }
    printf("%.7lf\n", (l+r)/2);
  }
  return 0;
}
