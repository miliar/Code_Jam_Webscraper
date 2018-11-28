#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;

int t, n, o, b, num;
int ans, so, sb, tmp, d;
char ch;

int main()
{
    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);
    scanf("%d", &t);
    for (int cas = 1; cas <= t; cas++)
    {
        scanf("%d ", &n);
        o = b = 1;
        ans = so = sb = 0;
        for (int i = 0; i < n; i++)
        {
            scanf("%c %d ", &ch, &num);
            if (ch == 'O')
            {
                   tmp = ans - so;
                   d = abs(num - o);
                   if (tmp < d) d -= tmp;
                   else d = 0;
                   so = ans = ans + d + 1;
                   o = num;
            }
            else
            {
                tmp = ans - sb;
                d = abs(num - b);
                if (tmp < d) d -= tmp;
                else d = 0;
                sb = ans = ans + d + 1;
                b = num;
            }
        }
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
