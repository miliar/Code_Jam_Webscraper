#ifdef DEBUG
#define _GLIBCXX_DEBUG
#endif

#include <cstring>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <complex>
#include <ctime>
#include <iomanip>
#include <cmath>
#include <cassert>
#include <queue>
#include <iterator>

typedef long long LL;
typedef long double LD;

using namespace std;

const int MAX_N = 110;

int f [MAX_N][MAX_N];

int main() {
#ifndef LOCAL
//  freopen(".in", "r", stdin);
//  freopen(".out", "w", stdout);
#endif

    int nTests;
    cin >> nTests;

    for (int test = 1; test <= nTests; test++) {
        int n, s, p;
        cin >> n >> s >> p;

        memset(f, 0, sizeof(f));

        for (int i = 0; i < n; i++) {
            int sum;
            cin >> sum;

            vector<int> is(4);
            for (int x = 0; x <= 10; x++)
                for (int y = 0; y <= 10; y++) {
                    int z = sum - x - y;
                    if (z < 0 || z > 10)
                        continue;
                    int d = max(abs(x - y), max(abs(z - x), abs(z - y)));
                    if (d > 2)
                        continue;
                    bool b1 = d == 2;
                    bool b2 = max(x, max(y, z)) >= p;
                    for (int j = b1; j <= s; j++)    
                        f[i + 1][j] = max(f[i + 1][j], f[i][j - b1] + b2);
                }
        }

        cout << "Case #" << test << ": " << f[n][s] << '\n';
    }

    return 0;
}


