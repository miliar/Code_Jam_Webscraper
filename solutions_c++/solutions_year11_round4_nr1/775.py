#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

const int MaxN = 1001;

int n;
double s, r, t, x;

struct E {
  double d, w;
  double a;
  E(double _d, double _w, double _a):d(_d), w(_w), a(_a){}

  friend bool operator<(const E &a, const E &b) {
    return (a.a < b.a);
  }
};

vector<E> a;


int main() {
  int testC; scanf("%d", &testC);
  for (int ttt = 1; ttt <= testC; ttt++) {
    a.clear();

    scanf("%lf %lf %lf %lf %d", &x, &s, &r, &t, &n);
    double ttime = 0.0;
    for (int i = 0; i < n; i++) {
      double b, e, w;
      scanf("%lf %lf %lf", &b, &e, &w);
      a.push_back(E((e-b), w, w));
      x -= (e-b); 
    }
    a.push_back(E(x, 0.0, 0.0));

    sort(a.begin(), a.end());


    for (int i = 0; i < n + 1; i++){
      double d = a[i].d;
      double w = a[i].w;
      //cout << d << " " << w;

      // try to run
      if (d / (r + w) <= t) {
	t -= d / (r + w);
	ttime += d / (r + w);
      }
      else { 
	// run as much as can
	double drest = d - t * (r + w);
	ttime += t; t = 0;
	ttime += drest / (s + w);
      }
      //      cout << " : " << ttime << endl;
    }

    printf("Case #%d: %.6lf\n", ttt, ttime);
  }

  return 0;
}

