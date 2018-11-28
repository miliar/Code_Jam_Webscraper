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

int ab(int x) {
    if (x < 0) return -x;
    else return x;
}

int main() {
    freopen("A1.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int test; scanf("%d", &test);
    FOR(t,1,test) {
        int n;
        scanf("%d", &n);
        int t1 = 0, t2 = 0, p1 = 1, p2 = 1;
        FOR(i,1,n) {
            char c; int u;
            cin >> c >> u;
            if (c == 'O') {
                t1 = max(t1 + ab(p1-u), t2) + 1;
                p1 = u;
            }
            else if (c == 'B') {
                t2 = max(t2 + ab(p2-u), t1) + 1;
                p2 = u;
            }
            else cout << "??????\n";
        }
        printf("Case #%d: %d\n", t, max(t1, t2));
    }
    return 0;
}
