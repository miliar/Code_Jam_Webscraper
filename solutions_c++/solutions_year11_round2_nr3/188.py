#include <string.h>
#include <iostream>
#include <cstdio>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <cmath>
#include <string>
#include <map>
#include <cassert>
#include <queue>

using namespace std;

#define forn(i, n)  for (int i = 0; i < int(n); i++)

#define X first
#define Y second

#define PI 3.1415926535897932384626433832795
#define R 10000

typedef pair<int,int> pt;

int m;
map<pt, vector<pt> > v;
set<pair<pt,pt> > used;
vector<pt> vt;
map<pt, int> tv;

vector<int> f, t;

pt center;
bool aroundCmp(const pt& a, const pt& b)
{
    return atan2(a.Y - center.Y * 1.0, a.X - center.X) < atan2(b.Y - center.Y * 1.0, b.X - center.X);
}

void dfs(pt from, pt to, vector<pt>& face)
{
    if (used.count(make_pair(from, to)) == 0)
    {
        used.insert(make_pair(from, to));
        face.push_back(to);
        center = to;
        vector<pt>& next = v[to];
        sort(next.begin(), next.end(), aroundCmp);
        forn(i, next.size())
            if (next[i] == from)
            {
                dfs(to, next[(i + 1) % next.size()], face);
                break;
            }
    }
}

map<pt,int> color;

int faces()
{
    v.clear();
    used.clear();
    color.clear();
    for (int i = 0; i < 2 * m; i += 2)
    {
        pt a, b;
        a = vt[f[i / 2]];
        b = vt[t[i / 2]];
        v[a].push_back(b);
        v[b].push_back(a);
    }

    vector<vector<pt> > result;

    for (map<pt, vector<pt> >::iterator i = v.begin(); i != v.end(); i++)
    {
        forn(j, i->second.size())
        {
            pt from = i->first, to = i->second[j];

            if (used.count(make_pair(from, to)) == 0)
            {
                vector<pt> face;
                dfs(from, to, face);
                if (face.size() < vt.size())
                    result.push_back(face);
            }
        }
    }

    int colors = 100000;
    forn(i, result.size())
        colors = min(colors, int(result[i].size()));

    map<pt,vector<int> > pf;
    forn(i, result.size())
    {
        forn(j, result[i].size())
            pf[result[i][j]].push_back(i);
    }

    int n = vt.size();
    m = result.size();

    set<pair<pt,pt> > bound;
    forn(i, n)
        bound.insert(make_pair(vt[i], vt[(i + 1) % n]));

    vector<vector<pt> > ord;

    vector<bool> used(m, false);
    forn(tt, m - 1)
    {
        forn(i, m)
            if (!used[i])
            {
                int b = 0;
                forn(j, result[i].size())
                {
                    pt f = result[i][j];
                    pt t = result[i][(j + 1) % result[i].size()];
                    if (!bound.count(make_pair(f, t)))
                        b++;
                }
                if (b == 1)
                {
                    ord.push_back(result[i]);
                    used[i] = true;
                    forn(j, result[i].size())
                    {
                        pt f = result[i][j];
                        pt t = result[i][(j + 1) % result[i].size()];
                        bound.erase(make_pair(f, t));
                        bound.insert(make_pair(t, f));
                    }
                    break;
                }
            }
    }

    int last = -1;
    forn(i, m)
        if (!used[i])
            last = i;

    assert(last != -1);
    assert(ord.size() + 1 == m);

    vector<int> colored(m, 0);

    int idx = 0;
    forn(i, result[last].size())
    {
        color[result[last][i]] = idx;
        idx = (idx + 1) % colors;
        if (i + 1 == result[last].size() && idx == 1)
            color[result[last][i]] = idx;
    }

    for (int tt = ord.size() - 1; tt >= 0; tt--)
    {
        vector<pt> o = ord[tt];
        int ff = -1;
        set<int> cc;
        forn(i, colors)                         \
            cc.insert(i);
        forn(i, o.size())
            if (color.count(o[i]) && color.count(o[(i + 1) % o.size()]))
            {
                cc.erase(color[o[i]]);
                cc.erase(color[o[(i + 1) % o.size()]]);
                ff = i;
                break;
            }
        assert(ff > -1);
        ff += 2;
        forn(i, o.size() - 2)
        {
            ff %= o.size();
            assert(color.count(o[ff]) == 0);
            if (cc.size() > 0)
            {
                color[o[ff]] = *cc.begin();
                cc.erase(*cc.begin());
            }
            else
            {
                bool ok = false;
                forn(ccx, colors)
                {
                    int pc = color[o[(ff - 1 + o.size()) % o.size()]];
                    int nc = color.count(o[(ff + 1) % o.size()]) == 0 ? -1 : color[o[(ff + 1) % o.size()]];

                    if (ccx != pc && ccx != nc)
                    {
                        color[o[ff]] = ccx;
                        ok = true;
                        break;
                    }
                }
                assert(ok);
            }
            ff++;
        }
        assert(cc.size() == 0);
    }

    forn(i, result.size())
    {
        set<int> c;
        forn(j, result[i].size())
            c.insert(color[result[i][j]]);
        assert(c.size() == colors);
    }

    return colors;
}

int n;
int e;

void read()
{
    f.clear();
    t.clear();
    cin >> n >> e;
    forn(i, n)
        f.push_back(i), t.push_back((i + 1) % n);

    forn(i, e)
    {
        int x;
        cin >> x;
        x--;
        f.push_back(x);
    }

    forn(i, e)
    {
        int x;
        cin >> x;
        x--;
        t.push_back(x);
    }

    vt.clear();
    tv.clear();
    forn(i, n)
    {
        double a = - 2 * PI / n * i;
        vt.push_back(pt(int(R * cos(a)), int(R * sin(a))));
        tv[vt[i]] = i;
    }
}

void process()
{
    m = f.size();
    cout << faces() << endl;
    forn(i, n)
    {
        if (i)
            cout << " ";
        cout << 1 + color[vt[i]];
    }
    cout << endl;
}

int main(int argc, char* argv[])
{
    freopen("input.txt", "rt", stdin);
    
    int cases;
    scanf("%d", &cases);

    int from = (argc > 1 ? atoi(argv[1]) : 1);
    int to = (argc > 2 ? atoi(argv[2]) : cases);

    for (int i = 1; i <= cases; i++)
    {
        read();
        if (from <= i && i <= to)
        {
            printf("Case #%d: ", i);
            process();
        }
    }

    return 0;
}


