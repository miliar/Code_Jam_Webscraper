#include <cstdio>
#include <cmath>

using namespace std;

const double EPS = 1e-10;
const double STWO = sqrt(2.0);
const double PI = acos(-1.0);

double f, R, t, r, g;

double sqr(double x) { return x*x; }
double get(double r, double x) { return sqrt(sqr(r) - sqr(x)); }
double ff(double x) { return 0.5*x*sqrt(sqr(R-t-f) - sqr(x)) + 0.5*sqr(R-t-f)*asin(x/(R-t-f)); }

double carea(double X0, double Y0) {
  double X1 = X0+g-2*f, Y1 = Y0+g-2*f;
  double CY0 = get(R-t-f, X0), CX0 = get(R-t-f, Y0);
  if (CX0 < X1+EPS) {
    double a = ff(CX0) - ff(X0);
    a -= Y0*(CX0 - X0);
    return a;
  }
  double CY1 = get(R-t-f, X1), CX1 = get(R-t-f, Y1);
  if (CY1 < Y1+EPS) {
    double a = (g-2*f)*(CX1 - X0);
    a += ff(X1) - ff(CX1);
    a -= Y0*(X1 - CX1);
    return a;
  }
  return sqr(g-2*f);   
}

double area(double X0, double Y0) {
  double X1 = X0+g-2*f, Y1 = Y0+g-2*f;
  double CY0 = get(R-t-f, X0), CX0 = get(R-t-f, Y0);
  if (CX0 < X1+EPS) {
    if (CY0 < Y1+EPS) {
      double a = ff(CX0) - ff(X0);
      a -= Y0*(CX0 - X0);
      return a;
    }
    double CX1 = get(R-t-f, Y1);
    double a = (g-2*f)*(CX1 - X0);
    a += ff(CX0) - ff(CX1);
    a -= Y0*(CX0 - CX1);
    return a;
  }
  double CY1 = get(R-t-f, X1);
  if (CY1 < Y1+EPS) {
    if (CY0 < Y1+EPS) {
      double a = ff(X1) - ff(X0);
      a -= Y0*(X1 - X0);
      return a;
    }
    double CX1 = get(R-t-f, Y1);
    double a = (g-2*f)*(CX1 - X0);
    a += ff(X1) - ff(CX1);
    a -= Y0*(X1 - CX1);
    return a;
  }
  return sqr(g-2*f);  
}

double calc() {
  if (R-t < f + EPS) return 1.0;
  if (g < 2*f + EPS) return 1.0;
  double CC = 4.0/sqr(R)/PI;
  double prob = 0.0;
  for (double s = r+f; s*STWO < R-t-f + EPS; s += g+2*r) {
    double X0 = s, Y0 = s;
    double cur = carea(X0, Y0) * CC;
    Y0 += g+2*r;
    double CY0 = get(R-t-f, X0);
    for (; Y0 < CY0 + EPS; Y0 += g+2*r) {
      cur += 2*area(X0, Y0) * CC;
    }
    prob += cur;
  }   
  return 1.0 - prob;
}



int main() {
  freopen("C.in", "r", stdin);
  freopen("C.out", "w", stdout);

  int T;
  scanf("%d", &T);

  for (int tt = 1; tt <= T; ++tt) {
    
    scanf("%lf %lf %lf %lf %lf", &f, &R, &t, &r, &g);
    double p = calc();
    printf("Case #%d: %.6f\n", tt, p);
  }

  return 0;
}