#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>
#include <cstring>
#include <cstdlib>
using namespace std;

const int MAX = 1010;
const double EPS = 1e-9;

int n, ok;
double xs[MAX], ys[MAX], zs[MAX], ps[MAX];
double P;

double dist(double x1, double y1, double z1, double x2, double y2, double z2){
  return fabs(x1-x2) + fabs(y1-y2) + fabs(z1-z2);
}

int check_pt(double x1, double y1, double z1){
  int i;
  for (i=1; i<=n; i++){
    if (dist(xs[i], ys[i], zs[i], x1, y1, z1) > P * ps[i] + EPS) return 0; 
  }
  return 1;
}

void check(double x1, double y1, double z1, double x2, double y2, double z2){
  int i, j;
  if (check_pt(x1, y1, z1)){
    ok = 1;
    return;
  }
  if (check_pt(x2, y2, z2)){
    ok = 1;
    return;
  }
  double ux = x2 - x1, uy = y2 - y1, uz = z2 - z1, t;
  for (i=1; i<=n; i++){
    if (fabs(ux) > EPS){
      t = (xs[i] - x1) / ux;
      if ((t > -EPS) && (t < 1+EPS) && (check_pt(x1 + ux*t, y1 + uy*t, z1 + uz*t))){
        ok = 1;
        return;
      }
    }
    if (fabs(uy) > EPS){
      t = (ys[i] - y1) / uy;
      if ((t > -EPS) && (t < 1+EPS) && (check_pt(x1 + ux*t, y1 + uy*t, z1 + uz*t))){
        ok = 1;
        return;
      }
    }
    if (fabs(uz) > EPS){
      t = (zs[i] - z1) / uz;
      if ((t > -EPS) && (t < 1+EPS) && (check_pt(x1 + ux*t, y1 + uy*t, z1 + uz*t))){
        ok = 1;
        return;
      }
    }
  }
  for (t=0.0001; t<=1; t+=0.0001){
    if (check_pt(x1+ux*t, y1+uy*t, z1+uz*t)){
      ok = 1;
      return;
    }
  }
  return;
}

int cool(double p){
  int i;
  P = p;
  ok = 0;
  for (i=1; i<=n; i++){
    double cd = P * ps[i];
    //Same plane
    check(xs[i] + cd, ys[i], zs[i], xs[i], ys[i] + cd, zs[i]);
    check(xs[i], ys[i] + cd, zs[i], xs[i] - cd, ys[i], zs[i]);
    check(xs[i] - cd, ys[i], zs[i], xs[i], ys[i] - cd, zs[i]);
    check(xs[i], ys[i] - cd, zs[i], xs[i] + cd, ys[i], zs[i]);
    //Higher
    check(xs[i] + cd, ys[i], zs[i], xs[i], ys[i], zs[i] + cd);
    check(xs[i], ys[i] + cd, zs[i], xs[i], ys[i], zs[i] + cd);
    check(xs[i] - cd, ys[i], zs[i], xs[i], ys[i], zs[i] + cd);
    check(xs[i], ys[i] - cd, zs[i], xs[i], ys[i], zs[i] + cd);
    //Lower
    check(xs[i] + cd, ys[i], zs[i], xs[i], ys[i], zs[i] - cd);
    check(xs[i], ys[i] + cd, zs[i], xs[i], ys[i], zs[i] - cd);
    check(xs[i] - cd, ys[i], zs[i], xs[i], ys[i], zs[i] - cd);
    check(xs[i], ys[i] - cd, zs[i], xs[i], ys[i], zs[i] - cd);
    /*check_pt(xs[i], ys[i], zs[i]);
    check_pt(xs[i] + cd, ys[i], zs[i]);
    check_pt(xs[i] - cd, ys[i], zs[i]);
    check_pt(xs[i], ys[i] + cd, zs[i]);
    check_pt(xs[i], ys[i] - cd, zs[i]);
    check_pt(xs[i], ys[i], zs[i] + cd);
    check_pt(xs[i], ys[i], zs[i] - cd);*/
    if (ok) return 1;
  } 
  return 0;
}

int main(){
  freopen("c.in", "r", stdin);
  freopen("c.out", "w", stdout);
  int tn, tst;
  scanf("%d", &tn);
  for (tst=1; tst<=tn; tst++){
    printf("Case #%d: ", tst);
    scanf("%d", &n);
    int i;
    for (i=1; i<=n; i++){
      scanf("%lf%lf%lf%lf", &xs[i], &ys[i], &zs[i], &ps[i]);
    }
    double l = 0, r = 1e7;
    while (r-l > 1e-7){
      double q = (l + r) / 2;
      if (cool(q)) r = q;
      else l = q;
    }
    printf("%.6lf\n", (l+r)/2.0);
  }
  return 0;
}