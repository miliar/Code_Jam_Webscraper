#include <stdio.h>
#include <string.h>
#include <stdlib.h>
const int MAXN = 1005;
int g[MAXN];
long long pre[MAXN],cnt[MAXN];
long long sum,cir,cur,ans;
int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cs = 1;cs <= t;cs++)
    {
        int r,k,n;
        printf("Case #%d: ",cs);
        int i,j;
        sum = 0;
        scanf("%d %d %d",&r,&k,&n);
        for(i = 0;i < n;i++)
        {
            scanf("%d",&g[i]);
            sum += g[i];
        }
        if(sum <= k)
        {
            printf("%lld\n",sum*r);
            continue;
        }
        memset(pre,-1,sizeof(pre));
        memset(cnt,-1,sizeof(cnt));
        j = 0;
        sum = 0;
        int num = 0,p;
        while(1)
        {
            cur = 0;
            for(;cur+g[j] <= k;j = (j+1)%n) cur += g[j];
            num++;
            sum += cur;
            if(pre[j] == -1)
            {
                cnt[j] = num;
                pre[j] = sum;
            }
            else
            {
                ans = sum - pre[j];
                cir = num - cnt[j];
                p = j;
                break;
            }
        }
        long long  tmp = 0;
        j = 0;
        num = 0;
        while(1)
        {
            if(num >= r)    break;
            cur = 0;
            for(;cur+g[j]<=k;j = (j+1)%n)   cur += g[j];
            num++;
            tmp += cur;
            if(j == p)  break;
        }
        tmp += ( (r - num) / cir ) * ans;

        r = (r - num) % cir;
        j = p;
        num = 0;
        while(1)
        {
            if(num >= r)    break;
            cur = 0;
            for(;cur+g[j]<=k;j = (j+1)%n)   cur += g[j];
            num++;
            tmp += cur;
        }
        printf("%lld\n",tmp);
    }
    return 0;
}