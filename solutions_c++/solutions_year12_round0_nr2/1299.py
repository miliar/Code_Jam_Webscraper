#include"stdio.h"
int t,i,j,n,s,p,bs[31],x,ans;
int main()
{
    //freopen("2.in","r",stdin);
    //freopen("2.txt","w",stdout);
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%d%d%d",&n,&s,&p);
        for(ans=j=0;j<=30;j++) bs[j]=0;
        for(j=0;j<n;j++)
        {
            scanf("%d",&x);
            bs[x]++;
        }
        for(j=30;j>=p;)
            if(bs[j]--)
                if(j+3>p*3) ans++;
                else if(s)
                    if(j+5>p*3)
                    {
                        ans++;
                        s--;
                    }
                    else break;
                else break;
            else j--;
        printf("Case #%d: %d\n",i,ans);
    }
    //scanf(" ");
}
