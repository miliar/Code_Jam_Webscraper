#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);

    int maxn = 1000;
    int a[maxn], b[maxn];
    int t; cin >>t;
    for (int tt = 1; tt <= t; ++ tt)
    {
        int n; cin >>n;
        int ans = 0;
        for (int i = 0; i < n; ++ i)
            cin >>a[i] >>b[i];
        for (int i = 0; i < n; ++ i)
            for (int j = i + 1; j < n; ++ j)
                if ((a[i] - a[j]) * (b[i] - b[j]) < 0)
                    ans ++;
        cout <<"Case #" <<tt <<": " <<ans <<endl;
    }
    return 0;
}
