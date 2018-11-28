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

int n, m;
int k;
char f[1000][1000];
int z[1000][1000];

#define M 10007

void solve()
{
    cin >> n >> m >> k;

    memset(f, 0, sizeof(f));

    forn(i, k)
    {
        int x, y;
        cin >> x >> y;
        f[x - 1][y - 1] = true;
    }

    memset(z, 0, sizeof(z));

    z[0][0] = 1;

    forn(i, n)
        forn(j, m)
        {
            if (i == 0 || j == 0)
                continue;

            if (f[i][j])
                continue;

            //
            {
                int px = i - 1;
                int py = j - 2;

                if (px >= 0 && py >= 0)
                    z[i][j] += z[px][py];
            }

            //
            {
                int px = i - 2;
                int py = j - 1;

                if (px >= 0 && py >= 0)
                    z[i][j] += z[px][py];
            }

            z[i][j] %= M;
        }

    cout << z[n - 1][m - 1] % M;
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

