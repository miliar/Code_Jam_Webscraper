#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>
#include <string>

#include <vector>
#include <algorithm>
#include <numeric>
#include <iostream>
#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <list>

#include <cmath>
#include <complex>
using namespace std;

#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define SIZE(t) ((int)((t).size()))
typedef long long LL;
char mat[110][110];
bool vist[110][110];
int dx[] = {1,1,0};
int dy[] = {0,1,1};
int main() {
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int T;
    scanf("%d", &T);
    int bb = 1;
    while (T--) {
        int r, c;
        scanf("%d%d", &r, &c);
        for (int i = 0; i < r; ++i) {
            scanf("%s", mat[i]);
        }
        for (int i = 0; i < r; ++i) {
            for (int j = 0; j < c; ++j) {
                vist[i][j] = false;
            }
        }
        printf("Case #%d:\n", bb++);

        for (int i = 0; i < r; ++i) {
            for (int j = 0; j < c; ++j) {
                if (mat[i][j] == '#' && !vist[i][j]) {
                    vist[i][j] = true;
                    for (int k = 0; k < 3; ++k) {
                        int nexti = dx[k] + i;
                        int nextj = dy[k] + j;
                        if (nexti < 0 || nexti >= r|| nextj < 0 || nextj >=c) {
                            goto l1;
                        }
                        if (mat[nexti][nextj] != '#') {
                            goto l1;
                        } else {
                            vist[i][j] = true;
                        }
                    }
                    mat[i][j] = '/';
                    mat[i][j + 1] = '\\';
                    mat[i + 1][j] = '\\';
                    mat[i + 1][j + 1]= '/';
                }
            }
        }

        for (int i = 0; i < r; ++i) {
            puts(mat[i]);
        }
        continue;
l1:
        puts("Impossible");
    }
    return 0;
}