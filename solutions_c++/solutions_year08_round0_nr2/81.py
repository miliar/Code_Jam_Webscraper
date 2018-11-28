#include<cstdio>
#include<cstring>
int n,n1,n2,t,t1s[100],t1a[100],t2s[100],t2a[100];
bool b[200],g[200][200];
int lk[200];
int ans1,ans2;
bool find(int v)
{
    for(int i=0; i<n; i++)
    if(g[v][i] && !b[i])
    {
        b[i]=1;
        if(lk[i]==-1 || find(lk[i]))
        {
            lk[i]=v;
            return 1;
        }
    }
    return 0;
}
int main()
{
    int p,x,y;
    scanf("%d",&p);
    for(int _=1; _<=p; _++)
    {
        scanf("%d%d%d",&t,&n1,&n2);
        n=n1+n2;
        for(int i=0; i<n1; i++)
        {
            scanf("%d%*c%d",&x,&y);
            t1s[i]=x*60+y;
            scanf("%d%*c%d",&x,&y);
            t1a[i]=x*60+y;
        }
        for(int i=0; i<n2; i++)
        {
            scanf("%d%*c%d",&x,&y);
            t2s[i]=x*60+y;
            scanf("%d%*c%d",&x,&y);
            t2a[i]=x*60+y;
        }
        memset(g,0,sizeof(g));
        memset(lk,-1,sizeof(lk));
        for(int i=0; i<n1; i++)
        for(int j=0; j<n2; j++)
        if(t1a[i]+t<=t2s[j])
        g[i][j+n1]=1;
        else if(t2a[j]+t<=t1s[i])
        g[j+n1][i]=1;
        for(int i=0; i<n; i++)
        {
            memset(b,0,sizeof(b));
            find(i);
        }
        ans1=n1,ans2=n2;
        for(int i=0; i<n1; i++)
        if(lk[i]!=-1)
        ans1--;
        for(int i=n1; i<n; i++)
        if(lk[i]!=-1)
        ans2--;
        printf("Case #%d: %d %d\n",_,ans1,ans2);
    }
    return 0;
}
