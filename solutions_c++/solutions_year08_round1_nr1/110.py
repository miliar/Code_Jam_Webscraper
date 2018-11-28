// comment

#define _CRT_SECURE_NO_DEPRECATE

#include <algorithm>
#include <iostream>
#include <cassert>
#include <vector>

using namespace std;

const int nmax = 100001;

int n;
vector < int > a, b;

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    a.reserve(nmax);
    b.reserve(nmax);

    int testcnt;
    scanf("%d", &testcnt);
    for (int testid = 0; testid < testcnt; ++testid) {
        scanf("%d", &n);
        a.resize(n);
        b.resize(n);
        for (int i = 0; i < n; ++i) scanf("%d", &a[i]);
        for (int i = 0; i < n; ++i) scanf("%d", &b[i]);
        sort(a.begin(), a.end());
        sort(b.rbegin(), b.rend());
        long long res = 0;
        for (int i = 0; i < n; ++i) {
            res += (long long)a[i] * (long long)b[i];
        }
        cout << "Case #" << testid + 1 << ": " << res << endl;
    }

    return 0;
}
