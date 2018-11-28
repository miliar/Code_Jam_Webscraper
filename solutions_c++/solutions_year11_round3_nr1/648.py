/*
 * Author: WHHeV
 * Created Time:  2011/5/22 16:50:13
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

bool flag[55][55];
bool ori[55][55];
int ret[55][55];
char s[55];
int R, C;

inline bool in(int i, int j) {
    if (i >= 0 && i < R && j >= 0 && j < C) {
        if (ori[i][j])
            return true;
        else
            return false;
    }
    return false;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T, tc;
    scanf("%d", &T);
    tc = 1;
    int num;
    while (T--) {
        scanf("%d%d", &R, &C);
        num = 0;
        for (int i = 0; i < R; i++) {
            scanf("%s", s);
            for (int j = 0; j < C; j++)
                if (s[j] == '#') {
                    ori[i][j] = 1;
                    num++;
                }
                else
                    ori[i][j] = 0;
        }
        //printf("<%d>\n", num);
        memset(flag, 0, sizeof(flag));
        memset(ret, 0, sizeof(ret));
        //printf("%d\n", in());
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (ori[i][j] && !flag[i][j]) {
                    if (in(i, j + 1) && in(i + 1, j) && in(i + 1, j + 1)) {
                        //printf("[%d %d]\n", i, j);
                        num -= 4;
                        ret[i][j] = 1;
                        ret[i+1][j] = 2;
                        ret[i][j+1] = 2;
                        ret[i+1][j+1] = 1;
                        flag[i+1][j] = 1;
                        flag[i][j+1] = 1;
                        flag[i+1][j+1] = 1;
                    }
                }
                flag[i][j] = 1;
            }
        }
        printf("Case #%d:\n", tc++);
        if (num > 0)
            printf("Impossible\n");
        else {
            for (int i = 0; i < R; i++) {
                for (int j = 0; j < C; j++) {
                    if (ret[i][j] == 0)
                        printf(".");
                    else if (ret[i][j] == 1)
                        printf("/");
                    else if (ret[i][j] == 2)
                        printf("\\");
                }
                printf("\n");
            }
        }
    }
    return 0;
}

