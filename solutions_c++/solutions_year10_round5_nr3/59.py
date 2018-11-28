#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>
#include <cstdio>
#include <cassert>
#include <string>
#include <queue>
#include <stack>
#include <deque>
#include <numeric>
#include <sstream>
#include <ctime>

using namespace std;

#define CIN_FILE "input.txt"
#define COUT_FILE "output.txt"

#define forn(i, n) for(int i = 0; i < int(n); i++)
#define for1(i, n) for(int i = 1; i <= int(n); i++)
#define forv(i, v) forn(i, v.size())

#define pb push_back
#define mp make_pair
#define all(v) v.begin(), v.end()

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

#define NMAX 205

int n;
int p[NMAX], v[NMAX];
vector<pii> a;

void merge_eq(vector<pii>& a)
{
    vector<pii> b = a;
    a.clear();
    int l = 0;
    while (l < b.size())
    {
        int r = l, s = 0;
        while (r < b.size() && b[l].first == b[r].first)
        {
            s += b[r].second;
            r++;
        }

        a.pb(mp(b[l].first, s));

        l = r;
    }
}

void solve(int tc)
{
    printf("Case #%d: ", tc);

    cerr << tc << endl;

    cin >> n;

    a.clear();

    forn(i, n)
    {
        cin >> p[i] >> v[i];
        a.pb(mp(p[i], v[i]));
    }

    sort(all(a));

    int ans = 0;

    while (true)
    {
        bool stop = true;

        forv(i, a)
        {
            if (a[i].second > 1)
            {
                pii p1 = mp(a[i].first - 1, 1);
                pii p2 = mp(a[i].first + 1, 1);
                a[i].second -= 2;

                if (a[i].second == 0)
                {
                    a.erase(a.begin() + i);
                }

                a.pb(p1);
                a.pb(p2);

                stop = false;
                break;
            }
        }

        if (stop) break;

        ans++;

        sort(all(a));

        merge_eq(a);
    }

    cout << ans << endl;
}

int main()
{
    freopen(CIN_FILE, "rt", stdin);
    freopen(COUT_FILE, "wt", stdout);
    int tc;
    scanf("%d\n", &tc);
    forn(it, tc) solve(it + 1);
    return 0;
}
            
