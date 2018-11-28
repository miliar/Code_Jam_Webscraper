#include<iostream>
using namespace std;
const int maxn=110;
int a[maxn][maxn],t,test,ans,n,m,x1,y1,x2,y2,sx,sy;
void init()
{
     scanf("%d%d",&n,&m);
     scanf("%d%d",&x1,&y1);
     scanf("%d%d",&x2,&y2);
     scanf("%d%d",&sx,&sy);     
}

int outside(int xx,int yy)
{
    if (xx<0) return 1;
    if (yy<0) return 1;
    if (xx>=n) return 1;
    if (yy>=m) return 1;
    return 0;
}

void go(int xx,int yy)
{
     if (outside(xx,yy)) return;
     if (a[xx][yy]) return;
     ans++;
     a[xx][yy]=1;
     go(xx+x1,yy+y1);
     go(xx+x2,yy+y2);
}

void work()
{
     memset(a,0,sizeof(a));
     ans=0;
     go(sx,sy);
}

void print()
{
     printf("Case #%d: %d\n",t,ans);
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    for (scanf("%d",&test),t=1;t<=test;t++)
    {
        init();
        work();
        print();
    }
    return 0;
}
