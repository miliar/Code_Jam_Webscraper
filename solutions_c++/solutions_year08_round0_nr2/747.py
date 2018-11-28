#include <iostream>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <vector>

using namespace std;

vector<pair<int,int> > read_sched(int n)
{
    string line;
    vector<pair<int,int> > rv(n);
    for( int i = 0; i != n; ++i )
    {
        getline(cin, line);
        int dh, dm, ah, am;
        sscanf(line.c_str(), "%d:%d %d:%d", &dh, &dm, &ah, &am);

        int dt = 60*dh + dm;
        int at = 60*ah + am;
        rv[i] = make_pair(dt, at);
    }
    return rv;
}

void solve(int c)
{
    string line;
    getline(cin, line);
    int t = atoi(line.c_str());

    getline(cin, line);
    int na, nb;
    sscanf(line.c_str(), "%d %d", &na, &nb);

    vector<pair<int,int> > ab = read_sched(na);
    vector<pair<int,int> > ba = read_sched(nb);

    vector<int> a(1550);
    vector<int> b(1550);

    for( int i = 0; i != na; ++i )
    {
        a[ab[i].first]--;
        b[ab[i].second+t]++;
    }
    for( int i = 0; i != nb; ++i )
    {
        b[ba[i].first]--;
        a[ba[i].second+t]++;
    }
    int ta = 0, tb = 0;
    int ma = 0, mb = 0;
    for( int i = 0; i != 24*60; ++i )
    {
        ta += a[i];
        tb += b[i];
        ma = min(ma, ta);
        mb = min(mb, tb);
    }
    cout << "Case #" << c << ": " << -ma << ' ' << -mb << endl;
}

int main()
{
    string line;
    getline(cin, line);
    int N = atoi(line.c_str());
    for( int c = 1; c <= N; ++c )
        solve(c);

    return 0;
}
