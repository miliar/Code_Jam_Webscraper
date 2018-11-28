#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <bitset>
#include <map>
#include <queue>
#include <algorithm>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

#define ALL(v) (v).begin(), (v).end()
#define RALL(v) (v).rbegin(), (v).rend()
#define SZ(v) ((int)(v).size())
#define FOR(i, a, b) for (typeof(a) i = (a); i < (b); ++i)
#define FORD(i, a, b) for(typeof(a) i = (a);i >= (b); --i)
#define FOREACH(iter, v) for (typeof((v).begin()) iter = (v).begin(); iter != (v).end(); ++iter)
#define REP(i, n) FOR(i, 0, n)

typedef long long ll;

using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T, R, C;
    string grid[60];
    bool can;
    scanf("%d",&T);
    for (int tc = 1; tc <= T; ++tc) {
        scanf("%d%d",&R, &C);
        REP(i,R) cin >> grid[i];
        can = true;

        REP(i,R) {
            REP(j,C) {
                if (grid[i][j] == '#')
                    if (i + 1 < R && j + 1 < C
                        && grid[i][j+1] == '#' && grid[i+1][j] == '#' && grid[i+1][j+1] == '#') {
                        grid[i][j] = grid[i+1][j+1] = '/';
                        grid[i+1][j] = grid[i][j+1] = '\\';
                    } else {
                        can = false;
                        break;
                    }
            }
            if (!can) break;
        }
        printf("Case #%d:\n",tc);
        if (!can) puts("Impossible");
        else {
            REP(i,R) cout << grid[i] << endl;
        }
    }
    return 0;
}
