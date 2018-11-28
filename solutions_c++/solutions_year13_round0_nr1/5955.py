#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <cstring>
#include <algorithm>
#include <string>
#include <set>
#include <functional>
#include <numeric>
#include <sstream>
#include <stack>
#include <map>
#include <queue>

#define CL(arr, val)    memset(arr, val, sizeof(arr))
#define REP(i, n)       for((i) = 0; (i) < (n); ++(i))
#define FOR(i, l, h)    for((i) = (l); (i) <= (h); ++(i))
#define FORD(i, h, l)   for((i) = (h); (i) >= (l); --(i))
#define L(x)    (x) << 1
#define R(x)    (x) << 1 | 1
#define MID(l, r)   (l + r) >> 1
#define Min(x, y)   (x) < (y) ? (x) : (y)
#define Max(x, y)   (x) < (y) ? (y) : (x)
#define E(x)        (1 << (x))
#define iabs(x)     (x) < 0 ? -(x) : (x)
#define OUT(x)  printf("%lld\n", x)
#define Read()  freopen("data.in", "r", stdin)
#define Write() freopen("data.out", "w", stdout);

typedef long long LL;
const double eps = 1e-6;
const double PI = acos(-1.0);
const int inf = 0x1F1F1F1F;

using namespace std;

char mp[5][5];

int main() {
    freopen("data.in", "r", stdin);
    Write();

    int T, i, j, flag, dot, cas = 0;
    scanf("%d", &T);
    while(T--) {
        dot = 0;
        for(i = 0; i < 4; ++i) {
            scanf("%s", mp[i]);
            for(j = 0; j < 4; ++j) if(mp[i][j] == '.')  dot++;
        }
        int x, o, t;
        flag = -1;
        printf("Case #%d: ", ++cas);
        //row
        for(i = 0; i < 4; ++i) {
            x = t = 0;
            for(j = 0; j < 4; ++j) {
                if(mp[i][j] == 'X') x++;
                if(mp[i][j] == 'T') t++;
            }
            if(x == 4 || (x == 3 && t == 1))    {flag = 0; break;}
            o = t = 0;
            for(j = 0; j < 4; ++j) {
                if(mp[i][j] == 'O') o++;
                if(mp[i][j] == 'T') t++;
            }
            if(o == 4 || (o == 3 && t == 1))    {flag = 1; break;}
        }
        if(flag != -1) {
            if(flag == 0)   puts("X won");
            else    puts("O won");
            continue;
        }
        //column
        for(j = 0; j < 4; ++j) {
            x = t = 0;
            for(i = 0; i < 4; ++i) {
                if(mp[i][j] == 'X') x++;
                if(mp[i][j] == 'T') t++;
            }
            if(x == 4 || (x == 3 && t == 1))    {flag = 0; break;}
            o = t = 0;
            for(i = 0; i < 4; ++i) {
                if(mp[i][j] == 'O') o++;
                if(mp[i][j] == 'T') t++;
            }
            if(o == 4 || (o == 3 && t == 1))    {flag = 1; break;}
        }
        if(flag != -1) {
            if(flag == 0)   puts("X won");
            else    puts("O won");
            continue;
        }
        //diagonal
        x = t = 0;
        for(i = 0; i < 4; ++i) {
            if(mp[i][i] == 'X') x++;
            if(mp[i][i] == 'T') t++;
        }
        if(x == 4 || (x == 3 && t == 1))    {puts("X won"); continue; }

        o = t = 0;
        for(i = 0; i < 4; ++i) {
            if(mp[i][i] == 'O') o++;
            if(mp[i][i] == 'T') t++;
        }
        if(o == 4 || (o == 3 && t == 1))    {puts("O won"); continue; }
        //others
        if(dot == 0)   puts("Draw");
        else    puts("Game has not completed");
    }
    return 0;
}
