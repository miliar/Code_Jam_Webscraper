#include <cstdio>

int div[101];

int gcd(int a, int b) {
    if (b == 0) return a;
    else return gcd(b, a % b);
}

int main() {
    int t, pd, pg, i, c = 1;
    long long n;
    for (i = 0; i <= 100; i++) {
        div[i] = 100 / gcd(100, i);
        // printf("%d ", div[i]);
    }
    scanf("%d", &t);
    while (t--) {
          scanf("%lld %d %d", &n, &pd, &pg);
          if (n >= div[pd] && !(pd != 100 && pg == 100) && !(pd != 0 && pg == 0))
             printf("Case #%d: Possible\n", c++);
          else
              printf("Case #%d: Broken\n", c++);
    }
    return 0;
}
