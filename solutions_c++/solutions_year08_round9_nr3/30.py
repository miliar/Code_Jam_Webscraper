#include<iostream>
using namespace std;
const int maxn=10;
int n,m,t,test,a[maxn][maxn],b[maxn][maxn],ans;
void init()
{
     scanf("%d%d",&n,&m);
     int i,j;
     for (i=0;i<n;i++)
         for (j=0;j<m;j++) scanf("%d",&a[i][j]);     
}

int get(int x,int y)
{
    if (x<0) return 0;
    if (x>=n) return 0;
    if (y<0) return 0;
    if (y>=m) return 0;
    return b[x][y];
}

void complete()
{
     int i,j,k,l,x;
     for (i=0;i<n-1;i++)
         for (j=0;j<m-1;j++)
         {
             b[i+1][j+1]=a[i][j];
             for (k=-1;k<2;k++)
                 for (l=-1;l<2;l++)
                 if (k+l!=2)
                 b[i+1][j+1]-=get(i+k,l+j);
             if (b[i+1][j+1]<0) return;
             if (b[i+1][j+1]>1) return;
         }
     for (i=0;i<n;i++)
         for (j=0;j<m;j++)
         {
             x=0;
             for (k=-1;k<2;k++)
                 for (l=-1;l<2;l++)
                 x+=get(i+k,l+j);
             if (x!=a[i][j]) return;
         }  
     j=0;
     for (i=0;i<m;i++) j+=b[n/2][i];
     ans>?=j;
}

void work()
{
     ans=0;
     int i,j,k,l;
     for (i=0;i<(1<<m);i++)
         for (j=0;j<(1<<(n-1));j++)
         {
             memset(b,0,sizeof(b));
             for (k=0;k<m;k++)
             if (i&(1<<k)) b[0][k]=1;
             for (k=0;k<n-1;k++)
             if (j&(1<<k)) b[k+1][0]=1;
             complete();
         }
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
