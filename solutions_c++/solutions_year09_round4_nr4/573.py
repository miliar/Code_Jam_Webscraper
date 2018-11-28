#include<iostream>
#include<cmath>
#include<algorithm>
using namespace std;

struct node {
  double x, y, r;
  node(){}
  node(double x2, double y2, double r2): x(x2), y(y2), r(r2){}
  friend double dist(const node &p1, const node &p2) {
    double dx = p1.x - p2.x, dy = p1.y - p2.y;
    return sqrt(dx*dx + dy*dy);
  }
  bool operator<(const node &b) const {
    if (y != b.y) return y < b.y;
    if (x != b.x) return x < b.x;
    return r < b.r;
  }
};

int main() {
  int cases, q, n, i;
  node p[10];
  double r1, r2, ans;

  cin >> cases;
  for (q = 1; q <= cases; q++) {
    cin >> n;
    for (i = 0; i < n; i++) {
      cin >> p[i].x >> p[i].y >> p[i].r;
    }
    sort(p, p+n);
    
    ans = 0;
    for (i = 0; i < 3; i++) ans += p[i].r;
    for (i = 1; i < 3; i++) {
      ans += dist(p[i-1], p[i]);
    }
			      
    do {
      r1 = p[0].r;
      r2 = r1;
      if (n  == 2) r2 =  p[1].r;
      else if (n == 3) {
	r2 = (p[1].r + p[2].r + dist(p[1], p[2]))/2;
	r2 >?= max(p[1].r, p[2].r);
      }
      ans <?= max(r1, r2);
    } while (next_permutation(p, p+n));
    printf("Case #%d: %.6f\n", q, ans);
  }
  return 0;
}
