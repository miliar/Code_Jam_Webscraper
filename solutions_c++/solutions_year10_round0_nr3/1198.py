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
#define ALL(a) a.begin(), a.end()
#define sqr(a) ((a) * (a))

typedef long long ll;

int a[1000];
ll s[1000];
int l[1000];

int main()
{
    int t;
    scanf("%d", &t);
    REP(kk, t)
    {
        int r, k, n;
        scanf("%d%d%d", &r, &k, &n);
        REP(i, n)
            scanf("%d", &a[i]);
        REP(i, n)
        {
            s[i] = a[i];
            int j = (i + 1) % n;
            while (s[i] <= k && (j != i))
                s[i] += a[j], j = (j + 1) % n;
            if (s[i] > k)
            {
                j = (j + n - 1) % n;
                s[i] -= a[j];
            }
            l[i] = j;
        }
        ll rt = 0;
        int x = 0;
        REP(i, r)
            rt += s[x], x = l[x];
        cout << "Case #" << kk + 1 << ": " << rt << endl;
    }
    return 0;
}
