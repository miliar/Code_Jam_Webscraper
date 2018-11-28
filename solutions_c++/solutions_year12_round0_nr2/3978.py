#include<cstdio>
int a[50];
int test(int n,bool s)
{
    if(!s)
    {
        return (n+2)/3;
    }
    else
    {
        if(n==0)
        {
            return 0;
        }
        if(n==1)
        {
            return 1;
        }
        return (n+4)/3;
    }
}
int main()
{
    int t;
    scanf("%d",&t);
    for(int c=1; c<=t; ++c)
    {
        int n,s,p;
        scanf("%d%d%d",&n,&s,&p);
        for(int i=0; i<n; ++i)
        {
            scanf("%d",&a[i]);
        }
        int ans=0,sp=0;
        for(int i=0; i<n; ++i)
        {
            if(test(a[i],false)>=p)
            {
                ++ans;
            }
            else if(test(a[i],true)>=p)
            {
                if(sp<s)
                {
                    ++ans;
                    ++sp;
                }
            }
        }
        printf("Case #%d: %d\n",c,ans);
    }
    return 0;
}
