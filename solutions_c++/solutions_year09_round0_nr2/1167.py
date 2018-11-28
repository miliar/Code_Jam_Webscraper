#include<cstdio>
#include<cstring>
#include<cstdlib>
#define MAXH 110
#define MAXW 110
int T;
int H,W;
int a[MAXH][MAXW];
int CaseNum;
int dir[4][2]={{-1,0},{0,-1},{0,1},{1,0}};
int last[MAXH][MAXW][2];
char ans[MAXH][MAXW];
void init()
{
    memset(a,0,sizeof(a));
    memset(ans,0,sizeof(ans));
    memset(last,0,sizeof(last));
    scanf("%d%d",&H,&W);
    int i,j;
    for (i=1;i<=H;i++)
        for (j=1;j<=W;j++)
            scanf("%d",&a[i][j]);
}
inline bool check(int x,int y)
{
    if (x>0&&x<=H&&y>0&&y<=W)return true;
    else return false;
}
void getlast(int I,int J)
{
    int i,x,y,x0=I,y0=J,X,Y;
    int MIN;
    for (;;)
    {
        MIN=1000000;
        for (i=0;i<4;i++)
        {
            x=x0+dir[i][0];y=y0+dir[i][1];
            if (check(x,y)&&a[x][y]<MIN&&a[x][y]<a[x0][y0])
            {
                MIN=a[x][y];
                X=x;Y=y;
            }
        }
        if (MIN==1000000)
        {
            X=x0;Y=y0;
            break;
        }
        x0=X;y0=Y;
    }
    last[I][J][0]=X;
    last[I][J][1]=Y;
}
void solve()
{
    int i,j;
    char now;
    for (i=1;i<=H;i++)
        for (j=1;j<=W;j++)getlast(i,j);
    now='a'-1;
    for (i=1;i<=H;i++)
        for (j=1;j<=W;j++)
        if (ans[last[i][j][0]][last[i][j][1]])ans[i][j]=ans[last[i][j][0]][last[i][j][1]];
        else
        {
            now++;
            ans[i][j]=now;
            ans[last[i][j][0]][last[i][j][1]]=now;
        }
}
void print()
{
    CaseNum++;
    printf("Case #%d:\n",CaseNum);
    int i,j;
    for (i=1;i<=H;i++)
    {
        for (j=1;j<W;j++)printf("%c ",ans[i][j]);
        printf("%c\n",ans[i][W]);
    }
}
int main()
{
//    freopen("B-large.in","r",stdin);
//    freopen("B-large.out","w",stdout);
    scanf("%d",&T);
    int i;
    for (i=1;i<=T;i++)
    {
        init();
        solve();
        print();
    }
    return 0;
}
