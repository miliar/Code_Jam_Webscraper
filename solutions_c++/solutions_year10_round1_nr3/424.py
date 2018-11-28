#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <bitset>
#include <utility>

using namespace std;

#define dbg(x) cerr<<#x<<" : "<<x<<endl
#define inf (1<<30)
#define PB push_back
#define MP make_pair
#define mset(x,a) memset(x,(a),sizeof(x))
typedef long long LL;
#define twoL(X) (((LL)(1))<<(X))
const double PI = acos(-1.0);
const double eps = 1e-8;

template <class T> T sqr(T x) {
    return x*x;
}

int gcd(int a, int b) {
    return (b == 0) ? a : gcd(b, a % b);
}

#define FOREACH(it, a) for(typeof((a).begin()) it = (a).begin(); it!=(a).end(); ++it)
#define ALL(x) (x).begin(), (x).end()


int T;
int a1, a2, b1, b2;

bool win(int a, int b) {
    if (a > b) swap(a, b);
    if (a == b) return 0;
    if (b % a == 0) return 1;
    else {
        if (win(b % a, a) && b / a == 1)
            return 0;
        else return 1;
    }
}

int main() {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    scanf("%d", &T);
    for (int ti = 1; ti <= T; ++ti) {
        scanf("%d%d%d%d", &a1, &a2, &b1, &b2);
        int res = 0;
        for (int i = a1; i <= a2; ++i) {
            for (int j = b1; j <= b2; ++j) {
                if (win(i, j))++res;
            }
        }
        printf("Case #%d: %d\n", ti, res);
    }
    return (EXIT_SUCCESS);
}


