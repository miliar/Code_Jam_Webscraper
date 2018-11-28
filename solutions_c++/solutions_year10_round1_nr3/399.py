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
int A1, A2, B1, B2;
bool ok(int a, int b) {
    if(a < b) swap(a, b);
    if(a == b) return false;
    if(a % b == 0) return true;
    if(a / b >= 2) return true;
    if(ok(b, a - b)) return false;
    return true;
}
int main() {
    int t;
    cin >> t;
    int Case = 1;
    while(t--) {
        cin >> A1 >> A2 >> B1 >> B2;
        int ans = 0;
        for(int i = A1; i <= A2; i++) {
            for(int j = B1; j <= B2; j++) {
                if(ok(i, j)) ans++;
            }
        }
        printf("Case #%d: %d\n", Case++, ans);
    }
    return 0;
}
