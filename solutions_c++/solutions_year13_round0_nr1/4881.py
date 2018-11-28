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
const int maxint = -1u>>1;
const int n = 4;

char s[n][n + 1];

int work() {
    for (int i = 0; i < n; ++i) {
        int cnt1 = 0, cnt2 = 0;
        for (int j = 0; j < n; ++j) {
            if (s[i][j] == 'X' || s[i][j] == 'T') ++cnt1;
            if (s[i][j] == 'O' || s[i][j] == 'T') ++cnt2;
        }
        if (cnt1 == n) return 1;
        if (cnt2 == n) return -1;
    }
    for (int j = 0; j < n; ++j) {
        int cnt1 = 0, cnt2 = 0;
        for (int i = 0; i < n; ++i) {
            if (s[i][j] == 'X' || s[i][j] == 'T') ++cnt1;
            if (s[i][j] == 'O' || s[i][j] == 'T') ++cnt2;
        }
        if (cnt1 == n) return 1;
        if (cnt2 == n) return -1;
    }
    int cnt1 = 0, cnt2 = 0;
    for (int i = 0; i < n; ++i) {
        if (s[i][i] == 'X' || s[i][i] == 'T') ++cnt1;
        if (s[i][i] == 'O' || s[i][i] == 'T') ++cnt2;
    }
    if (cnt1 == n) return 1;
    if (cnt2 == n) return -1;
    cnt1 = cnt2 = 0;
    for (int i = 0; i < n; ++i) {
        if (s[i][n - 1 - i] == 'X' || s[i][n - 1 - i] == 'T') ++cnt1;
        if (s[i][n - 1 - i] == 'O' || s[i][n - 1 - i] == 'T') ++cnt2;
    }
    if (cnt1 == n) return 1;
    if (cnt2 == n) return -1;
    return 0;
}

bool filled() {
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (s[i][j] == '.') return false;
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
            scanf("%s", s[i]);
        }
        int ans = work();
        if (ans > 0) printf("X won\n");
        else if (ans < 0) printf("O won\n");
        else if (filled()) printf("Draw\n");
        else printf("Game has not completed\n");
    }
    return 0;
}

