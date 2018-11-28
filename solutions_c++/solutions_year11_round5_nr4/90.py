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

char s[66], a[66];
bool found;

void attempt(int n, ll res, ll lt) {
    if (found) return ;
    if (n < 0) {
        ll now = (int) (sqrt(res) + 0.5);
        if (now * now == res) {
            found = true;
            REP(i,strlen(s)) cout << a[i];
            puts("");
        }
        return ;
    }
    
    FOR(now,0,1)
    if (s[n] == '?' || now == s[n] - '0') {
        a[n] = now + '0';
        attempt(n-1, res + (now?lt:0), lt + lt);
        if (found) return ;
    }
}

void solve() {
    found = false;
    attempt(strlen(s) - 1, 0, 1);
}


int main() {
    freopen("D-small.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int test; scanf("%d\n", &test);
    FOR(t,1,test) {
        printf("Case #%d: ", t);
        gets(s);
        solve();
    }
    return 0;
}