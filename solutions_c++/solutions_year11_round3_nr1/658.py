#include <vector>
#include <string>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <cstring>
#include <algorithm>
#include <functional>
#include <cstdlib>
#include <cmath>
#include <list>
#include <cctype>

using namespace std;

const int R = 60;
const int C = 60;

char mat[R][C];
int rn, cn;

bool valid(int r, int c)
{
    return mat[r][c] == '#' && mat[r + 1][c] == '#' && mat[r][c + 1] == '#' && mat[r + 1][c + 1] == '#';
}

void cover(int r, int c)
{
    mat[r][c] = '/';
    mat[r + 1][c] = '\\';
    mat[r][c + 1] = '\\';
    mat[r + 1][c + 1] = '/';
}

bool check()
{
    for (int i = 0; i < rn; ++i) {
        for (int j = 0; j < cn; ++j) {
            if (mat[i][j] == '#') {
                if (valid(i, j)) {
                    cover(i, j);
                    return check();
                } else {
                    return false;
                }
            }
        }
    }
    return true;
}

void solve()
{
    int tc;
    scanf("%d", &tc);
    for (int tci = 1; tci <= tc; ++tci) {
        memset(mat, 0, sizeof(mat));
        scanf("%d%d", &rn, &cn);
        for (int i = 0; i < rn; ++i) {
            scanf("%s", mat[i]);
        }
        printf("Case #%d:\n", tci);
        if (check()) {
            for (int i = 0; i < rn; ++i) {
                for (int j = 0; j < cn; ++j) {
                    putchar(mat[i][j]);
                }
                putchar('\n');
            }
        } else {
            puts("Impossible");
        }
    }
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    solve();
    return 0;
}