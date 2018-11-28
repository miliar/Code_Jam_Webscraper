#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>
#include <map>
#include <set>
#include <cmath>
#include <functional>
#include <sstream>
#include <cassert>
using namespace std;

#pragma comment(linker, "/STACK:56777216")

typedef long long LL;

#define rep(i, n) for (int i = 0; i < n; i++)
#define sz(v) (int) ((v).size())

int getLen(int v) {
    int mod = 1;
    while (mod < v) {
        mod *= 10;
    }
    return mod;
}

void calc(int v, int A, int B, vector< pair<int, int> >& res) {
    int mod = 1, len = getLen(v);

    static int numbers[100];
    int nc = 0;

    while (mod < v) {
        int l = v / mod;
        int r = v % mod;

        if (r * 10 >= mod) {
            int s = r * len + l;
            if (s != v) {
                numbers[nc++] = s;
            }
        }
        mod *= 10;
        len /= 10;
    }

    sort(numbers, numbers + nc);
    nc = unique(numbers, numbers + nc) - numbers;
    rep(i, nc) {
        if (numbers[i] >= A && numbers[i] <= B) {
            if (v < numbers[i])
                res.push_back(make_pair(v, numbers[i]));
            else
                res.push_back(make_pair(numbers[i], v));
        }
    }
}

int main() {
#ifndef ONLINE_JUDGE
//    freopen("../DefaultProject/1.txt", "rb", stdin);
    freopen("../DefaultProject/C-large.in", "rb", stdin);
    freopen("../DefaultProject/C-large.out", "wb", stdout);
#endif

    int T;
    scanf("%d", &T);
    vector< pair<int, int> > res;

    clock_t t = clock();

    rep(tc, T) {
        printf("Case #%d: ", tc + 1);

        int A, B;
        scanf("%d%d", &A, &B);

        res.clear();
        for (int i = A; i <= B; i++) {
            calc(i, A, B, res);
        }

        sort(res.begin(), res.end());
        printf("%d\n", unique(res.begin(), res.end()) - res.begin());

    }

    t = clock() - t;

    //printf("%lf\n", (double) t / CLOCKS_PER_SEC);

    return 0;
}
