#include <iostream>
#include <queue>
#include <cstdio>
#include <cstring>
#include <map>
#include <vector>
#include <list>
#include <sstream>
#include <cmath>
#include <ctime>
#include <algorithm>

using namespace std;

#define FOR(i, a, b) for (int i = (a); i < (b); i++)
#define FOD(i, a, b) for (int i = (a); i >= (b); i--)
#define REP(i, a) for (int i = 0; i < (a); i++)
#define sz(a) ((int)a.size())
#define cl clear()
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define all(a) a.begin(), a.end()
#define sqr(a) ((a) * (a))

typedef long long ll;

int x[1000];
int v[1000];

int main()
{
    int t;
    scanf("%d", &t);
    REP(ii, t)
    {
        int n, k, b, t;
        scanf("%d%d%d%d", &n, &k, &b, &t);
        REP(i, n)
            scanf("%d", &x[i]);
        REP(i, n)
            scanf("%d", &v[i]);
        int rt = 0, kh = 0;
        vector <int> a;
        FOD(i, n - 1, 0)
            if (kh < k && x[i] + v[i] * t >= b)
                kh++, a.pb(i);
        if (sz(a) < k)
            printf("Case #%d: IMPOSSIBLE\n", ii + 1);
        else
        {
            reverse(all(a));
            /*REP(i, sz(a))
                    printf("%d ", a[i]);
                cout << endl;*/
            bool mod = 1;
            int rt = 0;
            while (mod)
            {
                mod = 0;
                int x = 1;
                while (x < sz(a) && a[x] - a[x - 1] == 1)
                    x++;
                if (x < sz(a) && a[x] - a[x - 1] != 1)
                {
                    rt += (a[x] - a[x - 1] - 1) * x;
                    int tt = a[x] - a[x - 1] - 1;
                    REP(i, x)
                        a[i] += tt;
                    mod = 1;
                }
                /*REP(i, sz(a))
                    printf("%d ", a[i]);
                cout << endl;*/
            }
            if (k != 0)
                rt += (n - a.back() - 1) * sz(a);
            printf("Case #%d: %d\n", ii + 1, rt);
        }
    }
}
