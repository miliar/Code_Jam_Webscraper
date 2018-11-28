#include<iostream>
using namespace std;
const int maxn=110;
int modu= 10007;
int t,test,l1,l2,n,v[maxn][maxn],f[maxn][maxn];
void init()
{
     int i,x,y;
     scanf("%d%d%d",&l1,&l2,&n);
     memset(v,0,sizeof(v));
     for (i=0;i<n;i++)
     {
         scanf("%d%d",&x,&y);
         v[x][y]=1;
     }
}

int get(int x,int y)
{
    if (x<1) return 0;
    if (y<1) return 0;
    return f[x][y];
}

void work()
{
     int i,j;
     memset(f,0,sizeof(f));
     f[1][1]=1;
     for (i=2;i<=l1;i++)
         for (j=2;j<=l2;j++) 
         if (!v[i][j]) f[i][j]=(get(i-2,j-1)+get(i-1,j-2))%modu;
}

void print()
{
     printf("Case #%d: %d\n",t,f[l1][l2]);
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
