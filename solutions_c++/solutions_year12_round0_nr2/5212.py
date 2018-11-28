/*
ID   : mnlm1991
PROG : 
LANG : C++
*/

#include<map>
#include<set>
#include<list>
#include<cmath>
#include<queue>
#include<stack>
#include<string>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<iostream>
#include<iterator>
#include<algorithm>

using namespace std;

typedef long long LL;

int main()
{
    freopen("B-small-attempt2.in", "r", stdin);
    freopen("B-small-attempt2.out", "w", stdout);
    
    int T;
    while (scanf("%d", &T) != EOF)
    {
        int tc = 1;
        while (T--)
        {
            int s, p, n;
            scanf("%d%d%d", &n, &s, &p);
            int ans = 0;
            for (int i = 0; i < n; i++)
            {
                int x;
                scanf("%d", &x);
                int y = x / 3;
                int z = x % 3;
                if (z == 0)
                {
                    if (y >= p)
                    {
                        ans++;
                    }
                    else if (y - 1 >= 0 && y + 1 >= p && s > 0 && y + 2 <= 10)
                    {
                        ans++;
                        s--;
                    }
                }
                else if(z == 1)
                {
                    if (y + 1 >= p && y + 1 <= 10)
                    {
                        ans++;
                    }
                }
                else if(z == 2)
                {
                    if (y + 1 >= p && y + 1 <= 10)
                    {
                        ans++;
                    }
                    else if(y + 2 >= p && s > 0 && y + 2 <= 10)
                    {
                        ans++;
                        s--;
                    }
                }
            }
            printf("Case #%d: %d\n", tc++, ans);
        }
    }
    return 0;
}
