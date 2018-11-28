/*
 * Author: momodi
 * Created Time:  2010/5/8 19:37:45
 * File Name: c.cpp
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
int f[510][510];
int M = 100003;

int C[510][501];
int main() {
    for (int i = 0; i <= 500; ++i) {
        for (int j = 0; j <= 500; ++j) {
            if (i < j) {
                continue;
            }
            if (j == 0 || i == j) {
                C[i][j] = 1;
                continue;
            }
            C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % M;
        }
    }
    int max = 500;
    for (int i = 2; i <= max; ++i) {
        f[i][1] = 1;
        for (int j = 1; j < i; ++j) {
            for (int k = j + 1; k <= max; ++k) {
                f[k][i] = (f[k][i] + (long long)f[i][j] * C[k - i - 1][i - j - 1]) % M;
            }
        }
    }
    //out(f[3][2]);
    //freopen("c.out", "w", stdout);
    int ca;
    scanf("%d", &ca);
    for (int cc = 1; cc <= ca; ++cc) {
        printf("Case #%d: ", cc);
        int n;
        scanf("%d", &n);
        int ans = 0;
        for (int i = 1; i < n; ++i) {
            ans = (ans + f[n][i]) % M;
        }
        printf("%d\n", ans);
    }
    return 0;
}

