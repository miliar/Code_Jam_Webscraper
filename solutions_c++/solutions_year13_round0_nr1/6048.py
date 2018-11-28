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
#include <cassert>

#define ALL(v) (v).begin(), (v).end()
#define RALL(v) (v).rbegin(), (v).rend()
#define SZ(v) ((int)(v).size())
#define FOR(i, a, b) for (typeof(a) i = (a); i < (b); ++i)
#define FORD(i, a, b) for(typeof(a) i = (a);i >= (b); --i)
#define FOREACH(iter, v) for (typeof((v).begin()) iter = (v).begin(); iter != (v).end(); ++iter)
#define REP(i, n) FOR(i, 0, n)

using namespace std;

#define SMALL 0

bool win(string s, int player)
{
    int p = 0, t = 0;
    char c;
    if (player == 1) c = 'O';
    else c = 'X';
    REP(i,4) {
        if (s[i] == c) ++p;
        else if (s[i] == 'T') ++t;
    }
    return p == 4 || (p == 3 && t == 1);
}

int main()
{

#if SMALL
    freopen("A-small.in", "r", stdin);
    freopen("A-small.out", "w", stdout);
#else
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
#endif

    int n;
    scanf("%d", &n);
    string row[4];
    for (int tc = 1; tc <= n; ++tc) {
        REP(i,4) cin >> row[i];

        string col[4];
        bool full = true;
        REP(i,4) REP(j,4) if (row[i][j] == '.') full = false;
        REP(i,4) REP(j,4) col[i] += row[j][i];
        string diag[2];
        REP(i,4) diag[0] += row[i][i];
        REP(i,4) diag[1] += row[i][3-i];
        bool winner[2] = {false};
        int i;
        for (i = 0; i < 2; ++i) {
            REP(j,4) winner[i] |= win(row[j], i);
            REP(j,4) winner[i] |= win(col[j], i);
            REP(j,2) winner[i] |= win(diag[j], i);
            if (winner[i]) break;
        }
        printf("Case #%d: ", tc);
        if (i == 0) puts("X won");
        else if (i == 1) puts("O won");
        else if (full) puts("Draw");
        else puts("Game has not completed");
    }

	return 0;
}
