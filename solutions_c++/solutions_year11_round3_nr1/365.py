#include<sstream>
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <cctype>
#include <vector>
#include <map>

using namespace std;

#define rep(i,n) for (int i=0;i<(n);i++)
#define foru(i,a,b) for (int i=(a);i<=(b);i++)
#define ford(i,a,b) for (int i=(a);i>=(b);i--)

char mp[100][100];
char sqr[2][2];
int tot[100][100];
int r, c;

void no() {
    puts("Impossible");
}

void solve() {
    sqr[0][0] = '/';
    sqr[0][1] = '\\';
    sqr[1][0] = '\\';
    sqr[1][1] = '/';

    int ok = 1;


    rep(i, r) rep(j, c) tot[i][j] = 0;
    rep(i, r-1) rep(j, c-1) {
        if (mp[i][j] == '#' && mp[i][j+1]=='#' && mp[i+1][j] == '#' && mp[i+1][j+1]=='#') {
            rep(dx, 2) rep(dy, 2) {
                tot[i+dx][j+dy]++;
            }
        }
    }
    int total = 0;
    rep(i, r) rep(j, c) if (mp[i][j] == '#' && tot[i][j] == 0) {
        no();
        return;
    }
    rep(i, r) rep(j, c) if (mp[i][j] == '#') total++;

    if (total % 4) {
        no();
        return;
    }
    while (total > 0) {
        rep(i, r) rep(j, c) tot[i][j] = 0;
        rep(i, r-1) rep(j, c-1) {
            if (mp[i][j] == '#' && mp[i][j+1]=='#' && mp[i+1][j] == '#' && mp[i+1][j+1]=='#') {
                rep(dx, 2) rep(dy, 2) {
                    tot[i+dx][j+dy]++;
                }
            }
        }
        rep(i, r) rep(j, c) if (mp[i][j] == '#' && tot[i][j] == 0) {
            no();
            return;
        }

        int found = 0;
        rep(i, r - 1) rep(j, c - 1) if (mp[i][j] == '#') {
            if (total == 0) break;
            if (found == 0) found = 1;
            if (mp[i][j+1]!='#' || mp[i+1][j]!='#' || mp[i+1][j+1]!='#') continue;
            if (tot[i][j]==1 || tot[i+1][j]==1 || tot[i][j+1]==1 || tot[i+1][j+1]==1) {
                mp[i][j] = sqr[0][0];
                mp[i][j+1] = sqr[0][1];
                mp[i+1][j] = sqr[1][0];
                mp[i+1][j+1] = sqr[1][1];
                total -= 4;
                found = 2;
            }
        }
        if (found == 1) {
            //rep(i, r) { rep(j, c) printf("%c", mp[i][j]); puts(""); }
            no();
            return;
        }
    }
    rep(i, r) {
        rep(j, c) printf("%c", mp[i][j]);
        puts("");
    }

}

int main() {
    int cas;
    scanf("%d", &cas);
    for (int tt = 0; tt < cas; tt++) {
        scanf("%d%d", &r, &c);
        rep(i, r) rep(j, c) scanf(" %c", &mp[i][j]);
        printf("Case #%d:\n", tt + 1);
        solve();
    }
    return 0;
}
