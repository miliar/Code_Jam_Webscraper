#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>

using namespace std;

#define f(i, a, b) for(int i = a; i < b; i++)
#define rep(i, n)  f(i, 0, n)

char s[100][100];

int main(){

    int T; scanf("%d", &T); for(int test = 1; test <= T; test++) {

        printf("Case #%d: ", test);

        int R, C; cin >> R >> C;
        rep(i, R) scanf("%s", s[i]);

        int possible = 1;
        rep(i, R - 1) rep(j, C - 1) {

            if(s[i][j] == '#') {

                s[i][j] = '/';

                int ni, nj;
                ni = i + 1, nj = j;

                if(s[ni][nj] == '#')
                    s[ni][nj] = '\\';
                else {
                    possible = 0;
                    goto end;
                }

                ni = i, nj = j + 1;

                if(s[ni][nj] == '#')
                    s[ni][nj] = '\\';
                else {
                    possible = 0;
                    goto end;
                }

                ni = i + 1, nj = j + 1;

                if(s[ni][nj] == '#')
                    s[ni][nj] = '/';
                else {
                    possible = 0;
                    goto end;
                }

            }
        }

        rep(i, R) rep(j, C)
            if(s[i][j] == '#') {
                possible = 0;
            }

      end:
        cout << endl;
        if(possible)
            rep(i, R) {
                rep(j, C) cout << s[i][j];
                cout << endl;
            }
        else
            cout << "Impossible" << endl;

    }
}
