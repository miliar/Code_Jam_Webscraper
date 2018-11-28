/* Google Code Jam 2011, Round 1A, Problem A: "FreeCell Statistics". */
/* Fri. May. 20, 2011, By: Samuel Tien-Chieh Huang. */
// Last update: Fri. May. 10, 2011.
#include <cstdio>
#include <map>
using namespace std;

map <int, pair <int, int> > per;

void gen (void) {
  int n, p;
  for (n = 1; n <= 1000; ++ n) {
    for (p = 0; p <= n; ++ p) {
      if (p * 100 % n == 0) {
        int v = p * 100 / n;
        if (per.count (v) == 0) per[v] = make_pair (n, p);
      }
    }
  }
}

bool solve (long long n, long long a, long long b) {
  if ((b == 100) && (a < 100)) return false;
  if ((b == 0) && (a > 0)) return false;
  if (per[a].first > n) return false;
  return true;
}

int main (void) {
  int nc, ca;
  gen ();
  scanf ("%d", &nc);
  for (ca = 1; ca <= nc; ++ ca) {
    long long n, a, b;
    scanf ("%lld%lld%lld", &n, &a, &b);
    printf ("Case #%d: %s\n", ca, solve (n, a, b) ? "Possible" : "Broken");
  }
  return 0;
}
