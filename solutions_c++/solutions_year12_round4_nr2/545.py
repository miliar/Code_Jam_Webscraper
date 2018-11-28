#include <iostream>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <functional>
#include <complex>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <climits>
#include <cassert>
using namespace std;

#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define SZ(a) ((int)((a).size()))
#define REPSZ(i,v) REP(i,SZ(v))
#define ALL(a) (a).begin(),(a).end()
typedef long long Int;

typedef complex<double> P;
const double PI = acos(-1.0);
const double EPS = 1e-10;

double getRandom() {
  return (double)rand() / RAND_MAX;
}

Int N, W, L;
double r[1024];

P p[1024];

bool check() {
  REP(i, N) {
      REP(j, i) {
          if (abs(p[i] - p[j]) < r[i] + r[j] - EPS)
              return false;
      }
  }
  return true;
}

Int main2() {
  cin >> N >> W >> L;
  REP(i, N) cin >> r[i];

  REP(i, N) {
      p[i].real() = getRandom() * W;
      p[i].imag() = getRandom() * L;
  }
  
  for (;;) {
      REP(i, N) {
          p[i].real() = getRandom() * W;
          p[i].imag() = getRandom() * L;
      }
      if (check())
          break;
  }
  
}

int main() {
  int TNO; scanf("%d\n", &TNO);
  for(int tno = 1; tno <= TNO; tno++) {

      printf("Case #%d: ", tno);
      main2();
      REP(i, N) {
          printf("%.8f ", p[i].real());
          printf("%.8f ", p[i].imag());
      }
      cout << endl;
  }
  return 0;
}

// ./a.exe < B-large.in | tee B-large.res
