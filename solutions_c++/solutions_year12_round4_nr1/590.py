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

const int MAX_N = 10010;

int n, D;
int d [MAX_N], l [MAX_N], f [MAX_N];

int main() {
#ifndef LOCAL
//  freopen(".in", "r", stdin);
//  freopen(".out", "w", stdout);
#endif

    int nTests;
    cin >> nTests;
    for (int test = 1; test <= nTests; test++) {
        cin >> n;
        for (int i = 0; i < n; i++)
            cin >> d[i] >> l[i];
        cin >> D;

        bool ans = false;

        memset(f, 0, sizeof(f));
        f[0] = d[0];
        for (int i = 0; i < n; i++) {
            if (d[i] + f[i] >= D)
                ans = true;
            for (int j = i + 1; j < n; j++)
                if (d[j] <= d[i] + f[i])
                    f[j] = max(f[j], min(l[j], d[j] - d[i]));
        }
#ifdef DEBUG
        for (int i = 0; i < n; i++)
            cerr << f[i] << ' ';
        cerr << '\n';
#endif

        cout << "Case #" << test << ": " << (ans ? "YES" : "NO") << '\n';
    }

    return 0;
}


