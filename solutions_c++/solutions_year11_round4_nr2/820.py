/*
 * Author: Dumbear
 * Created Time:  2011/6/4 22:41:57
 * File Name: B.cpp
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

int t, n, m, d, mass[512][512], row[512][512], col[512][512];

int get_row(int r, int c1, int c2) {
    if (c1 > c2)
        return 0;
    return row[r][c2] - (c1 == 0 ? 0 : row[r][c1 - 1]);
}

int get_col(int c, int r1, int r2) {
    if (r1 > r2)
        return 0;
    return col[r2][c] - (r1 == 0 ? 0 : col[r1 - 1][c]);
}

void solve();

int main() {
    freopen("out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i)
        solve();
    return 0;
}

void solve() {
    scanf("%d%d%d", &n, &m, &d);
    for (int i = 0; i < n; ++i) {
        char buf[512];
        scanf("%s", buf);
        for (int j = 0; j < m; ++j)
            mass[i][j] = buf[j] - '0';
    }
    for (int i = 0; i < n; ++i) {
        row[i][0] = mass[i][0];
        for (int j = 1; j < m; ++j) {
            row[i][j] = row[i][j - 1] + mass[i][j];
        }
    }
    for (int i = 0; i < m; ++i) {
        col[0][i] = mass[0][i];
        for (int j = 1; j < n; ++j) {
            col[j][i] = col[j - 1][i] + mass[j][i];
        }
    }
    int ans = 1;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            int u = 0, d = 0, l = 0, r = 0;
            for (int k = 1; i - k >= 0 && i + k < n && j - k >= 0 && j + k < m; ++k) {
                //if (i == 3 && j == 3)
                    //printf("-- %d %d %d %d\n", u, d, l, r);
                u += get_row(i - k, j - k, j + k) + get_col(j - k, i - k + 1, i - 1) + get_col(j + k, i - k + 1, i - 1);
                d += get_row(i + k, j - k, j + k) + get_col(j - k, i + 1, i + k - 1) + get_col(j + k, i + 1, i + k - 1);
                l += get_col(j - k, i - k, i + k) + get_row(i - k, j - k + 1, j - 1) + get_row(i + k, j - k + 1, j - 1);
                r += get_col(j + k, i - k, i + k) + get_row(i - k, j + 1, j + k - 1) + get_row(i + k, j + 1, j + k - 1);
                //if (i == 3 && j == 3)
                    //printf("-- %d %d %d %d\n", u, d, l, r);
                if (u - mass[i - k][j - k] - mass[i - k][j + k] == d - mass[i + k][j - k] - mass[i + k][j + k] && l - mass[i - k][j - k] - mass[i + k][j - k] == r - mass[i - k][j + k] - mass[i + k][j + k])
                    ans = max(ans, k * 2 + 1);
            }
        }
    }
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            int u = 0, d = 0, l = 0, r = 0;
            for (int k = 1; i - k >= 0 && i + k <= n && j - k >= 0 && j + k <= m; ++k) {
                //if (i == 3 && j == 3)
                    //printf("-- %d %d %d %d\n", u, d, l, r);
                u += get_row(i - k, j - k, j + k - 1) + get_col(j - k, i - k + 1, i - 1) + get_col(j + k - 1, i - k + 1, i - 1);
                d += get_row(i + k - 1, j - k, j + k - 1) + get_col(j - k, i, i + k - 2) + get_col(j + k - 1, i, i + k - 2);
                l += get_col(j - k, i - k, i + k - 1) + get_row(i - k, j - k + 1, j - 1) + get_row(i + k - 1, j - k + 1, j - 1);
                r += get_col(j + k - 1, i - k, i + k - 1) + get_row(i - k, j, j + k - 2) + get_row(i + k - 1, j, j + k - 2);
                //if (i == 3 && j == 3)
                    //printf("-- %d %d %d %d\n", u, d, l, r);
                if (u - mass[i - k][j - k] - mass[i - k][j + k - 1] == d - mass[i + k - 1][j - k] - mass[i + k - 1][j + k - 1] && l - mass[i - k][j - k] - mass[i + k - 1][j - k] == r - mass[i - k][j + k - 1] - mass[i + k - 1][j + k - 1])
                    ans = max(ans, k * 2);
            }
        }
    }
    if (ans < 3) {
        printf("Case #%d: IMPOSSIBLE\n", ++t);
    } else
        printf("Case #%d: %d\n", ++t, ans);
}
