/*
 * Author: WHHeV
 * Created Time:  2013/4/13 13:15:40
 * File Name: a.cpp
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

char map[4][10];
int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        memset(map, 0, sizeof(map));
        for (int i = 0; i < 4; ++i)
            scanf("%s", map[i]);
        bool nocom = false, xwin = false, owin = false;
        for (int i = 0; i < 4; ++i) {
            int nx = 0, no = 0, nt = 0;
            for (int j = 0; j < 4; ++j) {
                switch (map[i][j]) {
                    case 'O':
                        ++no; break;
                    case 'X':
                        ++nx; break;
                    case 'T':
                        ++nt; break;
                    case '.':
                        nocom = true; break;
                }
            }
            if (nx + nt == 4) {
                xwin = true;
                break;
            }
            if (no + nt == 4) {
                owin = true;
                break;
            }
        }
        if (xwin) {
            printf("Case #%d: X won\n", t);
            continue;
        }
        if (owin) {
            printf("Case #%d: O won\n", t);
            continue;
        }
        for (int i = 0; i < 4; ++i) {
            int nx = 0, no = 0, nt = 0;
            for (int j = 0; j < 4; ++j) {
                switch (map[j][i]) {
                    case 'O':
                        ++no; break;
                    case 'X':
                        ++nx; break;
                    case 'T':
                        ++nt; break;
                    case '.':
                        nocom = true; break;
                }
            }
            if (nx + nt == 4) {
                xwin = true;
                break;
            }
            if (no + nt == 4) {
                owin = true;
                break;
            }
        }
        if (xwin) {
            printf("Case #%d: X won\n", t);
            continue;
        }
        if (owin) {
            printf("Case #%d: O won\n", t);
            continue;
        }
        int nx = 0, no = 0, nt = 0;
        for (int j = 0; j < 4; ++j) {
            switch (map[j][j]) {
                case 'O':
                    ++no; break;
                case 'X':
                    ++nx; break;
                case 'T':
                    ++nt; break;
                case '.':
                    nocom = true; break;
            }
        }
        if (nx + nt == 4) {
            printf("Case #%d: X won\n", t);
            continue;
        }
        if (no + nt == 4) {
            printf("Case #%d: O won\n", t);
            continue;
        }
        nx = 0, no = 0, nt = 0;
        for (int j = 0; j < 4; ++j) {
            switch (map[j][3-j]) {
                case 'O':
                    ++no; break;
                case 'X':
                    ++nx; break;
                case 'T':
                    ++nt; break;
                case '.':
                    nocom = true; break;
            }
        }
        if (nx + nt == 4) {
            printf("Case #%d: X won\n", t);
            continue;
        }
        if (no + nt == 4) {
            printf("Case #%d: O won\n", t);
            continue;
        }
        if (nocom) {
            printf("Case #%d: Game has not completed\n", t);
            continue;
        } else {
            printf("Case #%d: Draw\n", t);
        }
    }
    return 0;
}

