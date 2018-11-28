/*
 * Author: Dumbear
 * Created Time:  2010/6/5 22:25:21
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

int t, n, X, Y, b[512][512], tmp[512][512];

void solve();
bool calc();

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
    memset(b, 0, sizeof(b));
    X = 0;
    Y = 0;
    for (int i = 0; i < n; ++i) {
        int x1, y1, x2, y2;
        scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
        X = max(X, x2);
        Y = max(Y, y2);
        for (int j = x1; j <= x2; ++j)
            for (int k = y1; k <= y2; ++k)
                b[k][j] = 1;
    }
    int cnt = 0;
    while (true) {
        memcpy(tmp, b, sizeof(b));
        if (!calc())
            break;
        ++cnt;
        memcpy(b, tmp, sizeof(tmp));
    }
    printf("Case #%d: %d\n", ++t, cnt);
}

bool calc() {
    bool f = false;
    for (int i = 0; i <= Y; ++i) {
        for (int j = 0; j <= X; ++j) {
            if (b[i][j] == 1) {
                f = true;
                break;
            }
        }
    }
    if (!f)
        return false;
    for (int i = 0; i <= Y; ++i) {
        for (int j = 0; j <= X; ++j) {
            if ((i == 0 || b[i - 1][j] == 0) && (j == 0 || b[i][j - 1] == 0))
                tmp[i][j] = 0;
            else if ((i != 0 && b[i - 1][j] == 1) && (j != 0 && b[i][j - 1] == 1)) {
                tmp[i][j] = 1;
                f = true;
                X = max(X, j);
                Y = max(Y, i);
            }
        }
    }
    return true;
}
