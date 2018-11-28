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

const long double EPS = 1e-9;
const int INF = 1000000001;
const int MAXN = 1003;

struct inter{
    int w, l;
};

inter a[MAXN];

bool _less(inter a, inter b)
{
    return a.w < b.w;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	//freopen("", "w", stderr);
    int T;
    cin >> T;
    for(int t = 1; t <= T; ++t)
    {
        int x, s, r, tm, n;
        scanf("%d%d%d%d%d", &x, &s, &r, &tm, &n);


        FOR(i, n)
        {
            int b, e;
            scanf("%d%d%d", &b, &e, &a[i].w);
            a[i].l = e - b;
            x -= a[i].l;
        }
        if (x != 0) a[n].l = x, a[n++].w = 0;
        sort(a, a + n, _less);
        double o = tm;
        double ans = 0;
        FOR(i, n)
        {
            if (((double)a[i].l) / (a[i].w + r) - o > EPS)
            {
                double ws = ((double)a[i].l) - o * (a[i].w + r);
                ans += o + ws / (double)(a[i].w + s);
                o = 0;
            }
            else
            {
                o -= ((double)a[i].l) / ((double)(a[i].w + r));
                ans += ((double)a[i].l) / (double)(a[i].w + r);
            }
        }

        printf("Case #%d: %.8lf\n", t, ans);

        /*
        int p = 0;
        FOR(i, n)
        {
            int b, e, w;
            scanf("%d%d%d", &b, &e, &w);
            int s0 = b - p;
            if (((double)s0) / r - tm > EPS)
            {
                double ws = s0 - tm * r;
                ans += tm + ws / s;
                tm = 0;
            }
            else
            {
                tm -= ((double)s0) / r;
                ans += ((double)s0) / r;
            }
            p = b;
            s0 = e - p;
            if (((double)s0) / (w + r) - tm > EPS)
            {
                double ws = s0 - tm * (w + r);
                ans += tm + ws / (w + s);
                tm = 0;
            }
            else
            {
                tm -= ((double)s0) / (w + r);
                ans += ((double)s0) / (w + r);
            }
            p = e;
        }
        int s0 = x - p;
        if (((double)s0) / r - tm > EPS)
            {
                double ws = s0 - tm * r;
                ans += tm + ws / s;
                tm = 0;
            }
            else
            {
                tm -= ((double)s0) / r;
                ans += ((double)s0) / r;
            }
            */


    }

	return 0;
}




