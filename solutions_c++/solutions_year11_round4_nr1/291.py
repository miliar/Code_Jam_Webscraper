#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <utility>
#include <vector>
#include <string>
#include <cstring>
#include <set>
#include <map>

const int maxn = 1000;

const double eps = 1e-10;

double b[maxn], e[maxn], w[maxn];
std::vector<std::pair<double, double> > a;



int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    int T;
    
    std::cin >> T;
    for (int ti = 1; ti <= T; ++ti) {
        double x, s, r, t;
        int n;
        std::cin >> x >> s >> r >> t >> n;
        for (int i = 0; i < n; ++i) {
            std::cin >> b[i] >> e[i] >> w[i];
        }
        a.clear();
        if (n == 0) {
            a.push_back(std::make_pair(x, 0));
        } else {
            a.push_back(std::make_pair(b[0], 0));
            for (int i = 0; i < n; ++i) {
                a.push_back(std::make_pair(e[i]-b[i], w[i]));
                if (i+1 < n) {
                    a.push_back(std::make_pair(b[i+1]-e[i], 0));
                } else {
                    if (x > e[i]) {
                        a.push_back(std::make_pair(x-e[i], 0));
                    }
                }
            }
        }
        
        for (int i = 0; i < a.size(); ++i) {
            std::swap(a[i].first, a[i].second);
        }
        std::sort(a.begin(), a.end());
        for (int i = 0; i < a.size(); ++i) {
            std::swap(a[i].first, a[i].second);
        }
        double ans = 0;
        for (int i = 0; i < a.size(); ++i) {
            if (t > 0) {
                if (a[i].first > (r+a[i].second)*t) {
                    a[i].first -= (r+a[i].second)*t;
                    ans += t;
                    t = 0;
                } else if (a[i].first > eps) {
                    t -= a[i].first/(r+a[i].second);
                    ans += a[i].first/(r+a[i].second);
                    a[i].first -= a[i].first;
                }
            }
            if (a[i].first > eps) {
                ans += a[i].first/(s+a[i].second);
            }
        }
        std::printf("Case #%d: %.12lf\n", ti, ans);
    }


    return 0;
}