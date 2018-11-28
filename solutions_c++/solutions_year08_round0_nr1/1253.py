#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
using namespace std;

#define MAXN 1000000000
typedef long long LL;

LL mm[105][1000];
int s, q;
vector<string> engine(105);
vector<string> query(1005);

LL dp(int n1, int n2) {
    LL& ret = mm[n1][n2];
    if (ret != -1) return ret;

    if (engine[n1] == query[n2]) {
        ret = -2;
        return ret;
    }

    if (n2 == q - 1) {
        ret = 0;
        return ret;
    }

    ret = MAXN;
    for (int i = 0; i < s; ++i) {
        LL t = dp(i, n2 + 1);
        if (t == -2) continue;
        if (i != n1) ++t;

        if (t < ret) ret = t;
    }

    if (ret == MAXN) ret = -2;

    return ret;
}

void run() {
    memset(mm, -1, sizeof(mm));

    cin >> s;
    getline(cin, engine[0]);
    for (int i = 0; i < s; ++i) {
        getline(cin, engine[i]);
    }

    cin >> q;
    getline(cin, query[0]);
    for (int i = 0; i < q; ++i) {
        getline(cin, query[i]);
    }

    int ret = MAXN;

    if (q == 0) {
        cout << 0 << endl;
        return;
    }

    for (int i = 0; i < s; ++i) {
        LL t = dp(i, 0);
        if (t == -2) continue;
        if (t < ret) ret = t;
    }

    cout << ret << endl;
}

int main() {
    int kase;
    cin >> kase;
    for (int k = 1; k <= kase; ++k) {
        cout << "Case #" << k << ": ";
        run();
    }
    return 0;
}
