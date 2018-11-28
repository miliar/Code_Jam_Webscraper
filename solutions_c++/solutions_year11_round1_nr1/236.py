#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

typedef unsigned long long ullong;

ullong gcd(ullong x, ullong y) {
  if (x < y) swap(x, y);
  while (y > 0) {
    int tmp = x % y;
    x = y;
    y = tmp;
  }
  return x;
}
  

int main() {
  setvbuf(stdin, NULL, _IOFBF, 10000);
  setvbuf(stdout, NULL, _IOFBF, 10000);

  int n_cases;
  scanf("%d", &n_cases);

  for (int ctr = 0; ctr < n_cases; ++ctr) {
    printf("Case #%d: ", ctr+1);
    ullong n = 0;
    int pd = 0;
    int pg = 0;
    scanf("%llu %d %d", &n, &pd, &pg);
    if (pg == 100 && pd < 100 || pg == 0 && pd > 0) {
      printf("Broken\n");
      continue;
    }
    ullong d = gcd(pd, 100);
    if (n < 100/d) {
      printf("Broken\n");
    } else {
      printf("Possible\n");
    }
  }
  
  return 0;
}
