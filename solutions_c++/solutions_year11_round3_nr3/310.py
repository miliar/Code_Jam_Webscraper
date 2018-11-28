#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;

bool q;
int t, n, L, H, ans, a[100];

int main()
{
    freopen("C-small-attempt1.in", "r", stdin);
    freopen("C-small-attempt1.out", "w", stdout);
    scanf("%d", &t);
    for (int cas = 1; cas <= t; cas++)
    {
        printf("Case #%d: ", cas);
        scanf("%d%d%d", &n, &L, &H);
        for (int i = 0; i < n; i++)
            scanf("%d", &a[i]);
        ans = -1;
        for (int i = L; i <= H; i++)
        {
            q = true;
            for (int j = 0; j < n; j++)
                if (i % a[j] != 0 && a[j] % i != 0)
                {
                      q = false;
                      break;
                }
            if (q)
            {
                  ans = i;
                  break;
            }
        }
        if (ans >= 0) printf("%d\n", ans);
        else printf("NO\n"); 
    }
    return 0;
}
