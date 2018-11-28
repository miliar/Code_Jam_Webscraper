#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <utility>
#include <cassert>
#include <numeric>
using namespace std;

#define REQUIRE(cond, message) \
    do { \
        if (!(cond)) { \
            std::cerr << message << std::endl; \
        } \
    } while (false)

#define forn(i, n) for (int i = 0; i < int(n); ++i)
#define for1(i, n) for (int i = 1; i <= int(n); ++i)
#define forv(i, v) forn(i, v.size())
#define pb push_back
#define mp make_pair
#define all(v) v.begin(), v.end()

typedef vector<int> vi;
typedef long long ll;
typedef vector<ll> vl;
typedef pair<int, int> pii;
typedef vector<string> vs;
typedef long double ld;
typedef pair<double, double> point;

double getX(const point& pt) { return pt.first; }
double getY(const point& pt) { return pt.second; }

const int INF = std::numeric_limits<int>::max();

void readData()
{
}

void outData()
{
}

void solve()
{
    int tc; cin >> tc;
    forn(it, tc) {
        int n; cin >> n;
        vector<pair<int, int> > a(n);
        forn(i, n) cin >> a[i].first >> a[i].second;
        int d; cin >> d;

        bool ans = false;

        vector<int> g(n, -1);
        g[0] = min(a[0].second, a[0].first);
        forn(i, n) {
            if (g[i] == -1) continue;
            if (a[i].first + g[i] >= d) {
                ans = true;
                break;
            }
            for (int j = i + 1; j < n; ++j) {
                if (a[j].first - a[i].first > g[i]) break;
                g[j] = max(g[j], min(a[j].first - a[i].first, a[j].second));
            }
        }

        cout << "Case #" << it + 1 << ": ";
        if (ans) cout << "YES\n";
        else cout << "NO\n";
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    readData();
    solve();
    outData();
    return 0;
}
