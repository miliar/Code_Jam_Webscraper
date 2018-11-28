#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t, n, s, p;
    int x, ans;
    scanf("%d", &t);
    for (int tcase = 1; tcase <= t; tcase++)
    {
        scanf("%d%d%d", &n, &s, &p);
        ans = 0;
        for (int i = 0; i < n; i++)
        {
            scanf("%d", &x);
            if (x == 0 && p == 0) ans++;
            if (x >= 1 && (x + 2) / 3 >= p) ans++;
            else
            {
                if (s > 0 && x >= 2 && (x + 4) / 3 >= p)
                {
                    ans++;
                    --s;
                }
            }
        }
        printf("Case #%d: %d\n", tcase, ans);
    }
    fclose(stdout);
    return 0;
}
