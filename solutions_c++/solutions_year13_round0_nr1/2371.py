#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstring>

using namespace std;

typedef long long ll;
typedef long double ldb;

#define forab(i, a, b) for(int i = int(a); i < int(b); ++i)
#define forba(i, b, a) for(int i = int(b) - 1; i >= int(a); --i)
#define forn(i, n) forab(i, 0, n)

int T;
char c[4][4];

string ans;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d ", &T);
    forn(t, T) {
        ans = "Draw";
        forn(i, 4)
            forn(j, 4) {
                cin >> c[i][j];
                if (c[i][j] == '.')
                    ans = "Game has not completed";
            }

        forn(i, 4) {
            int good = 0;
            forn(j, 4) {
                if (c[i][j] == '.') {
                    good = -1;
                    break;
                }
                if (c[i][j] == 'X') {
                    if (good == 2) {
                        good = -1;
                        break;
                    }
                    good = 1;
                }
                if (c[i][j] == 'O') {
                    if (good == 1) {
                        good = -1;
                        break;
                    }
                    good = 2;
                }
            }
            if (good == 1)
                ans = "X won";
            if (good == 2)
                ans = "O won";
        }

        forn(j, 4) {
            int good = 0;
            forn(i, 4) {
                if (c[i][j] == '.') {
                    good = -1;
                    break;
                }
                if (c[i][j] == 'X') {
                    if (good == 2) {
                        good = -1;
                        break;
                    }
                    good = 1;
                }
                if (c[i][j] == 'O') {
                    if (good == 1) {
                        good = -1;
                        break;
                    }
                    good = 2;
                }
            }
            if (good == 1)
                ans = "X won";
            if (good == 2)
                ans = "O won";
        }

        int good = 0;
        forn(i, 4) {
            if (c[i][i] == '.') {
                good = -1;
                break;
            }
            if (c[i][i] == 'X') {
                if (good == 2) {
                    good = -1;
                    break;
                }
                good = 1;
            }
            if (c[i][i] == 'O') {
                if (good == 1) {
                    good = -1;
                    break;
                }
                good = 2;
            }
        }
        if (good == 1)
            ans = "X won";
        if (good == 2)
            ans = "O won";


        good = 0;
        forn(i, 4) {
            if (c[3 - i][i] == '.') {
                good = -1;
                break;
            }
            if (c[3 - i][i] == 'X') {
                if (good == 2) {
                    good = -1;
                    break;
                }
                good = 1;
            }
            if (c[3 - i][i] == 'O') {
                if (good == 1) {
                    good = -1;
                    break;
                }
                good = 2;
            }
        }
        if (good == 1)
            ans = "X won";
        if (good == 2)
            ans = "O won";



        printf("Case #%d: ", t + 1);
        cout << ans << '\n';
    }
    return 0;
}
