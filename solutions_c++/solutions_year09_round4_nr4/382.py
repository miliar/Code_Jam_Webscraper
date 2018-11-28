#include <iostream>
#include <iomanip>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <deque>
#include <stack>
#include <bitset> 
#include <complex>
#include <ctime>
#include <utility>
#include <numeric>
#include <functional>
using namespace std;

#define max2(a,b) (((a) > (b)) ? (a) : (b))
#define min2(a,b) (((a) < (b)) ? (a) : (b))
#define sqr(x) ((x) * (x))
#define debug(x) cout << (#x) << ": " << (x) << endl
#define echo(x) cout << (#x) << endl
#define SZ(x) (int(x.size()))

#define PB push_back
#define MP make_pair
#define FI first
#define SE second

const double eps = 1e-8;
const double pi = acos(-1.0);
const int oo = 0x7f7f7f7f;

typedef long long LL;

struct Coor
{
  double x, y;
  
  Coor () {}
  Coor (double _x, double _y) : x(_x), y(_y) {}
};

int TN, TC;

int N;
Coor dot[40];
double R[40];

double excpt ()
{
  if (N == 1)
    return R[0];
  else if (N == 2)
    return R[0] >? R[1];
  
  double ret = 1e10;
  for (int i = 0; i < 3; ++i)
    for (int j = i + 1; j < 3; ++j)
    {
      double x = (sqrt(sqr(dot[i].x - dot[j].x) + sqr(dot[i].y - dot[j].y)) + R[j] - R[i]) * 0.5;
      double d = x + R[i];
      ret <?= R[3 - i - j] >? d;
    }
  return ret;
}

double solve ()
{
  return 0.0;
}

int main ()
{
  scanf("%d", &TN);
  for (TC = 1; TC <= TN; ++TC)
  {
    scanf("%d", &N);
    for (int i = 0; i < N; ++i)
      scanf("%lf%lf%lf", &dot[i].x, &dot[i].y, &R[i]);
    double ans;
    if (N <= 3)
      ans = excpt();
    else
      ans = solve();
    printf("Case #%d: %.5lf\n", TC, ans);
  }
}
