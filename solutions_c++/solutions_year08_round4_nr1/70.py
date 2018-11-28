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

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef vector<vs> vvs;

#define forr(i,n0,n1) for(int i=(n0); i<(n1); i++)
#define forn(i,n) for(int i=0; i<(n); i++)
#define fors(i,s) forn(i, (int)s.length())
#define forv(i,v) forn(i, (int)v.size())
#define fore(t, it, obj) for (t :: iterator it = obj.begin(); it != obj.end(); it++)

#define two(n) (1 << (n))
#define has(mask, i) (((mask) & two(i)) != 0)

#define pb push_back
#define all(v) v.begin(), v.end()
#define mp make_pair

#define AND 1
#define OR 0
#define LEAF 2

struct node
{
    int type, value;
    bool change;
};

int n, v;

vector<node> tree;

#define INF 100000

int z[100000][2];

int apply(int a, int b, int type)
{
    if (type == AND)
        return a & b;
    else
        return a | b;
}

int solve(int idx, int value)
{
    if (z[idx][value] >= 0)
        return z[idx][value];

    int& result = z[idx][value];

    if (tree[idx].type == LEAF)
    {
        if (tree[idx].value == value)
            return (result = 0);
        else
            return (result = INF);
    }
    else
    {
        result = INF;

        forn(a, 2)
            forn(b, 2)
            {
                //a = 1, b = 1;
                int lf = solve(2 * (idx + 1) - 1, a);
                int rg = solve(2 * (idx + 1), b);

                if (lf < INF & rg < INF)
                {
                    if (apply(a, b, tree[idx].type) == value)
                    {
                        result = min(result, lf + rg);
                    }

                    if (tree[idx].change && apply(a, b, tree[idx].type ^ 1) == value)
                    {
                        result = min(result, 1 + lf + rg);
                    }
                }
            }

        return result;
    }
}

int main()
{
    freopen("input.txt", "rt", stdin);

    int testCount;

    cin >> testCount;

    forn(ta, testCount)
    {
        cin >> n >> v;

        tree = vector<node>(n);

        int m = (n - 1) / 2;

        forn(i, m)
        {
            int g, change;

            cin >> g >> change;
            tree[i].type = g;
            tree[i].change = change;
        }

        for (int i = m; i < n; i++)
        {
            tree[i].type = LEAF;
            cin >> tree[i].value;
        }

        memset(z, -1, sizeof(z));

        int result = solve(0, v);

        if (result >= INF)
            cout << "Case #" << ta + 1 << ": " << "IMPOSSIBLE" << endl;
        else
            cout << "Case #" << ta + 1 << ": " << result << endl;
    }

    return 0;
}


