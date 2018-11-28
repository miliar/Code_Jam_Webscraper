#include<iostream>
#define maxn 110
#define maxkk 30
int price[maxn][maxkk],link[maxn];
bool map[maxn][maxn],cover[maxn];
int l,t,n,kk,i,j,ans;

bool ok(int x,int y)
{
    for(int i=1;i<=kk;++i)
      if(price[x][i]<=price[y][i])return false;
    return true;
}

bool find(int s)
{
    for(int i=1;i<=n;++i)if((map[s][i])&&(!cover[i]))
    {
        int p=link[i];link[i]=s;cover[i]=true;
        if((p==0)||(find(p)))return true;
        link[i]=p;
    }
    return false;
}

int main()
{
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    scanf("%d",&t);
    for(l=1;l<=t;++l)
    {
        scanf("%d%d",&n,&kk);
        for(i=1;i<=n;++i)
            for(j=1;j<=kk;++j)
                scanf("%d",&price[i][j]);
        for(i=1;i<=n;++i)
            for(j=1;j<=n;++j)map[i][j]=ok(i,j);
        for(i=1;i<=n;++i)link[i]=0;
        ans=n;
        for(i=1;i<=n;++i)
        {
            for(j=1;j<=n;++j)cover[j]=false;
            if(find(i))--ans;
        }
        printf("Case #%d: %d\n",l,ans);
    }
    return 0;
}
