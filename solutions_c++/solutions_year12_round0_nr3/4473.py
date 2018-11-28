#include<cstdio>
int s[4],t[4];
int solve(int x,int a[])
{
    int len=0;
    for (;x;x/=10,len++)
        a[len]=x%10;
    return len;
}
bool check(int a,int b)
{
    int la=solve(a,s),lb=solve(b,t);
    if (la!=lb)
        return 0;
    for (int i=0;i<la;i++)
    {
        bool flag=1;
        for (int j=0;j<la && flag;j++)
            if (s[j]!=t[(i+j)%la])
                flag=0;
        if (flag)
            return 1;
    }
    return 0;
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for (int cas=1;cas<=t;cas++)
    {
        int a,b;
        scanf("%d%d",&a,&b);
        int ans=0;
        for (int i=a;i<=b;i++)
            for (int j=i+1;j<=b;j++)
                if (check(i,j))
                    ans++;
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
