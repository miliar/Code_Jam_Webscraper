/*
 * File:   A.cpp
 * Author: yzq110abc
 *
 * Created on 2011年5月22日, 上午12:11
 */

#include <algorithm>
#include <iostream>
#include <utility>
#include <cstring>
#include <cstdio>
#include <string>
#include <vector>
#include <bitset>
#include <queue>
#include <cmath>
#include <map>
#include <set>
#define PB push_back
#define MP make_pair
using namespace std;
typedef pair<int, int> PII;
typedef pair<int, double> PID;
typedef long long LL;

const int MAXN = 110;
int n;
int mat[MAXN][MAXN];
char s[MAXN][MAXN];
double wp[MAXN], owp[MAXN], oowp[MAXN];
int up[MAXN], down[MAXN];

int Solve() {
    memset(wp, 0, sizeof(wp));
    memset(owp, 0, sizeof(owp));
    memset(oowp, 0, sizeof(oowp));
    memset(up, 0, sizeof(up));
    memset(down, 0, sizeof(down));
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%s", s[i]);
        for (int j = 0; j < n; j++) {
            if (s[i][j] == '.') mat[i][j] = -1;
            else if (s[i][j] == '0') mat[i][j] = 0;
            else mat[i][j] = 1;
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (mat[i][j] != -1) ++down[i];
            if (mat[i][j] == 1) ++up[i];
        }
        if (down[i] > 0) wp[i] = up[i] / (double) down[i];
    }
    for (int i = 0; i < n; ++i) {
        int cnt = 0;
        for (int j = 0; j < n; ++j) {
            if (mat[i][j] != -1) {
                ++cnt;
                double tmp = up[j] - mat[j][i];
                if (down[j] - 1 > 0) owp[i] += tmp / (down[j]-1);
            }
        }
        if (cnt > 0) owp[i] /= cnt;
    }
    for (int i = 0; i < n; ++i) {
        int cnt = 0;
        for (int j = 0; j < n; ++j) {
            if (mat[i][j] != -1) {
                ++cnt;
                oowp[i] += owp[j];
            }
        }
        if (cnt > 0) oowp[i] /= cnt;
    }
    for (int i = 0; i < n; ++i) {
        printf("%.12f\n", wp[i] * 0.25 + owp[i] * 0.5 + oowp[i] * 0.25);
//        printf("%.12f\n", owp[i]);
    }
    return 0;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t, cas = 0;
    scanf("%d", &t);
    while (t--) {
        printf("Case #%d:\n", ++cas);
        Solve();
    }
    return 0;
}
