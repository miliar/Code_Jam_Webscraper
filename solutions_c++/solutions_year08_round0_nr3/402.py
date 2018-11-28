#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <algorithm>

using namespace std;

#define rep(i, n) for (int i = 0; i < (n); i++)
#define foru(i, a, b) for (int i = (a); i <=(b); i++)
#define ford(i, a, b) for (int i = (a); i >=(b); i--) 

const double eps = 1e-8, pi = acos(-1.0);

int dcmp(double x) {
  return x < -eps ? -1 : x > eps;
}

double sqr(double x) {
  return x * x;
}

struct tnode {
  double x, y;
  tnode () {}
  tnode (double nx, double ny): x(nx), y(ny) {}
};

tnode operator+(const tnode &a, const tnode &b) {
  return tnode(a.x + b.x, a.y + b.y);
}

tnode operator-(const tnode &a, const tnode &b) {
  return tnode(a.x - b.x, a.y - b.y);
}

tnode operator*(const tnode &a, double d) {
  return tnode(a.x * d, a.y * d);  
}

tnode operator/(const tnode &a, double d) {
  return tnode(a.x / d, a.y / d);
}

double dis(const tnode &a, const tnode &b) {
  return sqrt(sqr(a.x - b.x) + sqr(a.y - b.y));
}

double f, R, t, r, g, rr, ret;
int cas;
tnode ori, a, b, c, d, p, q;

void init() {
  scanf("%lf%lf%lf%lf%lf", &f, &R, &t, &r, &g);  
  ori = tnode(0, 0);  
}

double sqrarea(const tnode &a, const tnode &b) {
  if (dcmp(a.x - b.x) <= 0 && dcmp(a.y - b.y) <= 0)
    return (b.x - a.x) * (b.y - a.y);
  return 0;
}

int inside(const tnode &t) {
  return dcmp(dis(t, ori) - rr) <= 0;
}

double area(const tnode &a, const tnode &b) {
  double d = dis(a, b);
  double alpha = asin((d / 2) / rr) * 2;
  double h = sqrt(sqr(rr) - sqr(d / 2));
  return alpha / 2 * rr * rr - (d / 2) * h;   
}

int cross(const tnode &a, const tnode &b, tnode &t) {
  if (dcmp(a.x - b.x) == 0) {
    t.x = a.x;
    if (dcmp(sqr(rr) - sqr(t.x)) < 0) return 0;
    t.y = sqrt(sqr(rr) - sqr(t.x));
    return dcmp(a.y - t.y) <= 0 && dcmp(t.y - b.y) <= 0;
  } else {
    t.y = a.y;
    if (dcmp(sqr(rr) - sqr(t.y)) < 0) return 0;
    t.x = sqrt(sqr(rr) - sqr(t.y));
    return dcmp(a.x - t.x) <= 0 && dcmp(t.x - b.x) <= 0;
  }
}

double calc() {
  rr = R - t - f;
  a = a + tnode(f, f);
  b = b + tnode(-f, f);
  c = c + tnode(-f, -f);
  d = d + tnode(f, -f);      
  //  printf("%lf %lf %lf %lf\n", a.x, a.y, c.x, c.y);
  if (inside(a) && inside(b) && inside(c) && inside(d)) return sqrarea(a, c);

  if (dcmp(a.x - c.x) <= 0 && dcmp(a.y - c.y) <= 0) {
    if (cross(a, b, p) && cross(a, d, q)) {
      return dis(a, p) * dis(a, q) / 2 + area(p, q);
    }

    if (cross(a, b, p) && cross(d, c, q)) return (dis(d, q) + dis(a, p)) * (d.y - a.y) / 2 + area(p, q);
    if (cross(b, c, p) && cross(a, d, q)) return (dis(p, b) + dis(q, a)) * (b.x - a.x) / 2 + area(p, q);
    if (cross(b, c, p) && cross(d, c, q)) return (dis(q, d) + b.x - a.x) * (q.y - p.y) / 2 + sqrarea(a, p) + area(p, q);
  }
  return 0;  
}

void solve() {
  ret = 0;
  for (double x = ori.x + r; dcmp(x - (R - t - f)) <= 0; x += g + 2 * r)
    for (double y = ori.y + r; dcmp(y - (R - t - f)) <= 0; y += g + 2 * r) {
      a = tnode(x, y);
      b = a + tnode(g, 0);
      c = b + tnode(0, g);
      d = c + tnode(-g, 0);      
      double tmp = calc();
            ret += tmp;
      //      printf("%lf %lf %lf\n", x, y, ret);
    }
  double s = pi * R * R / 4;
  ret /= s;
  ret = 1 - ret;
}

int main() {    
  scanf("%d", &cas);
  rep(tt, cas) {
    init();
    solve();
    printf("Case #%d: %.6lf\n", tt + 1, ret);
  }
  return 0;
}
