#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
#define maxn 10000
int t,n;
int c[maxn];
int main()
{
    int t;
    int sum1,sum2,mi;
    int cs,i;
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    while(scanf("%d",&t)!=EOF)
    {
        cs = 1;
        while(t--)
        {
            scanf("%d",&n);
            mi = 0x3f3f3f3f;
            sum1 = sum2 = 0;
            for(i = 0 ; i < n; i++)
            {
                scanf("%d",&c[i]);
                mi = min(mi,c[i]);
                sum1 += c[i];
                sum2 = sum2 ^ c[i];
            }
            if(sum2 == 0)
                printf("Case #%d: %d\n",cs++,sum1 - mi);
            else
                printf("Case #%d: NO\n",cs++);
        }
    }
    return 0;
}
