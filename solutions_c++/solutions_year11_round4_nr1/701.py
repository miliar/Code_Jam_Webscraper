#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

struct triple {
  int f,s,t;
};

bool operator<(const triple& a, const triple& b) {
  return a.f < b.f;
}

bool cmp(const triple& a, const triple& b) {
  return a.t < b.t;
}

#define eps 1e-9

triple w[2123];
int X, S, R, tt, N;
double t;

double go(int L, int inc, int& p) {
  double ret;
  if (t * (R+inc) >= L) {
    p += L;
    ret = (double)L/(inc+R);
    t -= ret;
  } else {
    p += L;
    ret = t + ((double)L - t*(R+inc)) / (S+inc);
    t = 0.0;
  }
  return ret;
}

int main() {
  int nt, cases = 1;
  scanf(" %d", &nt);
  while (nt--) {
    scanf(" %d%d%d%d%d", &X, &S, &R, &tt, &N);
    t = tt;
    for (int i = 0; i < N; i++)
      scanf(" %d%d%d", &w[i].f, &w[i].s, &w[i].t);
    sort(w, w+N);
    int n = N;
    int p = 0;
    for (int i = 0; i < N; i++) {
      if (p < w[i].f) {
	w[n].f = p;
	w[n].s = w[i].f;
	w[n].t = 0;
	++n;
      }
      p = w[i].s;
    }
    if (p != X) {
	w[n].f = p;
	w[n].s = X;
	w[n].t = 0;
	++n;
    }
    p = 0;
    sort(w, w+n, cmp);
    double res = 0.0;
    for (int i = 0; i < n; i++) {
      // printf("%d %lf\n", p, t);
      // if (p < w[i].f)
      // 	res += go(w[i].f-p, 0, p);
      res += go(w[i].s-w[i].f, w[i].t, p);
    }
    // printf("%d %lf\n", p, t);
    // if (p != X)
    //   res += go((X-p), 0, p);
    printf("Case #%d: %.10lf\n", cases++, res);
  }

  return 0;
}
