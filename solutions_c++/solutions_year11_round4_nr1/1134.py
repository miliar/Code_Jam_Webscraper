#include <iostream>
#include <stdio.h>
using namespace std;

int T, nCase;
int X, S, R, N;
double t, tTotal;
struct node {
  int l, w;
}dis[1010];

int cmp(const struct node &a, const struct node &b) {
  if (a.w == b.w) {
    return a.l < b.l;
  }
  return a.w < b.w;
}

int main() {
  FILE *file = freopen("A-large.in", "r", stdin);
  FILE *file2 = freopen("A-large.out", "w", stdout);
  cin >> T;
  nCase = 1;
  while (T--) {
    cin >> X >> S >> R >> t >> N;
    dis[N].l = X;
    for (int i = 0; i < N; i++) {
      int b, e;
      cin >> b >> e >> dis[i].w;
      dis[i].l = e - b;
      dis[N].l -= dis[i].l;
    }
    dis[N++].w = 0;
    sort(dis, dis + N, cmp);
    tTotal = 0;
    for (int i = 0; i < N; i++) {
      if (t >= 1e-12) {
        double tmp = 1.0 * dis[i].l / (dis[i].w + R);
        if (tmp - 1e-12 < t) {
          tTotal += tmp;
          t -= tmp;
        } else {
          tTotal += 1.0 * (dis[i].l - (dis[i].w + R) * t) / 
                    (dis[i].w + S);
          tTotal += t;
          t = 0.0;
        }
      } else {
        tTotal += 1.0 * dis[i].l / (dis[i].w + S);
      }
    }
    cout << "Case #" << nCase++ << ": ";
    printf("%0.9lf\n", tTotal);
  }
}
