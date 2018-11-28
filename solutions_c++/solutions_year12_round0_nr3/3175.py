#include <cstdio>

#include <set>

using namespace std;

inline void rol(int pow, int& x) {
  x = (x / 10) + ((x % 10) * pow);
}

unsigned long long solve() {
  int a, b;

  scanf("%d %d", &a, &b);

  int n = 0;
  int pow = 1;
  int aa = a;
  while (aa > 0) {
    n++;
    pow *= 10;
    aa /= 10;
  }
  pow /= 10;

  unsigned long long s = 0;
  for (int i = a; i <= b; i++) {
    int ii = i;
    set<int> found;
    for (int j = 0; j < n; j++) {
      if (i < ii && ii <= b && found.find(ii) == found.end()) {
        s++;
        found.insert(ii);
      }
      rol(pow, ii);
    }
  }

  return s;
}

int main() {
  int t;

  scanf("%d", &t);
  for (int k = 1; k <= t; k++) {
    printf("Case #%d: %lld\n", k, solve());
  }

  return 0;
}

