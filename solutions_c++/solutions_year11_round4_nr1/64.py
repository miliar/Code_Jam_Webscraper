#include <cstdio>
#include <cmath>
#include <string>
#include <iostream>
#include <vector>
#include <sstream>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

int n, tn, nt;

vector <pair <double, double> > v;

int main(void)
{
//   freopen("A-small-attempt0.in", "r", stdin);
//   freopen("A-small-attempt0.out", "w", stdout);
   freopen("A-large.in", "r", stdin);
   freopen("A-large.out", "w", stdout);

   scanf("%d", &nt);
   for (tn=0; tn<nt; tn++)
   {
      fprintf(stderr, "Case #%d: \n", tn+1);

      printf("Case #%d: ", tn+1);

      v.clear();
      double l, v1, v2, t;
      scanf("%lf%lf%lf%lf%d", &l, &v1, &v2, &t, &n);

      for (int i=0; i<n; i++) {
        double x, y, z;
        scanf("%lf%lf%lf", &x, &y, &z);
        l -= y - x;
        v.push_back(make_pair(z + v1, y - x));
      }
      v.push_back(make_pair(v1, l));
      sort(v.begin(), v.end());
      double ans = 0.0;
      for (int i=0; i<n+1; i++) {
        double l = v[i].second;
        double speed = v[i].first;
        double tt = min (l / (speed - v1 + v2), t);
        l -= tt * (speed - v1 + v2);
        t -= tt;
        ans += tt;
        ans += l / speed;
      }

      printf ("%.20lf\n", ans);

   }
   return 0;
}
