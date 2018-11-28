#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <iomanip>
#include <fstream>
#define eps 1e-10
using namespace std;
char list[600][600];

int main() {
        freopen("B-small-attempt4.in", "r", stdin);
        freopen("out4.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; i++) {
        int r, c, d;
        scanf("%d%d%d", &r, &c, &d);
        for (int i = 0; i < r; i++)
            scanf("%s", list[i]);
        int res = 0;
        for (int len = 3; len <= c; len++) {
            for (int i = 0; i <= r - len; i++) {
                for (int j = 0; j <= c - len; j++) {
                    double totalx = 0, totaly = 0;
                    double cx, cy;
                    if (len % 2) {
                        cx = i + len / 2;
                        cy = j + len / 2;
                    } else {
                        cx = i + len / 2 - 0.5;
                        cy = j + len / 2 - 0.5;
                    }
                    for (int x = i; x < i + len; x++) {
                        for (int y = j; y < j + len; y++) {
                            if (!((x == i && y == j) || (x == i + len - 1 && y == j)
                                    || (x == i && y == j + len - 1) || (x == i + len - 1 && y == j + len - 1))) {
                                totalx += (cx - x) * (list[x][y] - '0' + d);
                                totaly += (y - cy) * (list[x][y] - '0' + d);
                            }
                        }
                    }
                    if (fabs(totalx) < eps && fabs(totaly) < eps) res = max(res, len);
//                    int left = 0;
//                    int right = 0;
//                    int up = 0;
//                    int down = 0;
//                    for (int x = i; x < i + len; x++) {
//                        for (int y = j; y < j + len / 2; y++) {
//                            left += list[x][y] - '0';
//                        }
//                        int mid = len / 2;
//                        if (len % 2 == 1) mid++;
//                        for (int y = j + mid; y < j + len; y++) {
//                            right += list[x][y] - '0';
//                        }
//                    }
//                    for (int y = j; y < j + len; y++) {
//                        for (int x = i; x < i + len / 2; x++) {
//                            up += list[x][y] - '0';
//                        }
//                        int mid = len / 2;
//                        if (len % 2 == 1) mid++;
//                        for (int x = i + mid; x < i + len; x++) {
//                            down += list[x][y] - '0';
//                        }
//                    }
//                    left -= list[i][j] - '0';
//                    left -= list[i + len - 1][j] - '0';
//                    right -= list[i][j + len - 1] - '0';
//                    right -= list[i + len - 1][j + len - 1] - '0';
//                    up -= list[i][j] - '0';
//                    up -= list[i][j + len - 1] - '0';
//                    down -= list[i + len - 1][j] - '0';
//                    down -= list[i + len - 1][j + len - 1] - '0';
//                    if (right == left && up == down) res = max(res, len);
                }
            }
        }
        if (res) printf("Case #%d: %d\n", i + 1, res);
        else printf("Case #%d: IMPOSSIBLE\n", i + 1);
    }
    return 0;
}

