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

bool gen(ll n, ll pd) {
    if (n >= 100) return true;
    FOR(d,1,n)
        if ((d * pd) % 100 == 0) return true;
    return false;
}

bool check(ll n, ll pd, ll pg) {
    if (!gen(n, pd)) return false;
    if (pg == 100 && pd < 100) return false;
    if (pg == 0 && pd > 0) return false;
    return true;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    ll n, pd, pg;
    int test; cin >> test;
    FOR(t,1,test) {
        cout << "Case #" << t << ": ";
        cin >> n >> pd >> pg;
        if (check(n, pd, pg)) puts("Possible");
        else puts("Broken");
    }
    return 0;
}
