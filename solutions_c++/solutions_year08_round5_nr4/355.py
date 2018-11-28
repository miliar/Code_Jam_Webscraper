#include<stdio.h>
#include<string.h>

const int mod=10007;
const int maxn=128;
bool g[maxn][maxn];
int row,col;
int ans[maxn][maxn];
void input()
{
    int i,n,t1,t2;
    scanf("%d%d",&row,&col);
    scanf("%d",&n);
    memset(g,0,sizeof(g));
    for(i=0;i<n;i++){
        scanf("%d%d",&t1,&t2);
        g[t1][t2]=true;
    }
}

int solve()
{
    int i,j,x,y;
    memset(ans,0,sizeof(ans));
    for(i=1;i<=row;i++){
        for(j=1;j<=col;j++){
            ans[i][j]=0;
            if(i==1 && j==1) ans[i][j]=1;
            x=i-1, y=j-2;
            if(x>0 && y>0){
                ans[i][j]+=ans[x][y];
            }
            x=i-2, y=j-1;
            if(x>0 && y>0){
                ans[i][j]+=ans[x][y];
            }
            ans[i][j]%=mod;
            if(g[i][j]) ans[i][j]=0;
            //printf("%d\n",ans[i][j]);
        }
    }
    return ans[row][col];
}

int main()
{
    int i,T;
    freopen("D-small-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&T);
    for(i=1;i<=T;i++){
        input();
        printf("Case #%d: %d\n",i,solve());
    }
    return 0;
}
