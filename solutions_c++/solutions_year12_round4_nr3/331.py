// includes
#include <algorithm>
#include <cassert>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
using namespace std;

// typedefs
typedef long long ll;
typedef long double ld;
typedef complex<double> pt;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;

// macros
#define PRINT0(X) #X << " = " << (X)
#define PRINT1(X1) cout << PRINT0(X1) << endl;
#define PRINT2(X1, X2) cout << PRINT0(X1) << ", " << PRINT0(X2) << endl
#define PRINT3(X1, X2, X3) cout << PRINT0(X1) << ", " << PRINT0(X2) << ", " << PRINT0(X3) << endl
#define PRINT4(X1, X2, X3, X4) cout << PRINT0(X1) << ", " << PRINT0(X2) << ", " << PRINT0(X3) << ", " << PRINT0(X4) << endl
#define PRINTALL(COL) {cout << #COL << " ="; for (auto& printall_curr : (COL)) cout << " " << printall_curr;}

int my_floor(double x) {
    if (x >= 0)
        return int(floor(x) + 0.5);
    return int(floor(x) - 0.5);
}

// main
int main() {
	int num_tests; cin >> num_tests;
	for (int test = 1; test <= num_tests; ++test) {
		cout << "Case #" << test << ":";
        // read input
		int n; cin >> n;
        int hs[n];
        for (int i = 1; i < n; ++i)
            cin >> hs[i];
        int up[n];
        for (int i = 1; i <= n; ++i)
            up[i] = 999999999;
        // go through peaks
        bool can = true;
        int ans[n];
        for (int i = 1; i <= n; ++i)
            ans[i] = -1;
        bool done = false;
        while (!done) {
            for (int i = 1; i < n; ++i) {
                ans[hs[i]] = up[hs[i]];
                // make sure after hs[i] aren't too high
                ans[i] = up[i];
                for (int j = hs[i] + 1; j <= n; ++j) {
                    int b = up[j] - up[hs[i]];
                    int a = j - hs[i];
                    ans[i] = up[i] = min(ans[i], my_floor(up[j] - double(j - i)/a*b - 1e-10));
                }
                // make sure in between i and hs[i] aren't too high
                int b = ans[hs[i]] - ans[i];
                int a = hs[i] - i;
                for (int j = i + 1; j < hs[i]; ++j) {
                    //up[j] = min(up[j], up[i] + my_floor(double(j - i)/a*b - 1e-10));
                    if (up[j] > up[i] + my_floor(double(j - i)/a*b - 1e-10) && ans[j] != -1)
                        can = false;
                    up[j] = min(up[j], up[i] + my_floor(double(j - i)/a*b - 1e-10));
                }
            }
            // check correctness
            done = true;
            if (can) {
                for (int i = 1; i < n; ++i) {
                    double a = hs[i] - i;
                    double b = ans[hs[i]] - ans[i];
                    // check are below
                    for (int j = i + 1; j < hs[i]; ++j) {
                        if (ans[j] >= (j - i)/a*b + ans[i] - 1e-10) {
                            done = false;
                        }
                    }
                    // check are on or below
                    for (int j = hs[i] + 1; j <= n; ++j) {
                        if (ans[j] > (j - i)/a*b + ans[i])
                            done = false;
                    }
                }
            }
        }
        // output answer
        for (int i = 1; i <= n; ++i)
            if (ans[i] < 0)
                can = false;
        if (!can)
            cout << " Impossible";
        else
            for (int i = 1; i <= n; ++i)
                cout << " " << ans[i];
        cout << endl;
    }
}

