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
#include <conio.h>

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

typedef pair<int, int> PII;
typedef vector<int> VI;

int a[1005], last[1005], num[1005], n, nTest, d;

int main () {
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    cin >> nTest;
    FOR(test, 1, nTest) {
        cin >> n;
        d = 0;
        memset(last, 0, sizeof(last));
        memset(num, 0, sizeof(num));        
        FR(i, n) cin >> a[i];
        sort(a, a + n);
        FR(i, n) {
            int minx = oo;
            int lj = d + 1;
            FOR(j, 1, d) {
                if (last[j] == a[i] - 1) {
                    if (minx > num[j]) {
                        minx = num[j];
                        lj = j;   
                    }
                }
            }
            if (lj == d + 1) d++;
            num[lj]++;
            last[lj] = a[i];                         
        }
        int res = oo;
        if (d == 0) res = 0;
        FOR(j, 1, d) res = min(res, num[j]);
        printf("Case #%d: %d\n", test, res);
    }
    return 0;   
}
