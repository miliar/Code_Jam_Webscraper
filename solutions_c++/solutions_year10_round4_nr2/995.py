#include<stdio.h>
#include<string.h>
#include<memory.h>

int arr[20][2000];
int num[20][2000];
int judge[2000];
int main()
{
    int ans,u;
    int i,j,p,t,tt;
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    scanf("%d",&tt);
    for (t = 1; t <= tt; t ++)
    {
        scanf("%d",&p);
        for (i = 0; i < (1 << p); i ++)
        {
            scanf("%d",&u);
            judge[i] = p - u;
        }
        for (i = 1;i <= p;i ++)
        {
           for(j = 0; j< (1 << (p-i) );j ++)
           {
              scanf("%d",&num[i][j]);
           }
        }
        memset(arr,0,sizeof(arr));
        for(i=0;i< (1 << p); i++)
        {
            for(j=0;j<judge[i];j++)
            {
                arr[p-j][i/(1<<(p-j))] = 1;
            }
        }
        ans = 0;
        for(i = 1; i <= p;i ++)
        {
           for(j=0; j< (1<<p); j ++)
           {
              if (arr[i][j])
                ans ++;
           }
        }
        printf("Case #%d: %d\n",t,ans);
    }

    return 0;
}
