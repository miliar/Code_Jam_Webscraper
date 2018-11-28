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

vl populate(ll len, vl& r)
{
    vl res;
    res.pb(0);
    len -= r.back();
    ll x = r.back();
    r.pop_back();
    while (!r.empty() && r.back() <= len) {
        len -= r.back() * 2;
        x += r.back();
        res.pb(x);
        x += r.back();
        r.pop_back();
    }
    return res;
}

vector<point> solve(ll w, ll l, vl r)
{
    sort(all(r));
    vl cr = r;
    vl shifts = populate(l, r);
    vector<point> res;
    forv(i, shifts) {
        res.pb(mp(shifts[i], 0));
    }
    if (r.empty()) return res;
    ll s = cr[r.size()] + r.back();
    shifts = populate(w - s, r);
    forv(i, shifts) {
        res.pb(mp(l, shifts[i] + s));
    }
    if (r.empty()) return res;
    s = cr[r.size()] + r.back();
    shifts = populate(l - s, r);
    forv(i, shifts) {
        res.pb(mp(l - s - shifts[i], w));
    }
    if (r.empty()) return res;
    s = cr.back() + r.back() + cr[r.size()];
    ll t = cr.back() + r.back();
    assert(s >= 0);
    shifts = populate(w - s, r);
    assert(r.empty());
    forv(i, shifts) {
        res.pb(mp(0, t + shifts[i]));
    }
    return res;
}

void solve()
{
    int tc; cin >> tc;
    cout.precision(10);
    cout << fixed;
    forn(it, tc) {
        cout << "Case #" << it + 1 << ":";
        int n, w, l; cin >> n >> l >> w;
        vl r(n);
        forn(i, n) cin >> r[i];
        vector<pair<ll, int> > ids(n);
        forn(i, n) ids[i].first = r[i], ids[i].second = i;
        sort(all(ids));
        bool f = false;
        if (w > l) {
            swap(w, l);
            f = true;
        }
        vector<point> ans = solve(w, l, r);
        reverse(all(ans));
        if (f) {
            forv(i, ans) swap(ans[i].first, ans[i].second);
        }
        vector<point> res(n);
        forn(i, n) {
            res[ids[i].second] = ans[i];
        }
        forv(i, ans) {
            cout << " " << res[i].first << " " << res[i].second;
        }
        cout << endl;
    }
}

int main()
{
    readData();
    solve();
    outData();
    return 0;
}
