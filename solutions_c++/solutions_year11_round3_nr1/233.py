/*
 * Author: momodi
 * Created Time:  2010/5/8 19:00:54
 * File Name: a.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <sstream>
#include <string>
#include <map>
#include <set>
#include <vector>
using namespace std;
#define out(v) cerr << #v << ": " << (v) << endl
#define SZ(v) ((int)(v).size())
const int maxint = -1u>>1;
template <class T> bool get_max(T& a, const T &b) {return b > a? a = b, 1: 0;}
template <class T> bool get_min(T& a, const T &b) {return b < a? a = b, 1: 0;}
#define take(a, b) (((a) >> (b)) & 1)
#define move(v) (1 << (v))

char dts[100][100];
int n, m;
void solve() {
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (dts[i][j] == '#') {
                if (i + 1 < n && j + 1 < m && dts[i + 1][j + 1] == '#' && dts[i + 1][j] == '#' && dts[i][j + 1] == '#') {
                    dts[i][j] = '/';
                    dts[i][j + 1] = '\\';
                    dts[i + 1][j] = '\\';
                    dts[i + 1][j + 1] = '/';
                } else {
                    puts("Impossible");
                    return ;
                }
            }
        }
    }
    for (int i = 0; i < n; ++i) {
        puts(dts[i]);
    }
}

int main() {
    freopen("a.out", "w", stdout);
    int ca;
    scanf("%d", &ca);
    for (int cc = 1; cc <= ca; ++cc) {
        printf("Case #%d:\n", cc);
        scanf("%d %d", &n, &m);
        for (int i = 0; i < n; ++i) {
            scanf("%s", dts[i]);
        }
        solve();
    }
    return 0;
}

