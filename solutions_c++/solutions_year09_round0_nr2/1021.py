/* 
 * File:   B.cpp
 * Author: GongZhi
 * Problem:
 * Created on 2009年9月3日, 下午8:52
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>
using namespace std;

/*
 *
 */
#define mmaxN 110
int n, m;
int data[mmaxN][mmaxN];
char mark[mmaxN][mmaxN];
char now;
int P[4][2] = {
    {-1, 0},
    {0, -1},
    {0, 1},
    {1, 0}
};

char mmax(char a, char b) {
    return a > b ? a : b;
}

char mmin(char a, char b) {
    return a < b ? a : b;
}

void dfs(int x, int y) {
    if (mark[x][y] != 0)return;
    int i;
    int tx, ty;
    int ans = data[x][y];
    for (i = 0; i < 4; i++)
        if (x + P[i][0] >= 0 && x + P[i][0] < n && y + P[i][1] >= 0 && y + P[i][1] < m)
            if (data[x + P[i][0]][y + P[i][1]] < ans) {
                ans = data[x + P[i][0]][y + P[i][1]];
                tx = x + P[i][0];
                ty = y + P[i][1];
            }
    mark[x][y] = now;
    //        printf("%d %d %d\n",x,y,ans);
    if (ans < data[x][y]) {
        dfs(tx, ty);
        mark[x][y] = mark[tx][ty];
    }
    return;
}

int main() {
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int kase;
    int i, j;
    scanf("%d", &kase);
    for (int k = 1; k <= kase; k++) {
        memset(mark, 0, sizeof (mark));
        now = 'a';
        scanf("%d%d", &n, &m);
        for (i = 0; i < n; i++)
            for (j = 0; j < m; j++)scanf("%d", &data[i][j]);
        for (i = 0; i < n; i++)
            for (j = 0; j < m; j++)
                if (mark[i][j] == 0) {
                    dfs(i, j);
                    now = mmax(mark[i][j] + 1, now);
                }
        printf("Case #%d:\n", k);
        for (int ii = 0; ii < n; ii++) {
            for (int jj = 0; jj < m; jj++)printf("%c ", mark[ii][jj]);
            printf("\n");
        }
    }
    return 0;
}

