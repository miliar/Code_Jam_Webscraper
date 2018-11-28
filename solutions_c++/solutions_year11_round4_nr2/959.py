#include <iostream>
#include <stdio.h>
#include <string.h>
#define M 505

using namespace std;

char map[M][M];
int west[M][M];
int east[M][M];

bool judge1(int x, int y, int ans) {
    int len = ans >> 1;
    int xx = x + len;
    int yy = y + len;

    int tmp = len;
    int toL = tmp * (west[x + ans - 2][y] - west[x][y]);
    tmp --;
    for (int i = y + 1; i < yy; i ++) {
        toL += tmp * (west[x + ans - 1][i] - west[x - 1][i]);
        tmp --;
    }

    tmp = len;
    int toR = tmp * (west[x + ans - 2][y + ans - 1] - west[x][y + ans - 1]);
    tmp --;
    for (int i = y + ans - 2; i > yy; i --) {
        toR += tmp * (west[x + ans - 1][i] - west[x - 1][i]);
        tmp --;
    }

    tmp = len;
    int toU = tmp * (east[x][y + ans - 2] - east[x][y]);
    tmp --;
    for (int i = x + 1; i < xx; i ++) {
        toU += tmp * (east[i][y + ans - 1] - east[i][y - 1]);
        tmp --;
    }

    tmp = len;
    int toD = tmp * (east[x + ans - 1][y + ans - 2] - east[x + ans - 1][y]);
    tmp --;
    for (int i = x + ans - 2; i > xx; i --) {
        toD += tmp * (east[i][y + ans - 1] - east[i][y - 1]);
        tmp --;
    }

    if (toL == toR && toU == toD) {
        return true;
    } else {
        return false;
    }
}

bool judge2(int x, int y, int ans) {
    int len = ans >> 1;
    int xx = x + len;
    int yy = y + len;

    int tmp = len;
    int toL = tmp * (west[x + ans - 2][y] - west[x][y]);
    tmp --;
    for (int i = y + 1; i < yy; i ++) {
        toL += tmp * (west[x + ans - 1][i] - west[x - 1][i]);
        tmp --;
    }

    tmp = len;
    int toR = tmp * (west[x + ans - 2][y + ans - 1] - west[x][y + ans - 1]);
    tmp --;
    for (int i = y + ans - 2; i >= yy; i --) {
        toR += tmp * (west[x + ans - 1][i] - west[x - 1][i]);
        tmp --;
    }

    tmp = len;
    int toU = tmp * (east[x][y + ans - 2] - east[x][y]);
    tmp --;
    for (int i = x + 1; i < xx; i ++) {
        toU += tmp * (east[i][y + ans - 1] - east[i][y - 1]);
        tmp --;
    }

    tmp = len;
    int toD = tmp * (east[x + ans - 1][y + ans - 2] - east[x + ans - 1][y]);
    tmp --;
    for (int i = x + ans - 2; i >= xx; i --) {
        toD += tmp * (east[i][y + ans - 1] - east[i][y - 1]);
        tmp --;
    }

    if (toL == toR && toU == toD) {
        return true;
    } else {
        return false;
    }
}

int doIt(int R, int C) {
    for (int ans = min(R, C); ans >= 3; ans --) {
        for (int x = 1; x + ans - 1 <= R; x ++) {
            for (int y = 1; y + ans - 1 <= C; y ++) {
                if (ans & 1) {
                    if (judge1(x, y, ans)) {
                        return ans;
                    }
                } else {
                    if (judge2(x, y, ans)) {
                        return ans;
                    }
                }
            }
        }
    }
    return -1;
}

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    int T;
    int index = 1;
    scanf ("%d", &T);
    while (T --) {
        int R, C, D;
        scanf ("%d%d%d", &R, &C, &D);
        memset(map, 0, sizeof(map));
        memset(west, 0, sizeof (west));
        memset(east, 0, sizeof (east));
        for (int i = 1; i <= R; i ++) {
            scanf ("%s", &map[i][1]);
        }

        for (int i = 1; i <= R; i ++) {
            for (int j = 1; j <= C; j ++) {
                east[i][j] = east[i][j - 1] + map[i][j] - '0';
                west[i][j] = west[i - 1][j] + map[i][j] - '0';
            }
        }

        int ans = doIt(R, C);

        printf ("Case #%d: ", index ++);
        if (ans == -1) {
            printf ("IMPOSSIBLE\n");
        } else {
            printf ("%d\n", ans);
        }

    }
    return 0;
}
