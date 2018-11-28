#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <stack>
#include <deque>
#include <algorithm>
#include <cassert>
#include <cmath>
#include <ctime>
#include <cctype>

using namespace std;

#define all(v) (v).begin(), (v).end()

const double PI = 3.1415926535897932384626433832795;
const double EPS = 1e-9;
const int INF = (1 << 31) - 1;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;



double getSquare(double x_min, pdd y_left, double x_max, pdd y_right, double p) {
    double x = p;
    double y_min = y_left.first + (y_right.first - y_left.first) * (x - x_min) / (x_max - x_min);
    double y_max = y_left.second + (y_right.second - y_left.second) * (x - x_min) / (x_max - x_min);
    double dy1 = y_left.second - y_left.first;
    double dy2 = y_max - y_min;
    return (x - x_min) / 2 * (dy1 + dy2);
}


void solveProblem() {
    int w, l, u, G;
    cin >> w >> l >> u >> G;
    vector<pdd> lower(l);
    vector<double> xes;
    for (int i = 0; i < lower.size(); ++i) {
        cin >> lower[i].first >> lower[i].second;
        xes.push_back(lower[i].first);
    }
    vector<pdd> upper(u);
    for (int i = 0; i < upper.size(); ++i) {
        cin >> upper[i].first >> upper[i].second;
        xes.push_back(upper[i].first);    
    }
    sort(all(xes));
    vector<pdd> points(xes.size());
    for (int i = 0; i < points.size(); ++i) {
        double x = xes[i];
        int left = 0;
        for (int j = 0; j + 1 < upper.size(); ++j) {
            if (upper[j + 1].first > x - EPS) {
                left = j;
                break;
            }
        }
        double upper_y = upper[left].second + 
            (upper[left + 1].second - upper[left].second) * (x - upper[left].first) / (upper[left + 1].first - upper[left].first);
        for (int j = 0; j + 1 < lower.size(); ++j) {
            if (lower[j + 1].first > x - EPS) {
                left = j;
                break;
            }
        }
        double lower_y = lower[left].second + 
            (lower[left + 1].second - lower[left].second) * (x - lower[left].first) / (lower[left + 1].first - lower[left].first);
        points[i] = pdd(lower_y, upper_y);
    }
    double total = 0;
    vector<double> square(xes.size() - 1);
    for (int i = 0; i + 1 < xes.size(); ++i) {
        double dx = xes[i + 1] - xes[i];
        double dy_min = points[i].second - points[i].first;
        double dy_max = points[i + 1].second - points[i + 1].first;
        double sq = (dy_max + dy_min) / 2 * dx;
        total += sq;
        square[i] = sq;
        cerr << sq << endl;
    }
    vector<double> res;
    for (int part = 1; part < G; ++part) {
        int left = -1;
        double need = (1.0 * part / G) * total;
        for (int i = 0; i < square.size(); ++i) {
            if (square[i] > need) {
                left = i;
                break;
            }
            else {
                need -= square[i];
            }
        }
        double x_min = xes[left];
        double x_max = xes[left + 1];
        double ll = x_min;
        double rr = x_max;
        pdd y_left = points[left];
        pdd y_right = points[left + 1];
        for (int it = 0; it < 100; ++it) {
            double m = (rr + ll) / 2;
            if (getSquare(x_min, y_left, x_max, y_right, m) > need) {
                rr = m;
            }
            else {
                ll = m;
            }
        }
        res.push_back(ll);
    }
    cout << endl;
    for (int i = 0; i < res.size(); ++i) {
        printf("%0.18lf\n", res[i]);
    }
}


int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test) {
        double t = clock();
        printf("Case #%d: ", test);
        solveProblem();
        t = (clock() - t) / CLOCKS_PER_SEC;
        cerr << test << " time " << t << " s\n";
    }
	return 0;
}
