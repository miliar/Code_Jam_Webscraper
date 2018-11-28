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



int main() {
    freopen("1.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test) {
        int n;
        cin >> n;
        cerr << test << endl;
        vector<string> v(n);
        for (int i = 0; i < n; ++i) {
            cin >> v[i];
        }
        vector<double> wp(n), owp(n), oowp(n);
        for (int team = 0; team < n; ++team) {
            double res = 0;
            int total = 0;
            for (int i = 0; i < n; ++i) {
                if (v[team][i] == '.') {
                    continue;
                }
                else {
                    ++total;
                    if (v[team][i] == '1') {
                        res += 1;
                    }
                }
            }
            wp[team]  = res / total;
        }
        for (int team = 0; team < n; ++team) {
            double res = 0;
            int total = 0;
            for (int i = 0; i < n; ++i) {
                if (v[team][i] == '.') {
                    continue;
                }
                ++total;
                double oponent_res = 0;
                int oponent_total = 0;
                for (int j = 0; j < n; ++j) {
                    if (j == team || v[i][j] == '.') {
                        continue;
                    }
                    else {
                        ++oponent_total;
                        if (v[i][j] == '1') {
                            oponent_res += 1;
                        }
                    }
                }
                oponent_res /= oponent_total;
                res += oponent_res;
            }
            owp[team] = res / total;
        }
        for (int team = 0; team < n; ++team) {
            double res = 0;
            int total = 0;
            for (int i = 0; i < n; ++i) {
                if (v[team][i] != '.') {
                    ++total;
                    res += owp[i];
                }
            }
            oowp[team] = res / total;
        }
        printf("Case #%d:\n", test);
        for (int i = 0; i < n; ++i) {
            double res = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
            printf("%0.18lf\n", res);
        }
    }
	return 0;
}
