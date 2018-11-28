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

typedef pair< pair<double, double>, pair<double, double> > def;

bool ls(def a, def b)
{
    if(a.se.fi < b.se.fi)
        return 1;
    return 0;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int n = 0, m, k;
    int test;
    scanf("%d", &test);
    forn(z, test)
    {
        vector< pair <pair<double, double>, pair<double, double> > > P;
        vector< pair <pair<double, double>, pair<double, double> > > P2;
        printf("Case #%d: ", z + 1);
        double X, S, R, T;
        int N;
        cin >> X >> S >> R >> T >> N;
        forn(i, N)
        {
            double x, y, w;
            cin >> x >> y >> w;
            P.pb(mp(mp(x, y), mp(w + S, 0)));
        }

        sort(P.begin(), P.end());

        double pred = 0;
        forn(i, (int)P.size())
        {
            if(fabs(P[i].fi.fi - pred) < eps)
                P2.pb(P[i]);
            else
            {
                P2.pb(mp(mp(pred, P[i].fi.fi), mp(S, 0)));
                P2.pb(P[i]);
            }
            pred = P[i].fi.se;
        }
        if(X - pred > eps)
            P2.pb(mp(mp(pred, X), mp(S, 0)));

        sort(P2.begin(), P2.end(), ls);
            //forn(i, (int)P2.size())
              // printf("[%.9f %.9f %.9f %.9f]\n", P2[i].fi.fi, P2[i].fi.se, P2[i].se.fi, P2[i].se.se);
  //  printf("&&\n");
        double time_run = 0;
        P.clear();
        forn(i, (int)P2.size())
        {
            if(time_run + (P2[i].fi.se - P2[i].fi.fi)/(double)(P2[i].se.fi + R - S) < T + eps)
            {
                P2[i].se.fi += R - S;
                time_run += (P2[i].fi.se - P2[i].fi.fi)/(double)(P2[i].se.fi);
            }
            else
            {
                double temp = (double)(T - time_run)*(P2[i].se.fi + R - S);
                P.pb(mp(mp(P2[i].fi.fi + temp, P2[i].fi.se), mp(P2[i].se.fi, 0)));
                P2[i] = mp(mp(P2[i].fi.fi, P2[i].fi.fi + temp), mp(P2[i].se.fi + R - S, 0));
                time_run = T;
            }
            if(fabs(T - time_run) < eps)
                break;
        }
        P2.insert(P2.end(), P.begin(), P.end());

        sort(P2.begin(), P2.end());

        //forn(i, (int)P2.size())
          //  printf("[%.9f %.9f %.9f %.9f]\n", P2[i].fi.fi, P2[i].fi.se, P2[i].se.fi, P2[i].se.se);
        double ans = 0;
        forn(i, (int)P2.size())
        {
            ans += (P2[i].fi.se - P2[i].fi.fi) / (double)(P2[i].se.fi);
        }
        printf("%.9f\n", ans);
    }
    return 0;
}
