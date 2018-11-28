#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <cmath>
#include <cstring>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)n; i++)
#define all(a) a.begin(), a.end()
#define fs first
#define sc second

typedef long long int64;

struct rec
{
  double x, y, r;
};

rec a[100];
int n, t;
double ans;

double r(rec A, rec B)
{
  return ( sqrt((A.x-B.x) * (A.x-B.x) + (A.y-B.y) * (A.y-B.y)) + A.r + B.r) / 2.0;
}



int main()
{
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  
  scanf("%d", &t);

  forn(w, t)
    {
      scanf("%d", &n);

      forn(i, n)
        scanf("%lf%lf%lf", &a[i].x, &a[i].y, &a[i].r);

      ans = 0;
      
      if (n == 1)
        ans = a[0].r;
       else
      if (n == 2)
        ans = max(a[0].r, a[1].r);
       else
      if (n == 3)
        {
          ans = 1000000000;
          ans = min( ans, max(a[2].r, r(a[0], a[1])));
          ans = min( ans, max(a[1].r, r(a[0], a[2])));
          ans = min( ans, max(a[0].r, r(a[1], a[2])));
        }


      printf("Case #%d: %.6lf\n", w+1, ans);
    }
}
