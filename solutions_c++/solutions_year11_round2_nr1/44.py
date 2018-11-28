/*
 * Author: Dumbear
 * Created Time:  2011/5/22 0:02:20
 * File Name: A.cpp
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

int t, n;
char s[128][128];
pair<int, int> wp[128];
double owp[128], oowp[128];

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
    scanf("%d", &n);
    for (int i = 0; i < n; ++i)
        scanf("%s", s[i]);
    for (int i = 0; i < n; ++i) {
        int a = 0, b = 0;
        for (int j = 0; j < n; ++j) {
            if (s[i][j] != '.')
                ++b;
            if (s[i][j] == '1')
                ++a;
        }
        wp[i] = make_pair(a, b);
    }
    for (int i = 0; i < n; ++i) {
        owp[i] = 0.0;
        int cnt = 0;
        for (int j = 0; j < n; ++j) {
            if (s[i][j] != '.') {
                owp[i] += (double)(wp[j].first - (s[i][j] == '0' ? 1 : 0)) / (wp[j].second - 1);
                ++cnt;
            }
        }
        owp[i] /= cnt;
    }
    for (int i = 0; i < n; ++i) {
        oowp[i] = 0.0;
        int cnt = 0;
        for (int j = 0; j < n; ++j) {
            if (s[i][j] != '.') {
                oowp[i] += owp[j];
                ++cnt;
            }
        }
        oowp[i] /= cnt;
    }
    printf("Case #%d:\n", ++t);
    for (int i = 0; i < n; ++i)
        //printf("%lf\n", owp[i]);
        printf("%.10lf\n", 0.25 * (double)wp[i].first / wp[i].second + 0.5 * owp[i] + 0.25 * oowp[i]);
}
