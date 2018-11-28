#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;

int c, d;
int p[200], v[200];

bool moze(long double m) {
  long double lMost = -10e13;
  for (int i=0; i<c; i++) {
    long double left = max(p[i] - m, lMost);
    if (fabsl(left - p[i]) > m) return false;
    long double right = left + (v[i] - 1) * d;
    if (fabsl(right - p[i]) > m) return false;
    lMost = right + d;
  }
  return true;
}

void solve() {
  scanf("%d %d\n", &c, &d);
  for (int i=0; i<c; i++) {
    scanf("%d %d\n", &p[i], &v[i]);
  }
  
  /* z bisekcijo */
  long double a = 0.0L;
  long double b = 6.0e11L;
  
  while (b-a > 10e-8L) {
    long double c = (a + b) / 2.0;
    // printf("[%Lg -- %Lg]\n", a, b);
    if (moze(c)) {
      b = c;
    } else {
      a = c;
    }
    if (a > 1 && (b-a)/a < 10e-8L) break;
  }
  printf("%.12Lg", (a+b) / 2.0L);
}

int main() {
  int t;
  
  scanf("%d\n", &t);
  for (int i=1; i<=t; i++) {
    printf("Case #%d: ", i);
    solve();
    printf("\n");
  }
  return 0;
}
