#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <ctime>
#include <cmath>
#include <sstream>
#include <fstream>
using namespace std;

vector<vector<int> > vec;

#define eps 1e-9

bool can(int i, int j, int k) {
    int xsum = 0;
    int ysum = 0;
    int total = 0;
    for (int x = 0; x < k; ++x) {
        for (int y = 0; y < k; ++y) {
            if (x==0 || x == k-1) {
                if (y==0 || y==k-1) continue;
            }
            if (y == 0 || y == k-1) {
                if (x==0 || x == k-1) continue;
            }
            xsum += (i + x) * vec[i+x][j+y];
            ysum += (j + y) * vec[i+x][j+y];
            total += vec[i+x][j+y];
        }
    }
    double x_exp = (double)(i + i + k - 1) / 2.0;
    double y_exp = (double)(j + j + k - 1) / 2.0;

    double x_real = (double)xsum / total;
    double y_real = (double)ysum / total;

    double a = fabs(x_exp - x_real);
    if (a > eps) return false;
    double b = fabs(y_exp - y_real);
    if (b > eps) return false;
    return true;
}

void solve(int test) {
    int r,c,d;
    cin >> r >> c >> d;
    vec.resize(r);
    string s;
    for (int i = 0; i < r; ++i) {
        vec[i].resize(c);
        cin >> s;
        for (int j = 0; j < c; ++j) {
            vec[i][j] = d + (int)(s[j] - '0');
        }
    }
    int ret = 0;
    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            for (int k = 3; i + k <= r && j + k <= c; ++k) {
                if (can(i,j,k)) {
                    if (k > ret) ret = k;
                }
            }
        }
    }
    cout << "Case #" << test << ": ";
    if (ret == 0) {
        cout << "IMPOSSIBLE" << endl;
    }
    else {
        cout << ret << endl;
    }
}

int main() {
    int n_tests;
    cin >> n_tests;
    for (int test = 1; test <= n_tests; ++test) {
        solve(test);
    }
    return 0;
}
