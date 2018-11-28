#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>

using namespace std;

int a[200];

int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    string s = "yhesocvxduiglbkrztnwjpfmaq";
    int z;
    scanf("%d\n", &z);
    for (int x = 1; x <= z; x++)
    {
        int ans = 0, m, s, p;
        printf("Case #%d: ", x);
        cin >> m >> s >> p;
        for (int i = 1; i <= m; i++)
            cin >> a[i];
        sort(a + 1, a + m + 1);
        for (int i = m; i >= 1; i--)
        {
            if (a[i] == 0) continue;
            if (((a[i] + 2) / 3) >= p) ans++; else
            {
                if (((p - 1) * 3 - 1 <= a[i]) && (s > 0))
                {
                    ans++;
                    s--;
                }
            }
        }
        if (p == 1)
        {
            ans = m;
            for (int i = 1; i <= m; i++)
                if (a[i] == 0) ans--;
        }
        if (p == 0) ans = m;
        printf("%d\n", ans);
    }
    return 0;
}
