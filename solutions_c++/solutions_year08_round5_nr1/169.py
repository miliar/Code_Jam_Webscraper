#include <cstdio>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <iostream>

using namespace std;

#define REP(a, b) for(int a=0; a<(b); a++)
#define FOR(a, b, c) for(int a=(b); a<=(c); a++)
#define FORD(a, b, c) for(int a=(b); a>=(c); a--)
#define ABS(a) ((a)<0 ? -(a) : (a))
#define MP make_pair
#define F first
#define S second

int tab[500][500];

int zx[4] = {1, 0, -1, 0};
int zy[4] = {0, 1, 0, -1};
int Q[600*600];

int main() {
    int zzz;
    scanf("%d", &zzz);
    FOR(zz, 1, zzz) {
        int n;
        scanf("%d", &n);
        memset(tab, 0, sizeof(tab));
        int x = 250, y = 250, pos = 0;
        tab[x][y] = 1;
        REP(i, n) {
            int a; string s;
            cin >> s >> a;
            REP(j, a) REP(k, s.size()) {
                if (s[k]=='F') {
                    x+=zx[pos];
                    y+=zy[pos];
                    tab[x][y] = 1;
                    x+=zx[pos];
                    y+=zy[pos];
                    tab[x][y] = 1;
                } else if (s[k]=='R') pos = (pos+1)%4;
                else if (s[k]=='L') pos = (pos+3)%4;
            }
        }
        REP(i, 500) {
            int akt = -1;
            while (akt<500) {
                int akt2 = akt+1;
                while (akt2<500 && tab[i][akt2]!=1) akt2++;
                if (akt!=-1 && akt2<500)
                    FOR(j, akt+1, akt2-1) tab[i][j] = 2;
                akt = akt2;
            }
        }
        REP(i, 500) {
            int akt = -1;
            while (akt<500) {
                int akt2 = akt+1;
                while (akt2<500 && tab[akt2][i]!=1) akt2++;
                if (akt != -1 && akt2<500)
                    FOR(j, akt+1, akt2-1) tab[j][i] = 2;
                akt = akt2;
            }
        }
        /*FOR(i, 248, 265) {
            FOR(j, 248, 265) printf("%d ", tab[i][j]);
            printf("\n");
        }*/
        int st= 0, en=1;
        Q[0] = 0;
        int ret = 0;
        while(st!=en) {
            int x = Q[st]/500, y = Q[st]%500;
            st++;
            REP(i, 4) if (x+zx[i]>=0 && x+zx[i]<500 && y+zy[i]>=0 && y+zy[i]<500) {
                //printf("%d %d\n", x+zx[i], y+zy[i]);
                if (tab[x+zx[i]][y+zy[i]]!=1) {
                    if (tab[x+zx[i]][y+zy[i]]==2 && (x+zx[i])%2==1 && (y+zy[i])%2==1) ret++;
                    tab[x+zx[i]][y+zy[i]] = 1;
                    Q[en++] = (x+zx[i])*500+y+zy[i];
                }
            }
        }
        /*FOR(i, 248, 265) {
            FOR(j, 248, 265) printf("%d ", tab[i][j]);
            printf("\n");
        }*/
        printf("Case #%d: %d\n", zz, ret);
    }
    return 0;
}
