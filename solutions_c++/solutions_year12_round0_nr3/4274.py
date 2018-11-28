#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cstring>

using namespace std;

int findlen(int x)
{
    int m = 1;
    while (x / m > 0)
    {
        m *= 10;
    }
    return m / 10;
}

int findnext(int x, int l)
{
    int tmp = x % 10;
    return tmp * l + x / 10;
}

int solve(int a,int b)
{
    int ans = 0;
    for (int i=a;i<b;i++)
    for (int j=i+1;j<=b;j++)
    {
        if (findlen(i) != findlen(j)) continue;
        int tmp = i;
        int l = findlen(tmp);
        while (true)
        {
            tmp = findnext(tmp, l);
            if (tmp == j)
            {
                ans++;
                break;
            }
            if (tmp == i) break;
        }
    }
    return ans;
}

int main()
{
    int n;
    scanf("%d",&n);
    for (int T=1;T<=n;T++)
    {
        int a,b;
        scanf("%d%d", &a, &b);
        printf("Case #%d: %d\n", T, solve(a,b));
    }
    return 0;
}
