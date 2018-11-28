#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <stack>
#include <map>
#include <set>
using namespace std;

#define abs(x) ((x)<0?-(x):(x))
#define sqr(x) ((x)*(x))
#define pb push_back

typedef long double ldouble;
typedef pair<int, int> pii;
typedef long long llong;
typedef vector<int> vi;

const int inf = (int)1e9; 
const ldouble eps = 1e-7;

int main()
{
    #ifdef DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif
    int tests;
    cin >> tests;
    for (int testCase = 1; testCase <= tests; ++testCase)
    {
        llong L, t, n, c;
        cin >> L >> t >> n >> c;
        vector<llong> a(n);
        vector<llong> sum(n + 1);
        for (int i = 0; i < c; ++i)
        {
            cin >> a[i];
            sum[i + 1] = sum[i] + a[i] * 2;
        }
        for (int i = c; i < n; ++i)
        {
            a[i] = a[i - c];
            sum[i + 1] = sum[i] + a[i] * 2;
        }
        llong res = sum[n];
        if (L == 0)
        {
            printf("Case #%d: %lld\n", testCase, res);
            continue;
        }
        for (int fi = 0; fi < n; ++fi)
        {
            llong tt = sum[fi];
            if (tt > t)
                tt += a[fi];
            else
                tt = t + max(0LL, a[fi] - (t - tt) / 2);
            res = min(res, tt + sum[n] - sum[fi + 1]);
            
            for (int i = fi + 1; i < n; ++i)
            {
                llong ttt = tt;
                if (ttt > t) ttt += a[i];
                else ttt = t + max(0LL, a[i] - (t - ttt) / 2);
                if (L > 1)
                {
                    res = min(res, ttt + sum[n] - sum[i + 1]);
                }
                tt += a[i] * 2;
            }
        }
        printf("Case #%d: %lld\n", testCase, res);
    }
    return 0;
}

