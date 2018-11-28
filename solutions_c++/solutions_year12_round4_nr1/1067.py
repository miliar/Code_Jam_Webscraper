#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:64000000")
#define _USE_MATH_DEFINES
#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <ctime>
#include <math.h>
#include <set>
#include <map>
#include <cassert>
#include <queue>
#include <deque>
#include <stack>
#include <sstream>
#include <cstring>
#include <string>
#include <functional>
#include <numeric>
#include <bitset>
#include <cassert>
#include <complex>

using namespace std;

#define MP make_pair
#define all(v) (v).begin(), (v).end()
#define debug(x) cerr << #x << ": " << x << endl;

const int INF = ((1 << 30) - 1);
const long long LLINF = (((1LL << 60) - 1LL));
const double EPS = 1e-9;
const double PI = 3.14159265358979323846;  

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef long double LD;
typedef pair<LD, LD> pdd;
typedef pair<ll, ll> pll;


template <typename T>
string toStr(T x) {
    stringstream ss;
    ss << x;
    return ss.str();
}

string getStr(const vector<LD>& v) {
    char buff[25];
    string res;
    for (int i = 0; i < v.size(); ++i) {
        sprintf(buff, "%0.18lf", v[i]);
        res += string(buff);
        if (i + 1 != v.size()) {
            res += " ";
        }
    }
    return res;
}

double sqr(double x) {
    return x * x;
}

string solve() {
    int n;
    cin >> n;
    vector<pll> l(n);
    for (int i = 0; i < n; ++i) {
        cin >> l[i].first >> l[i].second;
    }
    ll D;
    cin >> D;
    vector<ll> maxLen(n, 0);
    maxLen[0] = l[0].first;
    bool ok = false;
    for (int i = 0; i < n; ++i) {
        ll len = maxLen[i];
        ll x = l[i].first;
        if (x + len >= D) {
            ok = true;
            break;
        }
        for (int j = i + 1; j < n; ++j) {
            if (len + x < l[j].first) {
                break;
            }
            ll dx = l[j].first - x;
            ll can = min(dx, l[j].second);
            maxLen[j] = max(maxLen[j], can);
        }
    }
    return ok ? "YES" : "NO";
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    string endline;
    getline(cin, endline);
    for (int test = 1; test <= T; ++test) {
        string res = solve();
        fprintf(stdout, "Case #%d: %s\n", test, res.c_str());
        fprintf(stderr, "Case #%d: %s\n", test, res.c_str());
    }
    return 0;
}