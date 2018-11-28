#include <iostream>
#include <cstdio>
using namespace std;

const int MAXN = 10005;
int res[MAXN];

int main()
{
    freopen("dd.in", "r", stdin);
    freopen("outd.txt", "w", stdout);
    int t,n;
    int i,j,k;
    scanf("%d",&t);
    for(k = 1;k <= t;k ++)
    {
        scanf("%d",&n);
        if(1 == n)
        {
            scanf("%d",&res[0]);
            printf("Case #%d: 0.000000\n",k);
        }
        else
        {
            int sum = 0;
            for(i = 1;i <= n;i ++)
            {
                scanf("%d",&res[i]);
                if(i == res[i]) sum ++;
            }
            printf("Case #%d: %d.000000\n",k,n - sum);
        }
    }
    return 0;
}
