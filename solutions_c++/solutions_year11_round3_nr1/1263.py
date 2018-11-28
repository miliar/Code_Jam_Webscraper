/*
 * File:   main.cpp
 * Author: Young
 *
 * Created on 2011年5月22日, 下午5:14
 */

#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#define PI acos(-1.0)
using namespace std;
#define M 100000
int n, m;
char s[100][100];

bool q() {
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) {
            if (s[i][j] != '#')continue;
            if (s[i][j] == '#' && s[i + 1][j] == '#' && s[i][j + 1] == '#' && s[1 + i][1 + j] == '#') {
                s[i][j] = s[i + 1][j + 1] = '/';
                s[i + 1][j] = s[i][j + 1] = '\\';
            } else return false;
        }
    return true;
}

int main(int argc, char** argv) {
    int cas;
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%d", &cas);
    for (int th = 1; th <= cas; th++) {
        scanf("%d%d%*c", &n, &m);
        for (int i = 0; i <= n; i++)
            for (int j = 0; j <= m; j++)s[i][j] = '.';
        for (int i = 0; i < n; i++)gets(s[i]);
        printf("Case #%d:\n", th);
        if (q()) {
            for (int i = 0; i < n; printf("\n"), i++)
                for (int j = 0; j < m; j++)printf("%c", s[i][j]);
        } else printf("Impossible\n");
    }
    return 0;
}

