#include<stdio.h>
#include<stdlib.h>
int min(int a,int b)
{
    return a<b?a:b;
}
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cas=1;cas<=t;cas++)
    {
        int sum=0,minnum=0x7fffffff,ans=0;
        int n;
        scanf("%d",&n);
        for(int i=1;i<=n;i++)
        {
            int num;
            scanf("%d",&num);
            minnum=min(minnum,num);
            sum^=num;
            ans+=num;
        }
        printf("Case #%d: ",cas);
        if(sum!=0) printf("NO\n");
        else       printf("%d\n",ans-minnum);
    }
}
