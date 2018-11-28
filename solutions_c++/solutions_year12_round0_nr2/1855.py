#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <cstring>
//#include <conio.h>

using namespace std;

#define oo 1000000000
#define fi first
#define se second
#define sqr(a) ((a)*(a))
#define FR(i,n) for (int i = 0; i < (n); i++)
#define DN(i,a) for(int i = (a)-1; i >= 0; i--)
#define FOR(i,a,b) for (int i = (a); i <= (b); i++)
#define DOWN(i,a,b) for(int i = (a); i >= (b); i--)
#define FORV(i,a) for(typeof(a.begin()) i = a.begin(); i != a.end(); i++)
#define pb push_back

typedef pair<int, int> PII;
typedef vector<int> VI;
VI num1, num2;

int T, n, s, p, a[1000];

bool cmp(int a, int b) {
    return a > b;
}

int main () {
    freopen("B-large.in", "r", stdin);
    freopen("B.out", "w", stdout);
    cin >> T;
    FOR(i, 1, T) {
        printf("Case #%d: ", i);
        cin >> n >> s >> p;
        if (p <= 1) {
            int res = 0;
            FOR(j, 1, n) {
                int x;
                cin >> x;
                if (x >= p) res++;
            }
            cout << res << endl;
            continue;
        }
        int res1 = 0, res2 = 0;
        FOR(j, 1, n) {
            int x;
            cin >> x;
            if (x >= 3 * p - 2) res1++;
            else
            if (x >= 3 * p - 4) res2++;
        }
        cout << res1 + min(res2, s) << endl;
    }
    return 0;
}
