#include <cstdlib>
#include <iostream>

using namespace std;

#define le 100

int a[105];

bool cmp(int a, int b)
{
     return a > b;
}

int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.out","w",stdout);
    int n, s, p, ans, i;
    int t;
    scanf ("%d", &t);
    for (int cas = 1; cas <= t; cas++)
    {
        scanf ("%d %d %d", &n, &s, &p);
        printf ("Case #%d: ", cas);
        int temp = p + p - 1 + p - 1;
        int temp2 = p + p - 2 + p - 2;
        for (i = 0; i < n; i++)
            scanf ("%d", &a[i]);
        sort(a , a + n, cmp);
        ans = 0;
        for (i = 0; i < n; i++)
        {
            if (a[i] >= temp)
               ans++;
            else if (a[i] < 2)
                 break;
            else
            {
                if (s <= 0)
                   break;
                if (a[i] >= temp2)
                {
                   ans++;
                   s--;
                }
                else
                    break;
            }
        }
        printf ("%d\n", ans);
    }
    return 0;
}
