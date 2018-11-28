#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;
const int maxn=2000000;
int t, a, b, cnt, ans;
int vis[maxn];
int optimized_pow_n(int x, int n)
{
    int p=1;
    while (n>0)
    {
        if (n&1) p*=x;
        x*=x;
        n>>=1;
    }
    return p;
}
int main()
{
    //freopen("in.txt", "r", stdin);
   // freopen("out.txt", "w", stdout);
    scanf("%d", &t);
    cnt=1;
    while (t--)
    {
        ans=0;
        scanf("%d %d", &a, &b);
        for (int n=a; n<b; n++)
        {
            int sum=0;
            int tem=n;
            while (tem)
            {
                tem=tem/10;
                sum++;
            }
            tem=n;
            int num=sum-1;
            sum--;
            memset(vis, 0, sizeof(vis));
            while (sum)
            {
                int x=tem%10;
                tem=tem/10;
                tem=x*optimized_pow_n(10, num)+tem;
                if (tem>n&&tem<=b&&!vis[tem]) ans++, vis[tem]=1;
                sum--;
            }
        }
        printf("Case #%d: %d\n",cnt++, ans);
    }
    return 0;
}
