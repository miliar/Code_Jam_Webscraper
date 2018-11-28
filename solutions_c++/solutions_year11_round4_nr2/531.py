#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int MAXN=510;

int n,m,d;
char str[MAXN][MAXN];
int map[MAXN][MAXN];
int sum[MAXN][MAXN],isum[MAXN][MAXN],jsum[MAXN][MAXN];

bool check(int x,int y,int size)
{
    double ansx=0,ansy=0;
    double midx=x-(size-1)/2.0,midy=y-(size-1)/2.0;
    ansx=isum[x][y]-isum[x-size][y]-isum[x][y-size]+isum[x-size][y-size];
    ansx-=midx*(sum[x][y]-sum[x-size][y]-sum[x][y-size]+sum[x-size][y-size]);
    ansy=jsum[x][y]-jsum[x-size][y]-jsum[x][y-size]+jsum[x-size][y-size];
    ansy-=midy*(sum[x][y]-sum[x-size][y]-sum[x][y-size]+sum[x-size][y-size]);

    ansx-=(x-size+1-midx)*map[x-size+1][y-size+1],ansy-=(y-size+1-midy)*map[x-size+1][y-size+1];
    ansx-=(x-midx)*map[x][y],ansy-=(y-midy)*map[x][y];
    ansx-=(x-size+1-midx)*map[x-size+1][y],ansy-=(y-midy)*map[x-size+1][y];
    ansx-=(x-midx)*map[x][y-size+1],ansy-=(y-size+1-midy)*map[x][y-size+1];
    return (ansx==0&&ansy==0);
}

int solve()
{
    for(int k=min(n,m);k>=3;--k)
    {
        for(int i=k;i<=n;++i)
            for(int j=k;j<=m;++j)
                if(check(i,j,k))return k;
    }
    return -1;
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,cases=1;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d%d",&n,&m,&d);
        for(int i=0;i<n;++i)
        scanf("%s",str[i]);
        for(int i=1;i<=n;++i)
        for(int j=1;j<=m;++j)
        map[i][j]=(str[i-1][j-1]-'0');
        memset(sum,0,sizeof(sum));
        memset(isum,0,sizeof(isum));
        memset(jsum,0,sizeof(jsum));
        for(int i=1;i<=n;++i)
            for(int j=1;j<=m;++j)
            {
                sum[i][j]+=sum[i-1][j]+sum[i][j-1]-sum[i-1][j-1]+map[i][j];
                isum[i][j]+=isum[i-1][j]+isum[i][j-1]-isum[i-1][j-1]+i*map[i][j];
                jsum[i][j]+=jsum[i-1][j]+jsum[i][j-1]-jsum[i-1][j-1]+j*map[i][j];
            }
//        for(int i=1;i<=n;++i)
//        {
//            for(int j=1;j<=m;++j)
//            cout<<isum[i][j]<<" ";
//            cout<<endl;
//        }
        int tem=solve();
        if(tem==-1)printf("Case #%d: IMPOSSIBLE\n",cases++);
        else printf("Case #%d: %d\n",cases++,tem);
    }
    return 0;
}
