/*
 * Author: Xay
 * Created Time:  2011/5/22 17:04:15
 * File Name: a.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
using namespace std;
#define SZ(v) ((int)(v).size())
const int maxint = -1u>>1;

const int maxn = 50 + 5;
char s[maxn][maxn];
int r, c;

bool can_replace(int x, int y) {
    if (x + 1 >= r || y + 1 >= c) {
        return false;
    }
    for (int i = 0; i < 2; ++i) {
        for (int j = 0; j < 2; ++j) {
            if (s[x + i][y + j] != '#') {
                return false;
            }
        }
    }
    return true;
}

bool trans(int r, int c) {
    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            if (s[i][j] == '#') {
                if (!can_replace(i, j)) {
                    return false;
                }
                s[i][j] = s[i + 1][j + 1] = '/';
                s[i + 1][j] = s[i][j + 1] = '\\';
            }
        }
    }
    return true;
}
int main() {
    freopen("a.out", "w", stdout);
    int t, ca = 0;
    scanf("%d", &t);
    while (t--) {
        printf("Case #%d:\n", ++ca);
        scanf("%d%d", &r, &c);
        for (int i = 0; i < r; ++i) {
            scanf("%s", s[i]);
        }
        bool flag = trans(r, c);
        if (!flag) {
            printf("Impossible\n");
        } else {
            for (int i = 0; i < r; ++i) {
                printf("%s\n", s[i]);
            }
        }
    }
    return 0;
}

