#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
#include <cmath>
#include <utility>
#include <set>
#include <map>
#include <vector>

#define ll long long int
#define clr(a) memset(a, 0, sizeof(a))
#define FOR(a, b) for(int a = 0; a < (b); a++)
#define iter(a) typeof(a.begin())
#define foreach(a, it) for(typeof(a.begin()) it = a.begin(); it != a.end(); it++)

using namespace std;

const long double EPS = 1e-8;
const int INF = 1000000001;
const int MAXN = 1000001;

int a[MAXN];
int n;
int c, d;

bool check(long double x)
{
    long double lt = - x + a[0];
    for (int i = 1; i < n; ++i)
    {
        if (lt + d - a[i] - x > EPS) return false;
        lt = max(lt + d, ((long double)a[i]) - x);
    }
    return true;
}

int main()
{
    freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
    for (int t = 1; t <= T; ++t)
    {

        scanf("%d%d", &c, &d);
        n = 0;
        FOR(i, c)
        {
            int v, x;
            scanf("%d%d", &x, &v);
            FOR(j, v)
                a[n++] = x;
        }
        long double l, r;
        l = 0.0;
        r = 1100000000000.0;
        FOR(i, 100)
        {
            long double m = (l + r) / 2;
            if (check(m)) r = m;
                else l = m;
        }
        printf("Case #%d: %.7lf\n", t, (double)r);
    }
    return 0;
}
