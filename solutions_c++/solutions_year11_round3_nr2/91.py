#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

const int MaxN = 1000001;

int n;
long long d[MaxN], a[MaxN];

int L, C;

long long t;



int main() {
  int te; scanf("%d", &te);
  for (int test = 1; test <= te; test++) {
    scanf("%d %lld %d %d", &L, &t, &n, &C);

    for (int i = 0; i < C; i++)
      scanf("%lld", &a[i]);

    long long sum = 0;
    for (int i = 0; i < n; i++) {
      if (sum >= t) d[i] = a[i%C];
      else if (sum + 2 * a[i%C] >= t)
	d[i] = (sum + 2 * a[i%C] - t) / 2;
      else d[i] = 0;

      sum += 2 * a[i%C];
    }

    sort(d, d + n);
    for (int i = 0; i < L; i++) sum -= d[n - 1 - i];

    printf("Case #%d: %lld\n", test, sum);
  }

  return 0;
}


 
