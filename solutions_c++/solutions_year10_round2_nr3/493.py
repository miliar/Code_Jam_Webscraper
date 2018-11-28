#include<stdio.h>
#include<memory.h>
#define MOD 100003

int num[30],arr[30];
int main()
{
    int tt,t;
    int i,j,cur;
    int n,ct,ans;
    freopen("C-small-attempt1.in","r",stdin);
    freopen("C-small.out","w",stdout);
    scanf("%d",&t);
    for (tt = 1; tt <= t; tt ++)
    {
        scanf("%d",&n);
        ans = 0;
        for(i = 0; i < (1 << (n-1)); i ++)
        {
            if (i & (1 << (n - 2)) )
            {
                ct = 0;
                memset(arr,0,sizeof(arr));
                for(j = 0; j <= n - 2; j ++)
                {
                    if(i & (1 << j))
                    {
                        num[ct ++] = j + 2;
                        arr[j + 2] = ct;
                    }
                }
                cur = arr[n];
                while(cur != 1 && cur != 0)
                    cur = arr[cur];
                if (cur == 1)
                    ans ++;
            }
        }
        ans = (ans % MOD + MOD) % MOD;
        printf("Case #%d: %d\n",tt,ans);
    }
    return 0;
}
