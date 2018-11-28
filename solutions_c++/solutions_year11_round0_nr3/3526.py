#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<algorithm>

int n;
int s[1005];
int x[1005],sum[1005];

int max(int a,int b)
{
    if(a>b) return a;
    return b;
}
int main()
{
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    int i,j,k;
    int T;
    int case_cnt=0;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d",&n);
        int ans=0;
        memset(x,0,sizeof(x)),memset(sum,0,sizeof(sum));
        for(i=0;i<n;i++)
        {
            scanf("%d",&s[i]);
            ans^=s[i];
        }
        x[0]=sum[0]=s[0];
        int up=0;
        for(i=1;i<n;i++)
            x[i]=s[i]^x[i-1],sum[i]=s[i]+sum[i-1],up|=s[i];
        if(ans!=0)
        {
            printf("Case #%d: %s\n",++case_cnt,"NO");
            continue;
        }
        std::sort(s,s+n);
        int res=sum[n-1]-s[0];

        printf("Case #%d: %d\n",++case_cnt,res);
    }
}
