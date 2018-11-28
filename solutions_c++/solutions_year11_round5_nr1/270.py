#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

long double mix(long double x, vector<pair<int,int> >& points, int ap) {
  pair<int,int> a = points[ap], b = points[ap+1];
  return a.second + 1.0 * (x-a.first) * (b.second-a.second) / (b.first-a.first);
}

int main() {
  int T;
  scanf("%d", &T);
  for(int tid = 1; tid <= T; tid++) {
    int W, L, U, G;
    scanf("%d%d%d%d", &W, &L, &U, &G);

    vector<pair<int,int> > lower(L), upper(U);
    for(int i = 0; i < L; i++)
      scanf("%d%d", &lower[i].first, &lower[i].second);
    for(int i = 0; i < U; i++)
      scanf("%d%d", &upper[i].first, &upper[i].second);

    vector<long double> areas(W+1, 0);
    int lp = 0, up = 0;
    for(int x = 1; x <= W; x++) {
      long double x1 = x-1, x2 = x;
      long double low_y1 = mix(x1, lower, lp), low_y2 = mix(x2, lower, lp);
      long double upp_y1 = mix(x1, upper, up), upp_y2 = mix(x2, upper, up);
//      printf("x=%d: low_y1=%lf low_y2=%lf upp_y1=%lf upp_y2=%lf\n", x, low_y1, low_y2, upp_y1, upp_y2);
      areas[x] = areas[x-1] + (upp_y1 + upp_y2) / 2 - (low_y1 + low_y2) / 2;
      if(lp < L && lower[lp+1].first == x) lp++;
      if(up < U && upper[up+1].first == x) up++;
//      printf("areas[%d] = %lf\n", x, areas[x]);
    }
    printf("Case #%d:\n", tid);
    for(int g = 1; g < G; g++) {
      long double target = areas[W] / G * g;
      int x = 0;
      for(x = 0; x < W && areas[x+1] < target; x++)
        ;
      int lp = 0, up = 0;
      while(lp < L && lower[lp+1].first <= x) lp++;
      while(up < U && upper[up+1].first <= x) up++;
      long double low_y1 = mix(x, lower, lp);
      long double upp_y1 = mix(x, upper, up);
      long double bmin = 0, bmax = 1;
      for(int i = 0; i < 10000; i++) {
        long double mid = (bmin+bmax)/2;
        long double low_y2 = mix(x+mid, lower, lp);
        long double upp_y2 = mix(x+mid, upper, up);
//        if(i < 10) printf("x=%lf: low_y1=%lf low_y2=%lf upp_y1=%lf upp_y2=%lf\n", x+mid, low_y1, low_y2, upp_y1, upp_y2);
        long double result = areas[x] + mid * ((upp_y1 + upp_y2) / 2 - (low_y1 + low_y2) / 2);
//        if(i < 10) printf("result = %lf, target = %lf\n", result, target);
        if(result < target)
          bmin = mid;
        else
          bmax = mid;
      }
//      printf("bmin = %lf, bmax = %lf\n", bmin, bmax);
      printf("%.8Lf\n", x+(bmin+bmax)/2);
    }
  }
  return 0;
}

