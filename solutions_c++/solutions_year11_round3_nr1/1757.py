#include <iostream>
#include <sstream>
#include <cstring>
#include <vector>
#include <stack>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <ctime>
#include <cstdio>
#include <cstdlib>

using namespace std;

#define DPRINT printf
#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)

char red[2][2] = {
    {'/', '\\'},
    {'\\', '/'}
};

int R, C;

int dx[2] = {0, 1};
int dy[2] = {0, 1};

bool replaceTile(int r, int c, char pict[100][100]) {
    REP(i, 2) REP(j, 2) {
        if (r + dy[i] >= R || c + dx[j] >= C) return false;

        if (pict[r + dy[i]][c + dx[j]] == '#') {
            pict[r + dy[i]][c + dx[j]] = red[dy[i]][dx[j]];
        } else {
            return false;
        }
    }
    return true;
}

bool solve(int R, int C, char pict[100][100]) {
    REP(j, R) REP(k, C) {
        if (pict[j][k] == '#') {
            if (!replaceTile(j, k, pict)) return false;
        }
    }
    return true;
}

int main (void) {
    int T;
    cin >> T;
    REP(i, T) {
        cin >> R >> C;
        char pict[100][100];
        REP(j, R) {
            cin >> pict[j];
        }
        if (solve(R, C, pict)) {
            cout << "Case #" << i + 1 << ":" << endl;
            REP(j, R) cout << pict[j] << endl;
        } else {
            cout << "Case #" << i + 1 << ":" << endl;
            cout << "Impossible" << endl;
            //REP(j, R) cout << pict[j] << endl;
        }
    }
    return 0;
}
