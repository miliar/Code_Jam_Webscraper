#include <cassert>
#include <climits>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <vector>

using namespace std;


const int MAXN = 105;

static const int dy[4] = { -1, 0, 0, 1 };
static const int dx[4] = { 0, -1, 1, 0 };

int R, S;
int elev[MAXN][MAXN];
char vis[MAXN][MAXN];
char NEXT;

bool ok(int y, int x) {
    return y >= 0 && y < R && x >= 0 && x < S;
}

char dfs(int y, int x) {
    char &ret = vis[y][x];
    if ( ret ) return ret;

    int dir = -1, minelev = INT_MAX;
    for ( int i=0; i<4; ++i ) {
        int ny = y+dy[i], nx = x+dx[i];
        if ( !ok(ny, nx) ) continue;
        if ( elev[ny][nx] >= elev[y][x] ) continue;
        if ( elev[ny][nx] < minelev ) {
            dir = i;
            minelev = elev[ny][nx];
        }
    }
    // fprintf(stderr, "y = %d, x = %d, elev = %d, dir = %d\n", y, x, elev[y][x], dir);

    if ( dir == -1 ) { assert(NEXT <= 'z'); ret = NEXT++; }
    else ret = dfs(y+dy[dir], x+dx[dir]);
    return ret;
}

int main(void) { 
    cin.sync_with_stdio(0);

    int CASES; cin >> CASES;
    for ( int tt=1; tt<=CASES; ++tt ) { // caret here
        cin >> R >> S;
        for ( int y=0; y<R; ++y ) {
            for ( int x=0; x<S; ++x )
                cin >> elev[y][x];
        }

        memset(vis, 0, sizeof vis);
        NEXT = 'a';

        cout << "Case #" << tt << ":\n";
        for ( int y=0; y<R; ++y ) {
            for ( int x=0; x<S; ++x )
                cout << dfs(y, x) << (x+1 < S ? ' ' : '\n');
        }
    }
    return 0;
} 
