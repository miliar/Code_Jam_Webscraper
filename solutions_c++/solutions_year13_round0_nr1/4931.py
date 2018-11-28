/*
 * Author:  xioumu
 * Created Time:  2013/4/13 13:02:06
 * File Name: a.cpp
 * solve: a.cpp
 */
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<string>
#include<map>
#include<set>
#include<iostream>
#include<vector>
#include<queue>

using namespace std;
#define sz(v) ((int)(v).size())
#define rep(i, n) for (int i = 0; i < (n); ++i)
#define repf(i, a, b) for (int i = (a); i <= (b); ++i)
#define repd(i, a, b) for (int i = (a); i >= (b); --i)
#define clr(x) memset(x,0,sizeof(x))
#define clrs( x , y ) memset(x,y,sizeof(x))
#define out(x) printf(#x" %d\n", x)
#define sqr(x) ((x) * (x))
typedef long long lint;

const int maxint = -1u>>1;
const double eps = 1e-8;

int sgn(const double &x) {  return (x > eps) - (x < -eps); }
int notC = 0, xw = 0, ow = 0;
char s[10][10];
void gao() {
    rep (i, 4) {
            int nx = 1, no = 1, tn = 0;
            rep (j, 4) {
                if (s[i][j] == 'X') no = 0;
                else if (s[i][j] == 'O') nx = 0;
                else if (s[i][j] == 'T') {
                    tn++;
                    if (tn > 1) {
                        no = nx = 0;
                    }
                }
                else {
                    no = nx = 0;
                    notC = 1;
                }
            }
            if (nx == 1) xw = 1;
            if (no == 1) ow = 1;
        }
    int nx = 1, no = 1, tn = 0;
    int x = 0, y = 0;
    rep (i, 4) {
        if (s[x][y] == 'X') no = 0;
        else if (s[x][y] == 'O') nx = 0;
        else if (s[x][y] == 'T') {
            tn++;
            if (tn > 1) {
                no = nx = 0;
            }
        }
        else {
            no = nx = 0;
        }
        x++, y++;
    }
    if (nx == 1) xw = 1;
    if (no == 1) ow = 1;
}

void zhuan(char s[10][10]) {
    char tmp[10][10];
    rep (i, 4)
        rep (j, 4)
            tmp[j][4 - i - 1] = s[i][j];
    memcpy(s, tmp, sizeof(tmp));
}
int main() {
    freopen("a.out", "w", stdout);
    int T, ca = 1;
    scanf("%d", &T);
    while (T--) {
        rep (i, 4)
            scanf("%s", s[i]);
        notC = xw = ow = 0;
        gao();
        zhuan(s);
        gao();
        printf("Case #%d: ", ca++);
        if (xw == 1) printf("X won\n");
        else if (ow == 1) printf("O won\n");
        else if (notC == 1) printf("Game has not completed\n");
        else printf("Draw\n");
        scanf("\n");
    }
    return 0;
}
