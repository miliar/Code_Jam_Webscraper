#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstring>

using namespace std;

typedef long long ll;
typedef double db;

#define forab(i, a, b) for(int i = int(a); i < int(b); ++i)
#define forba(i, b, a) for(int i = int(b) - 1; i >= int(a); --i)
#define forn(i, n) forab(i, 0, n)

struct chl {
    int s, num;

    chl() {s = num = 0;}
    chl(int _s, int _num) {s = _s, num = _num;}

    bool operator <(const chl & a) const {
        if (s != a.s) return s > a.s;
        return num < a.num;
    }
};

int T;
int n, x, cur;
chl a[500];
double ans[500];

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d ", &T);
    forn(t, T) {
        scanf("%d", &n);
        x = 0;
        forn(i, n) {
            scanf("%d", &a[i].s);
            a[i].num = i;
            x += a[i].s;
        }

        printf("Case #%d: ", t + 1);

        sort(a, a + n);
        cur = 2 * x;
        int j = 0;
        while (j < n && cur < a[j].s * (n - j)) {
            cur -= a[j].s;
            ans[a[j].num] = 0.0;
            j++;
        }
        forab(i, j, n) ans[a[i].num] = (cur * 100.0 / (n - j) - a[i].s * 100.0) / x;
        forn(i, n) printf("%.10lf ", ans[i]);
        printf("\n");
    }
    return 0;
}
