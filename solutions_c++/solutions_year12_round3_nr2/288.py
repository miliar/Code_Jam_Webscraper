#include <iostream>
#include <utility>
#include <vector>
#include <set>
#include <map>
#include <deque>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <math.h>

using namespace std;

int T;
double end;
int N;
double pos[2000];
double tm[2000];
int A;
double a[250];

double res[250];

void solve() {
  for (int i=0; i<A; ++i) {
    //    printf("A%d\n",i);

    double x = 0;
    double v = 0;
    double dt, ac;

    for (int c=1; c<N; ++c) {
      dt = tm[c] - tm[c-1];
      ac = 2.0L * (pos[c] - x - v*dt) / (dt*dt);

      //      printf("x:%f->%f t:%f->%f:%f ac:%f ai:%f\n", pos[c-1],pos[c],tm[c-1],tm[c],dt, ac, a[i]);
      if (ac >= a[i]) {
	x += v * dt + a[i] * dt * dt / 2.0L;
        v += a[i] * dt;
	//	printf("not reached:%f %f\n", x, v);
      } else {
	x = pos[c];
        v = (pos[c]-pos[c-1]) / dt;
	//	printf("reached:%f %f\n", x, v);
      }
    }
    double tt = 0.0L;
    if (x < end) {
      double d = v*v + 2*a[i]*(end-x);
      tt = (v + sqrt(d)) / a[i];
      tt = (end-x) * 2.0L / (a[i] * tt);
      //      printf("add %f\n", tt);
    }
    res[i] = tm[N-1] + tt;
  }
}

int main() {
  cin >> T;
  for (int tc=1; tc<=T; ++tc) {
    cin >> end >> N >> A;
    for (int i=0; i<N; ++i) {
      cin >> tm[i] >> pos[i];
      if (pos[i] > end) {
	tm[i] = (end - pos[i-1]) * (tm[i] - tm[i-1]) / (pos[i] - pos[i-1]) + tm[i-1];
	pos[i] = end;
	int ii = i;
	++i;
	while (i<N) {
	  cin >> tm[i] >> pos[i];
	  ++i;
	}
	N = ii+1;
	break;
      }
    }
    for (int i=0; i<A; ++i) {
      cin >> a[i];
    }

    //    for (int i=0; i<N; ++i) {
    //      printf (" %f,%f", tm[i], pos[i]);
    //    }
    //    printf("\n");

    solve();

    printf("Case #%d:\n", tc);
    for (int i=0; i<A; ++i) {
      printf("%.6f\n", res[i]);
    }
  }
  return 0;
}
