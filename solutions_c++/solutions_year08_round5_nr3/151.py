#include <cmath>
#include <string>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <numeric>

using namespace std;

typedef signed long long i64;
typedef unsigned long long u64;
typedef long double real;

#define forn(i,n) for (int i = 0; i< int(n); i++)
#define fors(i,s) forn(i, s.length())
#define forv(i,v) forn(i, v.size())

#define two(n) (1 << (n))
#define has(mask, i) (((mask) & two(i)) != 0)

#define pb push_back
#define all(v) v.begin(), v.end()
#define mp make_pair

#define NMAX (12)

int z[NMAX][1 << NMAX];

char f[NMAX][NMAX];

int n, m;

vector<int> rows;

bool can(int a, int b)
{
    forn(i, m)
    {
        if (has(a, i) && has(b, i + 1))
            return false;
        if (has(a, i + 1) && has(b, i))
            return false;
        if (i > 0 && has(a, i - 1) && has(b, i))
            return false;
        if (i > 0 && has(b, i - 1) && has(a, i))
            return false;
    }
    return true;
}

int canF(int rowIdx, int rowMask)
{
    forn(i, m)
        if (f[rowIdx][i] == 'x' && has(rowMask, i))
            return false;
    return true;
}

int bitCount(int n)
{
    int result = 0;
    while (n > 0)
    {
        result += n % 2;
        n /= 2;
    }
    return result;
}

void solve()
{
    memset(z, 128, sizeof(z));

    z[0][0] = 0;

    cin >> n >> m;

    forn(i, n)
        scanf("%s", f[i + 1]);

    rows.clear();

    forn(i, 1 << m)
    {
        bool fail = false;
        forn(j, m)
            if (has(i, j) && has(i, j + 1))
                fail = true;
        if (!fail)
            rows.push_back(i);
    }

    for (int row = 1; row <= n; row++)
    {
        forv(j, rows)
        {
            int next = rows[j];

            if (canF(row, next))
            {
                forn(prev, 1 << m)
                    if (z[row - 1][prev] >= 0 && can(prev, next))
                    {
                        z[row][next] = max(z[row][next], z[row - 1][prev] + bitCount(next));
                    }
            } 
        }
    }

    int result = 0;

    forn(i, 1 << m)
        result = max(result, z[n][i]);

    cout << result;
}

int main()
{
    freopen("input.txt", "rt", stdin);

    int testCount;
    cin >> testCount;

    forn(ta, testCount)
    {
        cout << "Case #" << ta + 1 << ": ";
        solve();
        cout << endl;
    }

    return 0;
}

