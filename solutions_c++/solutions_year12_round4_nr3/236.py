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

bool below(ll x1, ll y1, ll x2, ll y2, ll x, ll y)
{
    return (y1 * (x2 - x1) + (y2 - y1) * (x - x1) > y * (x2 - x1));
}

bool above(ll x1, ll y1, ll x2, ll y2, ll x, ll y)
{
    return (y1 * (x2 - x1) + (y2 - y1) * (x - x1) < y * (x2 - x1));
}

bool check(int x1, int y1, int x2, int y2, const vi& y)
{
    for (int i = x1 + 1; i < x2; ++i) {
        if (!below(x1, y1, x2, y2, i, y[i])) return false;
    }
    for (int i = x2 + 1; i < (int)y.size(); ++i) {
        if (above(x1, y1, x2, y2, i, y[i])) return false;
    }
    return true;
}

void solve()
{
    int tc; cin >> tc;
    forn(it, tc) {
        int n; cin >> n;
        vi x(n - 1);
        forv(i, x) cin >> x[i], --x[i];
        cout << "Case #" << it + 1 << ":";
        vi y(n);
        bool ok = false;
        forn(inIt, 1000) {
            ok = true;
            forv(i, x) {
                if (!check(i, y[i], x[i], y[x[i]], y)) {
                    ++y[x[i]];
                    ok = false;
                    break;
                }
            }
            if (ok) break;
        }
        if (!ok) cout << " Impossible\n";
        else {
            forv(i, y) cout << " " << y[i];
            cout << endl;
        }
    }
}

int main()
{
    readData();
    solve();
    outData();
    return 0;
}
