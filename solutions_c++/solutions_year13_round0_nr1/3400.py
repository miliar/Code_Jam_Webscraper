/*
 * Author: tender
 * Created Time:  2013/4/13 19:09:06
 * File Name: a.cpp
 */
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <map>
#include <queue>
#include <string>
#include <vector>
#include <set>

using namespace std;
const double pi = acos(-1.0);
char g[10][10];
bool check1(const char& ch) {
    for (int i = 0; i < 4; i++) {
        int cnt = 0;
        for (int j = 0; j < 4; j++)
            if (g[i][j] == ch || g[i][j] == 'T') cnt++;
            else break;
        if (cnt == 4) return true;
    }
    for (int j = 0; j < 4; j++) {
        int cnt = 0;
        for (int i = 0; i < 4; i++)
            if (g[i][j] == ch || g[i][j] == 'T') cnt++;
            else break;
        if (cnt == 4) return true;
    }
    int cnt = 0;
    for (int i = 0; i < 4; i++)
        if (g[i][i] == ch || g[i][i] == 'T') cnt++;
        else break;
    if (cnt == 4) return true;
    cnt = 0;
    for (int i = 0; i < 4; i++)
        if (g[i][3 - i] == ch || g[i][3 - i] == 'T') cnt++;
        else break;
    return cnt == 4;
}
bool check2() {
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++)
            if (g[i][j] == '.') return false;
    return true;
}
int main() {
    int cas;
    freopen("A-large.in", "r", stdin);
    freopen("2.txt", "w", stdout);
    scanf("%d", &cas);
    for (int ii = 1; ii <= cas; ii++) {
        printf("Case #%d: ", ii);
        for (int i = 0; i < 4; i++) scanf("%s", g[i]);
        if (check1('X')) printf("X won\n");
        else if (check1('O')) printf("O won\n");
        else if (check2()) printf("Draw\n");
        else printf("Game has not completed\n");
    }
    return 0;
}
