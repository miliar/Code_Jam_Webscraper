#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <sstream>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <list>
using namespace std;
typedef long long int64;
#define showbit(a, b) (((a) >> (b)) & 1)
#define move(n) ((1) << (n))
#define sz(x) (int)x.size()
#define maxint 0x7fffffff
#define maxint64 0x7fffffffffffffffLL
#define sqr(x) ((x) * (x))
const double pi = acos(-1.0);
const double eps = 1e-8;
int sgn(double x) { return (x > eps) - (x < -eps); }
int main() {
    freopen("A-large.in","r",stdin);
    freopen("A.out", "w", stdout);
    int t, n, k;
    cin >> t;
    int Case = 1;
    while(t--) {
        cin >> n >> k;
        k %= move(n);
        printf("Case #%d: ", Case++);
        if(k == move(n) - 1) cout << "ON" << endl;
        else cout << "OFF" << endl;
    }
    return 0;
}
