#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <set>
using namespace std;
#define SZ(v) ((int)(v).size())
#define REP(i, n) for (int i = 0; i < (n); ++i)
#define REPF(i, a, b) for (int i = (a); i <= (b); ++i)
#define REPD(i, a, b) for (int i = (a); i >= (b); --i)
const int maxint = -1u>>1;

const int n = 4;

char str[n + 2][n + 2];

int check() {
    int cnt0, cnt1;
    for (int i = 0; i < n; ++i) {
        cnt0 = 0, cnt1 = 0;
        for (int j = 0; j < n; ++j) {
            if (str[i][j] == 'X' || str[i][j] == 'T') ++cnt1;
            if (str[i][j] == 'O' || str[i][j] == 'T') ++cnt0;
        }
        if (cnt1 == n) return 1;
        if (cnt0 == n) return 0;
    }
    for (int j = 0; j < n; ++j) {
        cnt0 = 0, cnt1 = 0;
        for (int i = 0; i < n; ++i) {
            if (str[i][j] == 'X' || str[i][j] == 'T') ++cnt1;
            if (str[i][j] == 'O' || str[i][j] == 'T') ++cnt0;
        }
        if (cnt0 == n) return 0;
        if (cnt1 == n) return 1;
    }
    cnt1 = 0, cnt0 = 0;
    for (int i = 0; i < n; ++i) {
        if (str[i][i] == 'X' || str[i][i] == 'T') ++cnt1;
        if (str[i][i] == 'O' || str[i][i] == 'T') ++cnt0;
    }
    if (cnt1 == n) return 1;
    if (cnt0 == n) return 0;
    cnt1 = 0, cnt0 = 0;
    for (int i = 0; i < n; ++i) {
        if (str[i][n - i - 1] == 'X' || str[i][n - i - 1] == 'T') ++cnt1;
        if (str[i][n - i - 1] == 'O' || str[i][n - i - 1] == 'T') ++cnt0;
    }
    if (cnt1 == n) return 1;
    if (cnt0 == n) return 0;
    return -1;
}

bool isFilled() {
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (str[i][j] == '.') return false;
        }
    }
    return true;
}

int main() {
    freopen("a.out", "w", stdout);
    int t, ca = 0;
    scanf("%d", &t);
    while (t--) {
        printf("Case #%d: ", ++ca);
        for (int i = 0; i < n; ++i) {
            scanf("%s", str[i]);
        }
        int res = check();
        if (res == 0) printf("O won\n");
        else if (res == 1) printf("X won\n");
        else if (isFilled()) printf("Draw\n");
        else printf("Game has not completed\n");
    }
    return 0;
}

