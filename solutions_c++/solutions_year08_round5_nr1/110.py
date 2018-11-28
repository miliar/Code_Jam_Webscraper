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

#define CMAX 7004

int n;
string s;

vector<
    set<int>
    > f = vector< set<int> >(CMAX, set<int>());

vector<
    vector<bool>
    > u = vector< vector<bool> >(CMAX, vector<bool>(CMAX, false));


void rotate(int& dx, int& dy, bool left)
{
    if (left)
    {
        int nx = -dy;
        int ny = +dx;

        dx = nx;
        dy = ny;
    }
    else
    {
        int nx = +dy;
        int ny = -dx;

        dx = nx;
        dy = ny;
    }
}

vector<int> xu;
vector<int> yu;

void solve()
{
    s = "";
    scanf("%d", &n);

    char w[512];

    forn(i, n)
    {
        int t;
        scanf("%s %d", w, &t);
        forn(j, t)
            s += w;
    }

    n = s.length();

    forn(i, CMAX)
        {
            f[i].clear();
        }

    if (xu.size() < 1000000 || true)
    {

    forv(i, xu)
    {
        u[xu[i]][yu[i]] = false;
    }

    }
    else
    {
        forn(i, CMAX)
            fill(all(u[i]), false);
    }

    xu.clear();
    yu.clear();
    /*
    forn(i, CMAX)
        forn(j, CMAX)
            u[i][j] = false;
    */
    int result = 0;

    {
        int x = CMAX / 2;
        int y = CMAX / 2;

        int dx = 0;
        int dy = 1;

        forn(i, n)
        {
            if (s[i] == 'L')
            {
                rotate(dx, dy, true);
                continue;
            }

            if (s[i] == 'R')
            {
                rotate(dx, dy, false);
                continue;
            }

            if (s[i] == 'F' && dx == 0)
            {
                if (dy == 1)
                {
                    f[y].insert(x);
                }
                else
                {
                    f[y - 1].insert(x);
                }

            }

            x += dx;
            y += dy;
        }

        forn(j, CMAX)
        {
            int odd = false;
            int prev = -1;

            set<int>& s = f[j];

            for (set<int>::iterator i = s.begin(); i != s.end(); i++)
            {
                if (!odd && prev > -1)
                {
                    for (int t = prev; t < *i; t++)
                    {
                        if (!u[t][j])
                        {
                            result++;
                            if (xu.size() < 1000000)
                            {
                                xu.push_back(t);
                                yu.push_back(j);
                            }
                        }
                        u[t][j] = true;
                    }
                }
                odd ^= true;
                prev = *i;
            }
        }
    }

    forn(i, CMAX)
        f[i].clear();

    {
        int x = CMAX / 2;
        int y = CMAX / 2;

        int dx = 0;
        int dy = 1;

        forn(i, n)
        {
            //cerr << "+ " << x << " " << y << endl;
            if (s[i] == 'L')
            {
                rotate(dx, dy, true);
                continue;
            }

            if (s[i] == 'R')
            {
                rotate(dx, dy, false);
                continue;
            }

            if (s[i] == 'F' && dy == 0)
            {
                if (dx == 1)
                {
                    f[x].insert(y);
                    //cerr << x << " " << y << endl;
                }
                else
                {
                    f[x - 1].insert(y);
                    //cerr << x << " " << y - 1 << endl;
                }

            }

            x += dx;
            y += dy;
        }

        forn(j, CMAX)
        {
            int odd = false;
            int prev = -1;

            set<int>& s = f[j];

            for (set<int>::iterator i = s.begin(); i != s.end(); i++)
            {
                if (!odd && prev > -1)
                {
                    for (int t = prev; t < *i; t++)
                    {
                        if (!u[j][t])
                        {
                            result++;
                            if (xu.size() < 1000000)
                            {
                                xu.push_back(j);
                                yu.push_back(t);
                            }
                        }
                        u[j][t] = true;
                    }
                }
                odd ^= true;
                prev = *i;
            }
        }
    }

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

