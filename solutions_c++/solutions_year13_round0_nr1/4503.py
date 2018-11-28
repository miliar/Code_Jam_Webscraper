#include <cassert>
#include <cctype>
#include <cmath>
#include <climits>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>

#include <algorithm>
#include <deque>
#include <functional>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <utility>
#include <vector>

#include <iostream>
#include <sstream>
#include <fstream>

using namespace std;

const int INF = (int) 1e9 + 5;

typedef long long int64;

template <class T> int len (T a) { return a.size (); }

bool
solve (vector <string> grid, char c) {
    string s (4, c);
    for (int i = 0; i < 4; i++)
        if (grid [i] == s) return true;
    string w = "";
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++)
            w += grid [j][i];
        if (w == s) return true;
        w = "";
    }
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++)
            if (i == j)
                w += grid [i][j];
    if (w == s) return true;
    w = "";
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++)
            if (i + j == 3)
                w += grid [i][j];
    if (w == s) return true;
    return false;

}

int
main () {
    #ifndef ONLINE_JUDGE
        // freopen ("test.in", "r", stdin);
        // freopen ("test.out", "w", stdout);
    #endif
    int T;
    scanf ("%d", &T);
    string s, w;
    for (int t = 1; t <= T; t++) {
        vector <string> grid1;
        vector <string> grid2;
        int cnt = 0;
        for (int i = 0; i < 4; i++) {
            cin >> s;
            cnt += count (s.begin (), s.end (), '.');
            w = s;
            replace (s.begin (), s.end (), 'T', 'O');
            replace (w.begin (), w.end (), 'T', 'X');
            grid1.push_back (s);
            grid2.push_back (w);
        }
        if (solve (grid1, 'O')) printf ("Case #%d: O won\n", t);
        else if (solve (grid2, 'X')) printf ("Case #%d: X won\n", t);
        else if (cnt == 0) printf ("Case #%d: Draw\n", t);
        else printf ("Case #%d: Game has not completed\n", t);
    }

    return 0;
}
