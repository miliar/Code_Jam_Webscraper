#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <algorithm>
#include <bitset>
#include <functional>
#include <iostream>
#include <iterator>
#include <limits>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>

using namespace std;

#include <ext/numeric>
#include <ext/functional>
using namespace __gnu_cxx;

int n, t;
double X;
double S, R;
vector<double> w;
vector<pair<double, double> > b;
vector<pair<double, double> > segment;

void process(int testcase, bool solvecase) {
    cin >> X >> S >> R >> t >> n;
    w.clear(); b.clear();
    for (int i = 0; i < n; ++i)  {
        double x, y; cin >> x >> y; b.push_back(make_pair(x, y));
        double a; cin >> a; w.push_back(a);
    }
    if (solvecase) {
        segment.clear();
        double s = 0;
        for (int i = 0; i < n; ++i) {
            if (b[i].first > s + 1e-5) {
                segment.push_back(make_pair(0, b[i].first - s));
            }
            segment.push_back(make_pair(w[i], b[i].second - b[i].first));
            s = b[i].second;
        }
        if (X > s + 1e-5) {
            segment.push_back(make_pair(0, X - s));
        }
        sort(segment.begin(), segment.end());
        int m = segment.size();
        double left = t;
        for (int i = 0; i < m; ++i) {
            if (left > 1e-12) {
                double run = (segment[i].first + R) * left;
                if (run < segment[i].second - 1e-12){
                    segment.push_back(make_pair(segment[i].first + R, run));
                    segment[i].second -= run;
                    segment[i].first += S;
                    left = 0;
                } else {
                    segment[i].first += R;
                    left -= segment[i].second / segment[i].first;
                }
            } else segment[i].first += S;
        }
        double res = 0;
        for (int i = 0; i < (int)segment.size(); ++i) {
            res += segment[i].second / segment[i].first;
        }
        cout << "Case #" << testcase << ": ";
        cout.precision(15);
        cout << res << endl;
    }
}

void test() {

}

#ifndef EXTERNAL_MAIN
int main() {
    int tc;
    cin >> tc;
    for (int i = 1; i <= tc; ++i)
        process(i, true);
    return 0;
}
#endif