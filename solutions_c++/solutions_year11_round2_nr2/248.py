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

using namespace std;

#define all(v) (v).begin(), (v).end()

const double PI = 3.1415926535897932384626433832795;
const double EPS = 1e-9;
const int INF = 1000 * 1000;

typedef long long ll;
typedef pair<int, int> pii;



bool isAble(const vector<double>& pos, double time, double dist) {
    double left = -1e15;
    for (int i = 0; i < pos.size(); ++i) {
        double need = left + dist;
        if (need < pos[i] - time) {
            left = pos[i] - time;
        }
        else {
            if (fabs(need - pos[i]) > time) {
                return false;
            }
            left = need;
        }
    }
    return true;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test) {
        cerr << test << endl;
        int c;
        double d;
        cin >> c >> d;
        cerr << "d = " << d << endl;
        vector<double> pos;
        for (int i = 0; i < c; ++i) {
            int amount;
            double p;
            cin >> p >> amount;
            for (int i = 0; i < amount; ++i) {
                pos.push_back(p);
            }
        }
        sort(all(pos));
        int n = pos.size();
        double l = 0, r = 1e15;
        for (int it = 0; it < 100; ++it) {
            double m = (l + r) / 2.0;
            if (isAble(pos, m, d)) {
                r = m;
            }
            else {
                l = m;
            }
        }
        double ans = 2.0 * r;
        ans = (ll)(ans + 0.5);
        double res = ans / 2.0;
        printf("Case #%d: %0.18lf\n", test, res);
    }
	return 0;
}
