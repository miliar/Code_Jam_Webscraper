#include <cstdio>
#include <cassert>
#include <algorithm>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <stack>
using namespace std;

const int MAXN=1000;
double r[MAXN];
double x[MAXN], y[MAXN];
int p[MAXN];

int main() {
  srand(time(NULL));
  int T;
  scanf("%d", &T);

  for(int tc = 1; tc <= T; ++tc) {
    int N;
    double W, L;
    scanf("%d%lf%lf", &N, &W, &L);
    for(int i = 0; i < N; ++i) {
      scanf("%lf", r + i);
      p[i] = i;
    }

failed:
    fprintf(stderr, "Randomizing\n");
      random_shuffle(p, p + N);

      double base = 0, baseadd = r[p[0]];
      int fb = 0;
      stack<int> S;

      x[p[0]] = 0;
      y[p[0]] = 0;

      for(int i = 1; i < N; ++i) {
//        fprintf(stderr, "Trying to put %d of radius %lf\n", p[i], r[p[i]]);
        double newX;
        if(base == 0)
          newX = x[p[i-1]] + r[p[i]] + r[p[i-1]] + 1e-5;
        else {
          newX = 0;
          while(!S.empty() && r[S.top()] < r[p[i]]) {
            newX = max(newX,x[S.top()] + 2*sqrt(r[S.top()]*r[p[i]]));
            S.pop();
          }
          if(!S.empty())
            newX = max(newX,x[S.top()] + 2*sqrt(r[S.top()]*r[p[i]]));

          newX += 1e-2;
        }
        if(newX > W) {
          base += baseadd + 0.5;
          baseadd = 0;
          fb = i;
          while(!S.empty())
            S.pop();
  //        fprintf(stderr, "New base: %lf\n", base);
          if(base + r[p[i]] > L)
            goto failed;

          x[p[i]] = 0;
          y[p[i]] = base + r[p[i]] + 1e-5;
          assert(pow(x[p[i]] - x[p[0]], 2) + pow(y[p[i]] - y[p[0]], 2) >= pow(r[p[i]] - r[p[0]], 2) - 1e-4);
        }
        else {
          x[p[i]] = newX;
          y[p[i]] = base == 0 ? 0 : base + r[p[i]] + 1e-7;;
        }
    //    fprintf(stderr, "Put %lf %lf\n", x[p[i]], y[p[i]]);
        if(base == 0)
          baseadd = max(baseadd, r[p[i]]);
        else
          baseadd = max(baseadd, 2 * r[p[i]]);
        assert(pow(x[p[i-1]] - x[p[i]], 2) + pow(y[p[i-1]] - y[p[i]], 2) >= pow(r[p[i-1]] + r[p[i]], 2) - 1e-4);
        S.push(p[i]);
        if(y[p[i]] > L)
         goto failed;
      }

    for(int i = 0; i < N; ++i) {
      assert(x[i] >= 0);
      assert(x[i] <= W);
      assert(y[i] >= 0);
      assert(y[i] <= L);
    }

    for(int i = 0; i < N; ++i)
      for(int j = 0; j < N; ++j) {
        if(i == j)
          continue;

      //  printf("Tring %d, %d... (%lf %lf, %lf) (%lf %lf, %lf)\n", i, j, x[i], y[i], r[i], x[j], y[j], r[j]);
        assert(pow(x[i] - x[j], 2) + pow(y[i] - y[j], 2) >= pow(r[i] + r[j], 2));
      }

    printf("Case #%d:", tc);

    for(int i = 0; i < N; ++i)
      printf(" %lf %lf", x[i], y[i]);

    puts("");
  }
}
