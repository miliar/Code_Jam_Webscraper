#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <ctime>
#include <cmath>
#include <cassert>
#include <numeric>
#include <algorithm>
using namespace std;

#define N 5
#define M 5200
#define ll long long
#define inf 0x7fffffff
#define lson (id<<1)
#define rson (id<<1|1)

#define eps 1e-6
#define pii pair<int,int>
#define pdd pair<double,int>
#define MP(i,j) make_pair(i,j)
#define It map<int,int>::iterator
#define X first
#define Y second

int n, m;
char ch[N][N];
const char *type[4] = {"X won", "O won", "Draw", "Game has not completed"};

int row(int x, char c) {
    int p = 0;
    for (int j = 0; j < 4; j++) {
        if (ch[x][j] == c)
            p++;
    }
    return p;
}

int column(int x, char c) {
    int p = 0;
    for (int i = 0; i < 4; i++) {
        if (ch[i][x] == c)
            p++;
    }
    return p;
}

int cross_1(char c) {
    int p = 0;
    for (int i = 0; i < 4; i++) {
        if (ch[i][i] == c)
            p++;
    }
    return p;
}

int cross_2(char c) {
    int p = 0;
    for (int i = 0; i < 4; i++) {
        if (ch[i][3 - i] == c)
            p++;
    }
    return p;
}
bool contains(char c) {
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++)
            if (ch[i][j] == c)
                return true;
    }
    return false;
}
int madan() {
    bool xok = false, ook = false;
    for (int i = 0; i < 4; i++) {
        if (row(i, 'X') == 3 && row(i, 'T') == 1)
            xok = true;
        if (row(i, 'O') == 3 && row(i, 'T') == 1)
            ook = true;
        if (row(i, 'X') == 4)
            xok = true;
        if (row(i, 'O') == 4)
            ook = true;
    }
    for (int j = 0; j < 4; j++) {
        if (column(j, 'X') == 3 && column(j, 'T') == 1)
            xok = true;
        if (column(j, 'O') == 3 && column(j, 'T') == 1)
            ook = true;
        if (column(j, 'X') == 4)
            xok = true;
        if (column(j, 'O') == 4)
            ook = true;
    }
    if (cross_1('X') == 3 && cross_1('T') == 1)
        xok = true;
    if (cross_1('O') == 3 && cross_1('T') == 1)
        ook = true;
    if (cross_2('X') == 3 && cross_2('T') == 1)
        xok = true;
    if (cross_2('O') == 3 && cross_2('T') == 1)
        ook = true;

    if (cross_1('X') == 4)
        xok = true;
    if (cross_1('O') == 4)
        ook = true;
    if (cross_2('X') == 4)
        xok = true;
    if (cross_2('O') == 4)
        ook = true;
    //===========================================
    if (xok && !ook)
        return 0;
    if (!xok && ook)
        return 1;
    if (contains('.'))
        return 3;
    else
        return 2;
}

int main() {
#ifndef ONLINE_JUDGE
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    int cas, pcas = 1;
    scanf("%d", &cas);
    while (cas--) {
        for (int i = 0; i < 4; i++)
            scanf("%s", ch[i]);
        printf("Case #%d: %s\n", pcas++, type[madan()]);
    }
    return 0;
}
