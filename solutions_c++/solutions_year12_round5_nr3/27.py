#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <string.h>
#include <algorithm>
using namespace std;

const int maxn = 200 + 5;

int n;
long long m, f, p[maxn], s[maxn];
long long sp, lim;
vector< pair<long long, long long> > a;

long long calc(int i, long long k)
{
    if (m / f < k)
        return 0;
    long long tmp = lim * k;
    if (double(lim) * double(k) > m)
        tmp = m + 1;
    return (i > 0 ? a[i - 1].second + 1 : 0) * k + min((m - k * f) / a[i].first, tmp);
}

int main()
{
    freopen("c2.in", "r", stdin);
    freopen("c2.out", "w", stdout);

    int t2;
    cin >> t2;
    for (int t1 = 1; t1 <= t2; ++t1) {
        printf("Case #%d: ", t1);
        cin >> m >> f >> n;
        for (int i = 1; i <= n; ++i)
            cin >> p[i] >> s[i];
        a.clear();
        for (int i = 1; i <= n; ++i) {
            bool ok = true;
            for (int j = 1; j <= n; ++j) {
                if (p[j] < p[i] && s[j] >= s[i])
                    ok = false;
                if (p[j] <= p[i] && s[j] > s[i])
                    ok = false;
                if (p[j] == p[i] && s[j] == s[i] && j < i)
                    ok = false;
            }
            if (ok)
                a.push_back(make_pair(p[i], s[i]));
        }
        sort(a.begin(), a.end());
        long long ret = 0;
        double _f = 0;
        for (int i = 0; i < a.size(); ++i) {
            if (i == 0)
                lim = a[i].second + 1;
            else
                lim = a[i].second - a[i - 1].second;
            long long l = 0, r = m;
            while (l + 100000 < r) {
                long long m1 = l + (r - l) / 3, m2 = l + (r - l) * 2 / 3;
                if (calc(i, m1) < calc(i, m2))
                    l = m1;
                else
                    r = m2;
            }
            for (long long j = l; j <= r; ++j)
                ret >?= calc(i, j);
            f += a[i].first * lim;
            _f += double(a[i].first) * double(lim);
            if (_f > m)
                break;
        }
        cout << ret;
        printf("\n");
    }
    
    return 0;
}
