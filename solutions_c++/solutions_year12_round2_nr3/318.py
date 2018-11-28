#include <cstdio>
#include <cmath>
using namespace std;

bool dfs(int a[],int as,int at,int b[],int bs,int bt,int s[],int i,int ss)
{
     if (i<ss)
     {
        if (at==bt&&at!=0)
        {
           for (int i=0;i<as;i++)
               printf("%d%c",a[i],i+1==as?'\n':' ');
           for (int i=0;i<bs;i++)
               printf("%d%c",b[i],i+1==bs?'\n':' ');
           return true;
        }
        if (dfs(a,as,at,b,bs,bt,s,i+1,ss)) return true;
        a[as]=s[i];
        if (dfs(a,as+1,at+a[as],b,bs,bt,s,i+1,ss)) return true;
        b[bs]=s[i];
        if (dfs(a,as,at,b,bs+1,bt+b[bs],s,i+1,ss)) return true;
     }
     return false;
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for (int t=1;t<=T;t++)
    {
        int N;
        scanf("%d",&N);
        int s[N];
        for (int i=0;i<N;i++) scanf("%d",&s[i]);
        printf("Case #%d:\n",t);
        int a[N],b[N];
        dfs(a,0,0,b,0,0,s,0,N);
    }
}
