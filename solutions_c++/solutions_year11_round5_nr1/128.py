#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <functional>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
#define point pair<double,double>
#define eps 1e-9
using namespace std;

double area(vector< point > P)
{
    double ans = 0.0;
    for (int i = 0; i + 1 < P.size(); i++) ans += (P[i + 1].second + P[i].second) * (P[i + 1].first - P[i].first)/2.0;
    return ans;
}

double trapezoidArea(vector<point> P,double xcord)
{
    double ans = 0.0;
    for (int i = 0; i + 1 < P.size(); i++)
      if (P[i + 1].first <= xcord) ans += (P[i + 1].second + P[i].second) * (P[i + 1].first - P[i].first)/2.0;
      else
      {
          double ratio = (P[i + 1].second - P[i].second)/(P[i + 1].first - P[i].first);
          double ycord = ratio * (xcord - P[i].first) + P[i].second;
          ans += (ycord + P[i].second) * (xcord - P[i].first)/2.0;
          return ans;
      }
    return ans;
}

int T,W,L,U,n;
vector< point > lower,upper;

int main()
{
    freopen("a.i2","r",stdin);
    freopen("a.o2","w",stdout);

    scanf("%d", &T);
    for (int it = 1; it <= T; it++)
    {
        scanf("%d %d %d %d", &W, &L, &U, &n);
        lower.resize(L);  upper.resize(U);
        for (int i = 0; i < L; i++) scanf("%lf %lf", &lower[i].first, &lower[i].second);
        for (int i = 0; i < U; i++) scanf("%lf %lf", &upper[i].first, &upper[i].second);
        printf("Case #%d:\n", it);

        double piece = (area(upper) - area(lower))/n;
        double leftCut = 0;
        for (int i = 1; i < n; i++)
        {
            double low = leftCut,high = W,ans = low;
            for (int j = 0; j < 70; j++)
            {
                double mid = (low + high)/2;
                double myArea = trapezoidArea(upper,mid) - trapezoidArea(lower,mid) - i * piece;
                if (myArea <= eps)
                {
                    ans = mid;  low = mid;
                }
                else high = mid;
            }
            leftCut = ans;  printf("%.6lf\n", ans);
        }
    }
}
