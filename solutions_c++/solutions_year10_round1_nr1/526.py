#include<stdio.h>
#include<string.h>
char map[2][101][101];
int n,k;
void out(int x)
{
    puts("");
    for (int i=1;i<=n;i++)
            puts(map[x][i]+1);
        puts("");
}
bool row(int x,int y,char r)
{
    int j;
    for (j=1;j<k && y+j<=n;j++)
        if (map[1][x][y+j]!=r) break;
    return j==k;
}
bool col(int x,int y,char r)
{
    int i;
    for (i=1;i<k && x+i<=n;i++)
        if (map[1][x+i][y]!=r) break;
    return i==k;
}
bool diag1(int x,int y,char r)
{
    int j;
    for (j=1;j<k && y+j<=n && x+j<=n;j++)
        if (map[1][x+j][y+j]!=r) break;
    return j==k;
}
bool diag2(int x,int y,char r)
{
    int j;
    for (j=1;j<k && y-j>=1 && x+j<=n;j++)
        if (map[1][x+j][y-j]!=r) break;
    return j==k;
}

int main()
{
    int index,t;
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&t);
    for (index=1;index<=t;index++)
    {
        scanf("%d%d",&n,&k);
        //if (index==10) printf("%d%d\n",n,k);
        memset(map,0,sizeof(map));
        for (int i=1;i<=n;i++)
            scanf("%s",map[0][i]+1);
        //if (index==10) out(0);
        for (int i=n;i>=1;i--)
            for (int j=1;j<=n;j++)
                map[1][j][n-i+1]=map[0][i][j];
        //if (index==10) out(1);
        for (int i=n-1;i>=1;i--)
            for (int j=1;j<=n;j++)
                if (map[1][i][j]!='.')
                {
                    int p;
                    for (p=i;p<n && map[1][p+1][j]=='.';p++);
                    map[1][p][j]=map[1][i][j];
                    if (p!=i) map[1][i][j]='.';
                }  
        //if (index==10) out(1);
        bool winb,winr;
        winb=winr=false;
        for (int i=1;i<=n;i++)
            for (int j=1;j<=n;j++)
                if (map[1][i][j]!='.')
                    if (map[1][i][j]=='R')
                        winr=winr || row(i,j,'R') || col(i,j,'R') 
                                  || diag1(i,j,'R') || diag2(i,j,'R');
                    else
                        winb=winb || row(i,j,'B') || col(i,j,'B') 
                                  || diag1(i,j,'B') || diag2(i,j,'B');
        if (winb && !winr) printf("Case #%d: Blue\n",index);
        if (!winb && winr) printf("Case #%d: Red\n",index);
        if (winb && winr) printf("Case #%d: Both\n",index);
        if (!winb && !winr) printf("Case #%d: Neither\n",index);
    }
}
