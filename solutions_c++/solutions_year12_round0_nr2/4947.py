#include<stdio.h>
#include<stdlib.h>
int g[1000];
int judge(int x,int p)
{
    if(x%3==0)
    {
        int ns=x/3;
        if(ns>=0&&ns>=p)
            return 1;
        else
        {
            int min=x/3-1;
            int s=x/3+1;
            if(min>=0&&s>=p)
                return 2;
            else
                return 0;
        }    
    }
    else if(x%3==1)
    {
        int ns=x/3+1;
        int min=ns-1;
        if(min>=0&&ns>=p)
            return 1;
        else
        {
            return 0;
        }
    }
    else if(x%3==2)
    {
        int ns=x/3+1;
        int min=ns-1;
        if(min>=0&&ns>=p)
            return 1;
        else
        {
            int s=x/3+2;
            int min=s-2;
            if(min>=0&&s>=p)
                return 2;
            else
                return 0;
        }
    }
}
int main()
{
    int cs;
    freopen("B-large.in","r",stdin);
    freopen("outBL.txt","w",stdout);
    scanf("%d",&cs);
    int cnt=1;
    int tt=0;
    while(cs--)
    {
        int n,s,p;
        scanf("%d%d%d",&n,&s,&p);
        for(int i=0;i<n;i++)
            scanf("%d",&g[i]);
        int needs=0;
        int cnt=0;
        for(int i=0;i<n;i++)
        {
            int ans=judge(g[i],p);//printf("%d\n",ans);
            if(ans==1)
                cnt++;
            else if(ans==2)
                needs++;
        }
        if(needs>s)
            needs=s;
        printf("Case #%d: %d\n",++tt,cnt+needs);
    }
    return 0;
}
