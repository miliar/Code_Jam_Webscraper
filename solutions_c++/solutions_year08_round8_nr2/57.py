#include <string>
#include <sstream>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <algorithm>
#include <queue>
#include <iostream>
#include <cstdio>
#include <cassert>
#include <utility>

using namespace std;

#define two(n) (1 << (n))
#define hold(mask, i) (((mask) & two(i)) != 0)
#define all(v) v.begin(), v.end()
#define forn(i, n) for (int i = 0; i < int(n); ++i)

int n;

map<string, vector<pair<int,int> > > s;
set<string> _names;
int m;
int result;

void solve(vector<string> f)
{
    vector<pair<int,int> > t;
    set<int> x;
    forn(i, f.size())
        forn(j, s[f[i]].size())
        {
            t.push_back(s[f[i]][j]);
            x.insert(s[f[i]][j].first);
            x.insert(s[f[i]][j].second);
        }

    if (x.count(1) == 0 || x.count(10000) == 0)
        return;

    map<int,int> r;

    int size = 0;
    for (set<int>::iterator i = x.begin(); i != x.end(); i++)
    {
        r[*i] = size++;
        set<int>::iterator j = i;
        j++;
        if (j != x.end())
        {
            if (*j - *i > 1)
            {
                r[(*j + *i) / 2] = size++;
            }
        }
    }


    int n = t.size();

    forn(i, n)
        t[i].first = r[t[i].first],
        t[i].second = r[t[i].second];

    sort(all(t));

    vector<int> z(r.size() + 1);

    int m = r.size();

    forn(i, m)
        z[i + 1] = INT_MAX;

    z[0] = 0;

    forn(i, n)
    {
        int from = t[i].first;

        if (z[from] < INT_MAX)
        {
            int next = from;
            while (next <= t[i].second)
            {
                next++;
                z[next] = min(z[next], z[from] + 1);
            }
        }
        else
            break;
    }

    if (z[m] < INT_MAX)
    {
        result = min(z[m], result);
    }
}

void read()
{
    cin >> n;
    s.clear();
    _names.clear();
    forn(i, n)
    {
        string name;
        int lf, rg;
        cin >> name >> lf >> rg;
        s[name].push_back(make_pair(lf, rg));
        _names.insert(name);
    }
}

void solve()
{
    vector<string> names(all(_names));
    m = names.size();
    result = INT_MAX;
    forn(i, m)
    {
        vector<string> na;
        na.push_back(names[i]);
        solve(na);
    }
    forn(i, m)
    forn(j, i)
    {
        vector<string> na;
        na.push_back(names[i]);
        na.push_back(names[j]);
        solve(na);
    }
    forn(i, m)
    forn(j, i)
    forn(k, j)
    {
        vector<string> na;
        na.push_back(names[i]);
        na.push_back(names[j]);
        na.push_back(names[k]);
        solve(na);
    }
    if (result == INT_MAX)
        cout << "IMPOSSIBLE" << endl;
    else
        cout << result << endl;
}

int main() {
    freopen("input.txt", "rt", stdin);

    int minTest = 1;
    int maxTest = 50000;

    int testCount;
    cin >> testCount;

    for (int test = 1; test <= testCount; test++)
    {
        read();
        if (minTest <= test && test <= maxTest)
        {
            cout << "Case #" << test << ": ";

            solve();
        }
    }

    return 0;
}
