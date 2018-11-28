#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

#define VAR(a,b) __typeof(b) a=(b)
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (c).size()

typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<pii> vpii;
typedef vector<vi> vvi;

int grid[50][50];

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w+", stdout);

    int tests;
    cin >> tests;
    REP (test, tests)
    {
        int R, C;
        string s;
        bool ok = true;
        cin >> R >> C;

        REP(i, R)
        {
            cin >> s;
            REP(j, C)
            {
                if (s[j] == '.')
                    grid[i][j] = 0;
                else
                    grid[i][j] = 1;
            }
        }

        REP(i, R)
        {
            if(!ok) break;
            REP(j, C)
            {
                if (grid[i][j] == 1)
                {
                    if ((i+1 < R) && (j+1 < C) && (grid[i+1][j] == 1) && (grid[i][j+1] == 1) && (grid[i+1][j+1] == 1))
                    {
                        grid[i][j] = 2;
                        grid[i+1][j+1] = 2;
                        grid[i+1][j] = 3;
                        grid[i][j+1] = 3;
                        continue;
                    }
                    ok = false;
                    break;
                }
            }
        }

        cout << "Case #" << test + 1 << ":" << endl;
        if(ok)
        {
            REP(i, R)
            {
                REP(j,C)
                {
                    if (grid[i][j] == 0)
                        cout << '.';
                    else if (grid[i][j] == 2)
                        cout << '/';
                    else
                        cout << '\\';
                }
                cout << endl;
            }
        }
        else
            cout << "Impossible" << endl;

    }

    return 0;
}
