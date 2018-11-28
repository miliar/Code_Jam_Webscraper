#include <cstdio>
#include <cstring>
#include <iostream>
#include <set>
using namespace std;

int l, A, B;
long long ans;
int a[20], m[20];
set <int> vis;

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("solve.out", "w", stdout);
    int T, tmp, p, f1, f2, tot;
    
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++)
    {
        scanf("%d%d", &A, &B);
        p = B, l = 0;
        while (p)
        {
              m[l++] = p % 10;
              p /= 10;
        }
        for (int j = 0; j < l / 2; j++)
        {
            tmp = m[l - 1 - j];
            m[l - 1 - j] = m[j];
            m[j] = tmp;
        }
        ans = 0;
        for (int i = A; i < B; i++)
        {
            p = i, l = 0;
            while (p)
            {
                  a[l++] = p % 10;
                  p /= 10;
            }
            for (int j = 0; j < l / 2; j++)
            {
                tmp = a[l - 1 - j];
                a[l - 1 - j] = a[j];
                a[j] = tmp;
            }
            vis.clear();
            for (int j = 1; j < l; j++)
            {
                f1 = f2 = p = tot = 0;
                for (int k = j; f1 != 2 && f2 != 2 && k < l; p++, k++)
                {
                    tot = tot * 10 + a[k];
                    if (f1 == 0)
                    {
                           if (a[k] > a[p]) f1 = 1;
                           else if (a[k] < a[p]) f1 = 2;
                    }
                    if (f2 == 0)
                    {
                           if (a[k] < m[p]) f2 = 1;
                           else if (a[k] > m[p]) f2 = 2;
                    }
                }
                for (int k = 0; f1 != 2 && f2 != 2 && p < l; k++, p++)
                {
                    tot = tot * 10 + a[k];
                    if (f1 == 0)
                    {
                           if (a[k] > a[p]) f1 = 1;
                           else if (a[k] < a[p]) f1 = 2;
                    }
                    if (f2 == 0)
                    {
                           if (a[k] < m[p]) f2 = 1;
                           else if (a[k] > m[p]) f2 = 2;
                    }
                }
                if (f1 != 2 && f2 != 2 && tot != i)
                {
                       if (vis.find(tot) == vis.end())
                       {
                                         vis.insert(tot);
                                         ans++;
                       }
                }
            }
        }
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
