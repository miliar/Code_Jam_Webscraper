#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>
#include <cstdio>
#include <cassert>
#include <string>
#include <queue>
#include <stack>
#include <deque>
#include <numeric>
#include <sstream>
#include <ctime>

using namespace std;

#define CIN_FILE "input.txt"
#define COUT_FILE "output.txt"

#define forn(i, n) for(int i = 0; i < int(n); i++)
#define for1(i, n) for(int i = 1; i <= int(n); i++)
#define forv(i, v) forn(i, v.size())

#define pb push_back
#define mp make_pair
#define all(v) v.begin(), v.end()

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

#define CMAX 5005

struct Point
{
    int x, y;
    Point() {};
    Point(int x, int y): x(x), y(y) {};
};

int n;
int used[2][CMAX][CMAX];
vector<Point> v, vn;

void solve(int tc)
{
    printf("Case #%d: ", tc);

    cerr << tc << endl;

    cin >> n;

    memset(used, 0, sizeof(used));

    v.clear();

    forn(i, n)
    {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;

        for (int x = x1; x <= x2; x++)
        {
            for (int y = y1; y <= y2; y++)
            {
                if (used[1][x][y] == 0)
                {
                    v.pb(Point(x, y));
                }
                used[1][x][y] = 1;
            }
        }
    }

    int iter = 2;
    for (; !v.empty(); iter++)
    {
        int cr = iter % 2;
        int pr = cr ^ 1;

        vn = v;

        forv(i, v)
        {
            Point p = v[i];

            vn.pb(Point(p.x + 1, p.y));
            vn.pb(Point(p.x, p.y + 1));
        }

        v.clear();

        forv(i, vn)
        {
            Point p = vn[i];

            if (used[pr][p.x][p.y] == iter - 1)
            {
                if (used[pr][p.x - 1][p.y] == iter - 1 || used[pr][p.x][p.y - 1] == iter - 1)
                {
					if (used[cr][p.x][p.y] != iter) v.pb(p);
                    used[cr][p.x][p.y] = iter;
                    
                }
            }
            else
            {                   
                if (used[pr][p.x - 1][p.y] == iter - 1 && used[pr][p.x][p.y - 1] == iter - 1)
                {
					if (used[cr][p.x][p.y] != iter) v.pb(p);
                    used[cr][p.x][p.y] = iter;
                    
                }
            }
        }

    }

    cout << iter - 2 << endl;
}

int main()
{
    freopen(CIN_FILE, "rt", stdin);
    freopen(COUT_FILE, "wt", stdout);
    int tc;
    scanf("%d\n", &tc);
    forn(it, tc) solve(it + 1);
    return 0;
}
            
