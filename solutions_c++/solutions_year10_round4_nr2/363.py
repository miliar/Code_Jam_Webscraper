/*
 * Author: Dumbear
 * Created Time:  2010/6/5 22:43:43
 * File Name: 
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;
#define out(v) cerr << #v << ": " << (v) << endl
#define SZ(v) ((int)(v).size())
const int maxint = -1u>>1;
template <class T> bool get_max(T& a, const T &b) {return b > a? a = b, 1: 0;}
template <class T> bool get_min(T& a, const T &b) {return b < a? a = b, 1: 0;}

int t, n, m[1100], p[1100][1100], dp[1100][10][1100];

void solve();
int calc(int s, int t, int c, int r);

int main() {
    freopen("out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i)
        solve();
    return 0;
}

void solve() {
    scanf("%d", &n);
    for (int i = 0; i < (1 << n); ++i)
        scanf("%d", &m[i]);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < (1 << (n - i - 1)); ++j)
            scanf("%d", &p[j * (1 << (i + 1))][(j + 1) * (1 << (i + 1)) - 1]);
    }
    memset(dp, -1, sizeof(dp));
    printf("Case #%d: %d\n", ++t, calc(0, (1 << n) - 1, 0, n - 1));
}

int calc(int s, int t, int c, int r) {
    if (r == -1) {
        return m[s] + c >= n ? 0 : INT_MAX;
    }
    if (dp[s][r][c] != -1)
        return dp[s][r][c];
    int mid = (s + t) / 2;
    dp[s][r][c] = INT_MAX;
    int tmp1 = calc(s, mid, c, r - 1), tmp2 = calc(mid + 1, t, c, r - 1);
    if (tmp1 != INT_MAX && tmp2 != INT_MAX) {
        dp[s][r][c] = tmp1 + tmp2;
    }
    tmp1 = calc(s, mid, c + 1, r - 1);
    tmp2 = calc(mid + 1, t, c + 1, r - 1);
    if (tmp1 != INT_MAX && tmp2 != INT_MAX) {
        dp[s][r][c] = min(dp[s][r][c], tmp1 + tmp2 + p[s][t]);
    }
    return dp[s][r][c];
 }
