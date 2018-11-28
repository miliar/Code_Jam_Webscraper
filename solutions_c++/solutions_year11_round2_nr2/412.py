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

int n;
int d;

vector<pair<double,int> > v;

void read()
{
    cin >> n >> d;
    v = vector<pair<double,int> >(n);
    forn(i, n)
        cin >> v[i].first >> v[i].second;
}

bool check(double gap)
{
    vector<pair<double,double> > segs(n);
    forn(i, n)
        segs[i].first = v[i].first - gap, segs[i].second = v[i].first + gap;

    double p = -1E100;
    forn(i, n)
    {
        double first = max(p + d, segs[i].first);
        double last = first + d * (v[i].second - 1);
        if (last > segs[i].second)
            return false;
        p = last;
    }

    return true;
}

void process()
{
    sort(v.begin(), v.end());
    double lf = 0;
    double rg = 1E10;
    forn(tt, 200)
    {
        double mid = (lf + rg) / 2.0;
        if (check(mid))
            rg = mid;
        else
            lf = mid;
    }
    printf("%.10lf\n", (lf + rg) / 2.0);
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

