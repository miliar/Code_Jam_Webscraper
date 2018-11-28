#include <cstring>
#include <iostream>
#include <cstdio>
#include <ctime>
#include <vector>
#include <set>
#include <string>
#include <map>
#include <cassert>
#include <queue>
#include <climits>
#include <cstdlib>
#include <algorithm>
#include <cmath>

using namespace std;

#define forn(i, n)  for (int i = 0; i < int(n); i++)

struct e {
    int from, to, w;
};

double x, r, t;
int s;
int n;
vector<e> d;
map<pair<int,int>,int> dd;

vector<e> segs;

bool operator <(const e& a, const e& b)
{
    return a.w < b.w;
}

void read()
{
    cin >> x >> s >> r >> t;
    cin >> n;

    d = vector<e>(n);
    dd.clear();
    forn(i, n)
    {
        cin >> d[i].from >> d[i].to >> d[i].w;
        dd[make_pair(d[i].from, d[i].to)] = d[i].w;
    }

    set<int> pos;
    pos.insert(0);
    pos.insert(x);

    forn(i, n)
        pos.insert(d[i].from),
        pos.insert(d[i].to);

    vector<int> p(pos.begin(), pos.end());
    segs.clear();
    forn(i, p.size() - 1)
    {
        int from = p[i];
        int to = p[i +  1];
        if (dd.count(make_pair(from, to)) > 0)
        {
            e ee = {from, to, dd[make_pair(from, to)] + s};
            segs.push_back(ee);
        }
        else
        {
            e ee = {from, to, s};
            segs.push_back(ee);
        }
    }
}

void process()
{
    sort(segs.begin(), segs.end());

    double result = 0;
    forn(i, segs.size())
        result += (segs[i].to - segs[i].from) / double(segs[i].w);

    forn(i, segs.size())
    {
        if (t > 1E-10)
        {
            double nv = segs[i].w + r - s;

            double nt = (segs[i].to - segs[i].from) / nv;
            double tt = nt;
            nt = min(nt, t);
            t -= nt;

            result -= (segs[i].to - segs[i].from) / double(segs[i].w);
            result += nt + (segs[i].to - segs[i].from - nt * nv) / double(segs[i].w);
        }
    }

    printf("%.10lf\n", result);
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

