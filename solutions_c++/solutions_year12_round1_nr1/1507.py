#include <iostream>
#include <utility>
#include <set>
#include <vector>
#include <map>
#include <deque>
#include <algorithm>
#include <cstring>
#include <cstdlib>

using namespace std;

int T;
int A, B;
double p[100000];
double pi[100000];

double solve() {
  double result = 9999999.0;
  double r =0.0;
  double pc = 1.0;
  int X = B+1-A;
  double t;

  for (int i=0; i<=A; ++i) {
    pi[i] = 1.0;
    for (int j=0; j<A-i; ++j) {
      pi[i] *= p[j];
    }
    pi[i] *= 1-p[A-i];
  }

  for (int b=0; b<=A; ++b) {
    r = 0.0;
    for (int i=0; i<=b; ++i) {
      r += (X+2*b) * pi[i];
    }
    for (int i=b+1; i<=A; ++i) {
      r += (X+B+1 + 2*b) * pi[i];
    }
    if (r <= result) result = r;
  }

  return min(result, (double)B+2);
}

int main() {
  cin >> T;
  for (int tc=1; tc<=T; ++tc) {
    for (int i=0; i<sizeof(p)/sizeof(p[0]); ++i) p[i] = 0.0;

    cin >> A >> B;

    for (int i=0; i<A; ++i) {
      cin >> p[i];
    }

    printf("Case #%d: %.6f\n", tc, solve());
  }
  return 0;
}
