#pragma comment(linker, "/STACK:16777216")
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <string>
#include <deque>
#include <complex>
#include <sstream>
#include <iomanip>

#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b); i>=_b; i--)
#define REP(i,a) for(int i=0,_a=(a); i<_a; i++)
#define ll long long
#define F first
#define S second
#define PB push_back
#define MP make_pair
using namespace std;

const double PI = acos(-1.0);

ll s[200111], cnt;

void update(int u) {
    ll x = u * (ll)u;
    while (x <= 1000000000000LL) {
        s[cnt++] = x;
        x = x * u;
    }
}

int sieve[1000111];

int main() {
    freopen("C-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    s[cnt++] = 2;
    FOR(i,2,1000000)
    if (!sieve[i]) {
        update(i);
        int j = i + i;
        while (j <= 1000000) {
            sieve[j] = 1;
            j += i;
        }
    }
    sort(s, s+cnt);
    int test; cin >> test;
    FOR(t,1,test) {
        ll u; cin >> u;
        printf("Case #%d: %d\n", t, upper_bound(s, s+cnt, u) - s);
    }
    return 0;
}
