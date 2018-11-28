#include<cstdio>
#include<cstring>
bool g[102][102],flag[102];
int n,k;
int num[102][30],y[102];
bool Check(int i,int j)
{
    for(int x=0;x<k;x++)
        if(num[i][x]<=num[j][x])
            return false;
    return true;
}
bool Path(int s)
{
    for(int i=0;i<n;i++)
    {
        if(!flag[i]&&g[s][i])
        {
            flag[i]=1;
            if(y[i]==-1||Path(y[i]))
            {
                y[i]=s;
                return true;
            }
        }
    }
    return false;
}
int Max_Match()
{
    int ans=0;
    memset(y,-1,sizeof(y));
    for(int i=0;i<n;i++)
    {
        memset(flag,0,sizeof(flag));
        if(Path(i))ans++;
    }
    return ans;
}
int main()
{
    freopen("c:\\C-large.in","r",stdin);
    freopen("c:\\c.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int ii=1;ii<=t;ii++)
    {
        scanf("%d%d",&n,&k);
        for(int i=0;i<n;i++)
            for(int j=0;j<k;j++)
                scanf("%d",&num[i][j]);
        memset(g,0,sizeof(g));
        for(int i=0;i<n;i++)
            for(int j=0;j<n;j++)
                if(Check(i,j))
                    g[i][j]=1;
        printf("Case #%d: %d\n",ii,n-Max_Match());
    }
    return 0;
}

