#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int Max, ans, sum, n;
int num[101];
bool fg[101];
void dfs(int a, int b, int sum, int k)
{
    if(a == b && k == n)
    {
        if(ans < sum)
            ans = sum;
        //printf("%d == %d\n",a,b);
    }
    if(k == n)
        return;
    if(!fg[k])
    {
        dfs(a^num[k], b, sum + num[k], k + 1);
        dfs(a, b^num[k], sum, k + 1);
    }
    else
    {
        dfs(a, b, sum, k + 1);
    }


}
int main()
{
    freopen("C-small-attempt0.in","r", stdin);
    freopen("C-small-attempt0.out","w", stdout);
    int t, x = 1;
    scanf("%d", &t);
    while(t--)
    {
        //int n;
        Max = 0;
        scanf("%d", &n);
        memset(fg, 0, sizeof(fg));
        for (int i = 0; i < n; i++)
            scanf("%d", &num[i]);
        for (int i = 0; i < n; i++)
        {
            ans = 0;
            fg[i] = 1;
            dfs(0, num[i], 0, 0);
            if(Max < ans)
                Max = ans;
            fg[i] = 0;
        }
        if(Max == 0)
            printf("Case #%d: NO\n", x++);
        else
            printf("Case #%d: %d\n", x++, Max);
    }

}
