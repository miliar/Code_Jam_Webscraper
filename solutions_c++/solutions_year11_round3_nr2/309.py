#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

long long d[1000001];
long long y[1000001];

bool comp(long long a, long long b) { return a > b; }

int main() {
    int e, l, n, c, a = 1, i, j, o;
    long long t, h;
    scanf("%d", &e);
    while (e--) {
          scanf("%d %lld %d %d", &l, &t, &n, &c);
          for (i = 0; i < c; i++) {
              scanf("%d", &d[i]);
              y[i] = d[i];
              if (i) d[i] += d[i - 1];
          }
          for ( ; i < n; i += c) {
              for (j = 0; j < c && i + j < n; j++) {
                  y[i + j] = y[j];
                  d[i + j] = d[i - 1] + d[j];
              }
          }
          o = upper_bound(d, d + n, t >> 1) - d;
          if (o < n) y[o] = d[o] - (t >> 1);
          h = d[n - 1] << 1;
          printf("Case #%d: ", a++);
          
          sort(y + o, y + n, comp);
          
          for (i = o; i < l + o && i < n; i++)
              h -= y[i];
          
          printf("%lld\n", h);
    }
    return 0;
}
