#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <bitset>
#include <set>
#include <sstream>
#include <stdlib.h>
#include <map>
#include <queue>
#include <assert.h>

using namespace std;

#define sz(x) ((int)x.size())
#define all(x) (x).begin(), (x).end()
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)

#define forit(X,Y) for(typeof((Y).begin()) X = (Y).begin(); X != (Y).end(); ++X)

#define debug(x) cout << '>' << #x << ':' << x << endl;

typedef long long int64;

typedef vector <int> vi;
typedef vector < vi > vvi;

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    
    int testCount;
    cin >> testCount;
    for (int testNumber = 1; testNumber <= testCount; ++testNumber) {
        cerr << "Case #" << testNumber << "..." << endl;

        int W, L, U, G;
        cin >> W >> L >> U >> G;
        vector<pair<int, int> > lower(L);
        for (int i = 0; i < L; ++i) {
            cin >> lower[i].first >> lower[i].second;
        }
        vector<pair<int, int> > upper(U);
        for (int i = 0; i < U; ++i) {
            cin >> upper[i].first >> upper[i].second;
        }

        vector<pair<int, double> > widths;
        {
            int i = 0, j = 0;
            while (i < L || j < U) {
                if (lower[i].first == upper[j].first) {
                    widths.pb(mp(lower[i].first, (double)upper[j].second - lower[i].second));
                    ++i;
                    ++j;
                } else if (lower[i].first < upper[j].first) {
                    double x = lower[i].first;
                    double h1 = upper[j-1].second;
                    double h2 = upper[j].second;
                    double x1 = upper[j-1].first;
                    double x2 = upper[j].first;
                    double h = h1 + (x - x1) * (h2 - h1) / (x2 - x1);
                    widths.pb(mp(lower[i].first, h - lower[i].second));
                    ++i;
                } else if (lower[i].first > upper[j].first) {
                    double x = upper[j].first;
                    double h1 = lower[i-1].second;
                    double h2 = lower[i].second;
                    double x1 = lower[i-1].first;
                    double x2 = lower[i].first;
                    double h = h1 + (x - x1) * (h2 - h1) / (x2 - x1);
                    widths.pb(mp(upper[j].first, upper[j].second - h));
                    ++j;
                }
            }
        }

        vector<pair<int, double> > areas;
        areas.pb(mp(0, 0.0));
        for (int i = 1; i < sz(widths); ++i) {
            double ar = areas.back().second +
                (widths[i].first - widths[i-1].first) * (widths[i-1].second + widths[i].second) / 2;
            areas.pb(mp(widths[i].first, ar));
        }
        double total = areas.back().second;

        vector<double> res;
        int k = 0;
        for (int i = 1; i < G; ++i) {
            double need = total * i / G;
            while (areas[k].second < need) ++k;
            double x0 = areas[k-1].first;
            double x1 = areas[k].first;
            double s0 = areas[k-1].second;
            double s1 = areas[k].second;
            double w0 = widths[k-1].second;
            double w1 = widths[k].second;
            double h = x1 - x0;
            /*double s = need - s0;
            double D = (w0 * w0) + 2 * s * (w1 - w0) / 2 / h;
            double x = x0 + (-w0 + sqrt(D)) / (w1 - w0) * h;*/
            double lo = 0, hi = h;
            double x = lo;
            while (hi > lo + 1e-8) {
                x = (lo + hi) / 2;
                double s = s0 + (w0 + w0 + (w1 - w0) * x / h) / 2 * x;
                if (s < need)
                    lo = x;
                else
                    hi = x;
            }
            x += x0;
            res.pb(x);
        }

        printf("Case #%d:\n", testNumber);
        for (int i = 0; i < sz(res); ++i) {
            printf("%.8lf\n", res[i]);
        }
        //cout << "Case #" << testNumber << ": " << res << endl;
    }

    return 0;
}