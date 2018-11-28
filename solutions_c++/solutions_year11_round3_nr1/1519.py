#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <complex>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <climits>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>

using namespace std;

#define ALL(x) x.begin(),x.end()
#define REP(i,n) for (int i=0; i<(n); ++i)
#define FOR(var,start,end) for (int var=(start); var<=(end); ++var)
#define FORD(var,start,end) for (int var=(start); var>=(end); --var)
#define FOREACH(it, X) for(__typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define PB push_back
#define PF push_front
#define MP(a,b) make_pair(a,b)
#define ST first
#define ND second
#define SIZE(x) (int)x.size()

// typedef long long LL;
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<bool> VB;
typedef vector< vector<int> > VVI;
typedef vector< vector<bool> > VVB;

vector<string> field;

bool isBlue(PII coord) {
    if (field[coord.ST][coord.ND] == '#') return true;
    return false;
}

void makeRed(PII coord, char ch) {
    field[coord.ST][coord.ND] = ch;
}

void main2() {
    int nRows, nCols;
    cin >> nRows >> nCols;
    field.clear();
    REP (i, nRows) {
        string s;
        cin >> s;
        field.PB(s);
    }

    REP (i, nRows) {
        REP (j, nCols) {
            vector<PII> coords;
            coords.PB(MP(i, j));
            coords.PB(MP(i, j+1));
            coords.PB(MP(i+1, j));
            coords.PB(MP(i+1, j+1));
            bool blue = true;
            REP (k, SIZE(coords)) {
                PII coord = coords[k];
                int x = coord.ND;
                int y = coord.ST;
                if (0 <= x && x < nCols && 0 <= y && y < nRows) {
                    blue &= isBlue(coord);
                } else {
                    blue = false;
                }
            }
            if (blue) {
                makeRed(coords[0], '/');
                makeRed(coords[1], '\\');
                makeRed(coords[2], '\\');
                makeRed(coords[3], '/');
            }
        }
    }

    bool good = true;
    REP (i, nRows) {
        REP (j, nCols) {
            if (field[i][j] == '#') good = false;
        }
    }

    if (good) {
        REP (i, nRows) {
            cout << field[i] << '\n';
        }
    } else {
        puts("Impossible");
    }
}

int main() {
    int nTests = 0;
    scanf("%d\n", &nTests);

    FOR (test, 1, nTests) {
        printf("Case #%d:\n", test);
        main2();
    }

    return 0;
}
