#pragma comment(linker, "/STACK:16000000")

#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <list>
#include <bitset>
#include <queue>
#include <stack>
#include <cmath>
#include <valarray>
#include <ctime>
#include <set>
#include <sstream>

using namespace std;

typedef pair<int, int> pi;
typedef long long ull;

#define x first
#define y second
#define mp make_pair

long long f[501][501][3] = {0};


long long getSum(int i1, int j1, int i2, int j2, int k) {
    long long ret = f[i2][j2][k];
    if (i1) {
        ret -= f[i1 - 1][j2][k];
    }
    if (j1) {
        ret -= f[i2][j1 - 1][k];
    }
    if (i1 && j1) {
        ret += f[i1 - 1][j1 - 1][k];
    }
    return ret;
}

void solution() {
    int r, c, d;
    scanf("%d%d%d\n", &r, &c, &d);
    char buf[501] = {0};    
    memset(f, sizeof(f), 0);
    long long tf[501][501] = {0};
    for (int i = 0; i < r; ++i) {
        gets(buf);
        for (int j = 0; j < c; ++j) {
            f[i][j][0] = buf[j] - '0';
            f[i][j][0] += d;
            tf[i][j] = f[i][j][0];
            f[i][j][1] = j * f[i][j][0];
            f[i][j][2] = i * f[i][j][0];
        }
    }
    for (int i = 1; i < r; ++i) {
        for (int k = 0; k < 3; ++k) {
            f[i][0][k] += f[i - 1][0][k];
        }
    }
    for (int j = 1; j < c; ++j) {
        for (int k = 0; k < 3; ++k) {
            f[0][j][k] += f[0][j - 1][k];
        }
    }
    for (int i = 1; i < r; ++i) {
        for (int j = 1; j < c; ++j) {
            for (int k = 0; k < 3; ++k) {
                f[i][j][k] += f[i - 1][j][k] + f[i][j - 1][k] - f[i - 1][j - 1][k];
            }
        }
    }
    int best = 0;
    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            for (int s = 3; i + s - 1< r && j + s - 1 < c; ++s) {
                int cx = j + s / 2;
                int cy = i + s / 2;

                ull scx = getSum(i, j, i + s - 1, j + s - 1, 0);
                scx -= tf[i][j] + tf[i + s - 1][j] + tf[i][j + s - 1] + tf[i + s - 1][j + s - 1];
                ull scy = scx;
                if (s % 2 == 0 && scx % 2 == 1) 
                    continue;
                if (s % 2) {
                    scx *= cx;                
                    scy *= cy;                
                } else {
                    scx *= 2 * cx - 1;
                    scx /= 2;
                    scy *= 2 * cy - 1;                
                    scy /= 2;
                }
                

                ull sx = getSum(i, j, i + s - 1, j + s - 1, 1);
                sx -= tf[i][j] * j + tf[i + s - 1][j] * j + 
                    tf[i][j + s - 1] * (j + s - 1) + tf[i + s - 1][j + s - 1] * (j + s - 1);

                ull sy = getSum(i, j, i + s - 1, j + s - 1, 2);
                sy -= tf[i][j] * i + tf[i + s - 1][j] * (i + s - 1) + 
                    tf[i][j + s - 1] * i + tf[i + s - 1][j + s - 1] * (i + s - 1);

                if (sx == scx && sy == scy) {
                    if (best < s) {
                        best = s;
                    }
                }
            }
        }
    }
    if (!best) {
        printf("IMPOSSIBLE\n");
    } else {
        printf("%d\n", best);
    }
}

int main() {

    //freopen("in.in", "rt", stdin);
    //freopen("out.out", "wt", stdout);

    //freopen("A-small.in", "rt", stdin);
    //freopen("A-small.out", "wt", stdout);

    //freopen("A-large.in", "rt", stdin);
    //freopen("A-large.out", "wt", stdout);

    //freopen("B-small.in", "rt", stdin);
    //freopen("B-small.out", "wt", stdout);

    freopen("B-large.in", "rt", stdin);
    freopen("B-large.out", "wt", stdout);


    //freopen("C-small.in", "rt", stdin);
    //freopen("C-small.out", "wt", stdout);

    //freopen("C-large.in", "rt", stdin);
    //freopen("C-large.out", "wt", stdout);

    int t = 0;
    scanf("%d\n", &t);
    for (int tt = 0; tt < t; tt++) {
        printf("Case #%d: ", tt + 1);
        solution();
    }

    return 0;
}