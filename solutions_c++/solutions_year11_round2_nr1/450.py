#include <cstdio>
#include <cstring>
#include <string>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <utility>
#include <map>
#include <queue>
#include <vector>
#include <cstdlib>
#include <iostream>
#include <iomanip>
#define MAXN (1 << 7)
#define INF
#define x first
#define y second
using namespace std;
#warning use cin/cout or %I64d for long integers

int n;
char grid[MAXN][MAXN];

double wp[MAXN], wns[MAXN], ttl[MAXN];
double op[MAXN];
double oop[MAXN];


inline void solve()
{
    for (int i=0; i < n; ++i)
    {
        double total = 0., wins = 0.;
        for (int j=0; j < n; ++j)
        {
            if (grid[i][j] != '.') total += 1.;
            if (grid[i][j] == '1') wins += 1.;
        }
        wns[i] = wins;
        ttl[i] = total;
        wp[i] = wins / total;
    }

    for (int i=0; i < n; ++i)
    {
        double total = 0., sum = 0.;
        for (int j=0; j < n; ++j)
        {
            if (grid[i][j] == '.') continue;
            total += 1.;
            double cur = wns[j];
            if (grid[i][j] == '0') cur -= 1.;
            cur /= (ttl[j] - 1.);
            sum += cur;
        }

        op[i] = sum/total;
    }

    for (int i=0; i < n; ++i)
    {
        double total = 0., sum = 0.;
        for (int j=0; j < n; ++j)
        {
            if (grid[i][j] == '.') continue;
            total += 1.;
            sum += op[j];
        }

        oop[i] = sum/total;
    }

    for (int i=0; i < n; ++i)
    {
        double rank = 0.;
        //cout << wp[i] << ' ' << op[i] << ' ' << oop[i] << endl;
        rank = 0.25 * wp[i] + 0.5 * op[i] + 0.25 * oop[i];
        cout << setprecision(10) << fixed << rank << endl;
    }
}


inline void read()
{
    scanf("%d", &n);
    for (int i=0; i < n; ++i)
        scanf("%s", grid[i]);
}

int main()
{
    int brt, testNo = 0;
    cin >> brt;

    while (brt--)
    {
        read();
        cout << "Case #" << ++testNo << ":\n";
        solve();
    }
    return 0;
}
