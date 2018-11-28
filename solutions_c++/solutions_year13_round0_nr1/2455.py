#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <cstring>
#include <string>

using namespace std;

#define rep(i,n) for(int i=0;i<n;i++)
#define re(i,j,n) for(int i=j;i<n;i++)
#define down(i,n) for(int i=n;i>=0;i--)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define pb push_back

#define debug1(x) cout << #x" = " << x << endl;
#define debug2(x, y) cout << #x" = " << x << " " << #y" = " << y << endl;
#define debug3(x, y, z) cout << #x" = " << x << " " << #y" = " << y << " " << #z" = " << z << endl;
#define debug4(x, y, z, w) cout << #x" = " << x << " " << #y" = " << y << " " << #z" = " << z << " " << #w" = " << w << endl;
#define LL long long
#define INF (0x3f3f3f3f)
int T, cas = 0;
char a[4][4];
void out(int ans) {
    cas ++;
    printf("Case #%d: ",cas);
    switch (ans) {
        case 1 : puts("X won"); break;
        case 2 : puts("O won"); break;
        case 3 : puts("Draw"); break;
        case 4 : puts("Game has not completed"); break;
    }
}
int main() {
    cin >> T;
    while (T--) {
        rep(i,4) scanf("%s", a[i]);
        int ans = 0;
        rep(i,4) {
            int t1 = 0, t2 = 0;
            rep(j,4)  {
                if (a[i][j] == 'X' || a[i][j] == '.') t1 = 1;
                if (a[i][j] == 'O' || a[i][j] == '.') t2 = 1;
            }
            if (t1 == 0) {ans = 2;break;}
            if (t2 == 0) {ans = 1;break;}
            t1 = 0; t2 = 0;
            rep(j, 4) {
                if (a[j][i] == 'X' || a[i][j] == '.') t1 = 1;
                if (a[j][i] == 'O' || a[j][i] == '.') t2 = 1;
            }
            if (t1 == 0) {ans = 2;break;}
            if (t2 == 0) {ans = 1;break;}
        }
        if (ans) {
            out(ans);
            continue;
        }
        int t1 = 0, t2 = 0;
        rep(i,4) {
            if (a[i][i] == 'X' || a[i][i] == '.') t1 = 1;
            if (a[i][i] == 'O' || a[i][i] == '.') t2 = 1;
        }
        if (t1 == 0) {ans = 2;}
        if (t2 == 0) {ans = 1;}
        if (ans) {
            out(ans);
            continue;
        }
        t1 = 0, t2 = 0;
        rep(i, 4) {
            if (a[3 - i][i] == 'X' || a[3 - i][i] == '.') t1 = 1;
            if (a[3 - i][i] == 'O' || a[3 - i][i] == '.') t2 = 1;
        }
        if (t1 == 0) {ans = 2;}
        if (t2 == 0) {ans = 1;}
        if (ans) {
            out(ans);
            continue;
        }
        ans = 3;
        rep(i, 4) rep(j, 4) {
            if (a[i][j] == '.') ans = 4;
        }
        out(ans);
    }
	return 0;
}



