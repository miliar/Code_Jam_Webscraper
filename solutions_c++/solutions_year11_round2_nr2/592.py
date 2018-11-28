#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <utility>
#include <math.h>
#include <set>
#include <map>

#define forn(i, n) for(int i = 0; i < n; i++)
#define VI vector<int>
#define PII pair<int, int>
#define fi first
#define se second
#define mp(a, b) make_pair(a, b)
#define pb(a) push_back(a)
#define deb(a); cout << #a << " = " << a << endl;

using namespace std;

const int maxn = 500000;
const long long inf = 10000000000000000LL;
const double eps = 1.0e-7;

int C, D;
PII P[300];

bool prov(double time)
{
//    printf("time = %.9f\n", time);
    double pred = -100000000;
    forn(i, C)
    {
  //      printf("i = %d\n", i);
        double left = P[i].fi  - time;
        double right = P[i].fi + time;
    //    printf("%.9f %.9f\n", left, right);
        if(left < pred + D)
        {
            left = pred + D;
        }
        if(right < pred + D)
        {
      //      printf("!\n");
            return false;
        }

        if(P[i].se > 1 && (right - left) / (P[i].se - 1) < D)
        {
        //    printf("!!\n");
            return false;
        }
        pred = left + (P[i].se - 1)*D;
     //   deb(pred);
    }
    return true;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int n = 0, m, k;
    int t = 0;
    scanf("%d", &t);
    forn(z, t)
    {
        printf("Case #%d: ", z + 1);
        scanf("%d%d", &C, &D);
        forn(i, C)
        {
            scanf("%d%d", &P[i].fi, &P[i].se);
        }
        sort(P, P + n);
        double l = 0;
        double r = 100000000000.0;
        while(r - l > eps)
        {
            double m = (l + r) / 2;
            if(prov(m))
                r = m;
            else
                l = m;
        }
        printf("%.9f\n", l);
    }
    return 0;
}
