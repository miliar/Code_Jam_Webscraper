#include <vector>
#include <map>
#include <set>
#include <queue>
#include <bitset>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <string>
#include <cstring>
using namespace std;

#define N 2005
#define D 100000
#define LL long long
#define C0 100
#define E 50000
#define C 10000
#define CC 100

int n;
int h[N];
LL y[N];

bool solve() {
    int cnt = 0;
    y[n] = int(5e8);
    for (int i = n - 1; i >= 1; --i) {
        y[i] = y[i + 1] + (rand() % D - D * 2);
        for (int c0 = 0; c0 < C0; ++c0) {
            bool ok = true;
            for (int j = i + 1; j < h[i]; ++j)
                if ((y[ h[i] ] - y[i]) * (j - i) <= (y[j] - y[i]) * (h[i] - i)) {
                    for (int ci = 0; ci < CC && (y[ h[i] ] - y[i]) * (j - i) <= (y[j] - y[i]) * (h[i] - i); ++ci)
                        --y[j];
                    ok = false;
                }
            for (int j = h[i] + 1; j <= n; ++j)
                if ((y[ h[i] ] - y[i]) * (j - i) < (y[j] - y[i]) * (h[i] - i)) {
                    for (int ci = 0; ci < CC && (y[ h[i] ] - y[i]) * (j - i) < (y[j] - y[i]) * (h[i] - i); ++ci)
                        --y[j];
                    ok = false;
                }
            if (ok) break;
        }
    }
    for (int e = 0; e < E; ++e) {
        bool finish = true;
        for (int i = n - 1; i >= 1; --i) {
            for (int c0 = 0; c0 < C0; ++c0) {
                if (c0 > 0) finish = false;
                bool ok = true;
                for (int j = i + 1; j < h[i]; ++j)
                    if ((y[ h[i] ] - y[i]) * (j - i) <= (y[j] - y[i]) * (h[i] - i)) {
                        for (int ci = 0; ci < CC && (y[ h[i] ] - y[i]) * (j - i) <= (y[j] - y[i]) * (h[i] - i); ++ci)
                            --y[j];
                        ok = false;
                    }
                for (int j = h[i] + 1; j <= n; ++j)
                    if ((y[ h[i] ] - y[i]) * (j - i) < (y[j] - y[i]) * (h[i] - i)) {
                        for (int ci = 0; ci < CC && (y[ h[i] ] - y[i]) * (j - i) < (y[j] - y[i]) * (h[i] - i); ++ci)
                            --y[j];
                        ok = false;
                    }
                if (ok) break;
            }
        }
        if (finish) return true;
    }
    return false;
}

int main() {
    int t, cas = 0;
    scanf("%d", &t);
    while (t--) {
        scanf("%d", &n);
        for (int i = 1; i < n; ++i)
            scanf("%d", &h[i]);
        printf("Case #%d:", ++cas);
        if (!solve())
            puts(" Impossible");
        else {
            for (int i = 1; i <= n; ++i)
                printf(" %lld", y[i]);
            puts("");
        }
    }
    return 0;
}
