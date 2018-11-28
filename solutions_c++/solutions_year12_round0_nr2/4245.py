#include <iostream>
#include <cstring>
#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;



int main()
{
        int t,tt;
        for (scanf("%d", &tt),t=1; t<=tt; ++t) {
                int n,p,m;
                scanf("%d%d%d", &n, &m, &p);
                int a[111];
                for (int i = 0; i < n; ++i) scanf("%d", a + i);
                sort(a, a+n);
                int ans = 0;
                for (int i = n - 1; i >= 0; --i)
                        if (a[i]+2 >= p*3)
                                ++ans; else
                        if (a[i] >= 2 && a[i] <= 28
                        && (a[i] - p) / 2 >= p - 2)
                                if (m)
                                        ++ans,--m;
                printf("Case #%d: %d\n", t, ans);
        }
        return 0;
}
