#include <cstdio>
#include <cstring>

double dist[101];

int main() {
    int T, x, s, r, n, a = 1;
    int b, e, w, l;
    double sum, t;
    scanf("%d", &T);
    while (T--) {
          memset(dist, 0, sizeof(dist));
          scanf("%d %d %d %lf %d", &x, &s, &r, &t, &n);
          l = x;
          for (int i = 0; i < n; i++) {
              scanf("%d %d %d", &b, &e, &w);
              dist[w] += e - b;
              l -= e - b;
          }
          dist[0] = l;
    
          
          sum = 0.0;
          for (int i = 0; i <= 100; i++) {
              if (t >= dist[i] / (r + i)) {
                 t -= dist[i] / (r + i);
                 sum += dist[i] / (r + i);
              } else {
                sum += t;
                dist[i] -= t * (r + i);
                t = 0;
                sum += dist[i] / (s + i);
              }
          }
          
          printf("Case #%d: %.6lf\n", a++, sum);
    }
    return 0;
}
