#include <cstdio>
#include <cstring>
using namespace std;
int s[35],ns[35],f[100][101],t[101],ans;
inline int min(int a,int b)
{
    return (a>b)?b:a;
}
void init()
{
    int a,b,c;
    memset(s,0,sizeof(s));
    memset(ns,0,sizeof(ns));
    for(a=0;a<=10;a++)
    {
        for(b=a;b<=10;b++)
        {
            for(c=b;c<=10;c++)
            {
                if (c-b<=2 && c-a<=2 && b-a<=2)
                {
                    if (b-a==2 || c-b==2 || c-a==2)
                    {
                        if(c>s[a+b+c])
                            s[a+b+c]=c;
                    }
                    else if (c>ns[a+b+c])
                        ns[a+b+c]=c;
                }
            }
        }
    }
}
void solve(int n,int ss,int p)
{
    int max;
    memset(f,0,sizeof(f));
    for(int i=1;i<=n;i++)
    {
        if (ns[t[i]]>=p)
            f[i][0]=f[i-1][0]+1;
        else
            f[i][0]=f[i-1][0];
    }
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=min(i,ss);j++)
        {
            if (i==j)
            {
                if (s[t[i]]>=p)
                    f[i][j]=f[i-1][j-1]+1;
                else
                    f[i][j]=f[i-1][j-1];
            }
            else
            {
                if (ns[t[i]]>=p)
                    max=f[i-1][j]+1;
                else
                    max=f[i-1][j];
                if (s[t[i]]>=p)
                {
                    if (f[i-1][j-1]+1>max)
                        max=f[i-1][j-1]+1;
                }
                else
                {
                    if (f[i-1][j-1]>max)
                        max=f[i-1][j-1];
                }
                f[i][j]=max;
            }
        }
    }
    ans=f[n][ss];
}

int main()
{
    int n,s,p,tt;
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    init();
    scanf("%d",&tt);
    for(int i=1;i<=tt;i++)
    {
        scanf("%d%d%d",&n,&s,&p);
        for(int j=1;j<=n;j++)
        {
            scanf("%d",&t[j]);
        }
        solve(n,s,p);
        printf("Case #%d: %d\n",i,ans);
    }
    return 0;
}
