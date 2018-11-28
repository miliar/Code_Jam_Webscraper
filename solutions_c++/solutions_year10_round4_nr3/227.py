#include<iostream>
using namespace std;
const int maxn=110;
int a[maxn][maxn],b[maxn][maxn];
int n=105;
int tt,ans,cases;
void init()
{
     int i,x1,x2,y1,y2,j,k;
     memset(a,0,sizeof(a));
     for (scanf("%d",&k);k;k--)
     {
         scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
         for (i=x1;i<=x2;i++)
             for (j=y1;j<=y2;j++)
                 a[j][i]=1;
     }
}

void work()
{
     ans=0;
     int i,j,k;
     while (1)
     {
           k=0;
           for (i=0;i<=n;i++)
               for (j=0;j<=n;j++)
               k+=a[i][j];
           if (!k) break;
           ans++;
           for (i=1;i<=n;i++)
               for (j=1;j<=n;j++)
               {
                   b[i][j]=a[i][j];
                   k=a[i-1][j]+a[i][j-1];
                   if (k==2) b[i][j]=1;
                   if (k==0) b[i][j]=0;
               }
           memcpy(a,b,sizeof(b));
     }
}

void print()
{
     printf("Case #%d: %d\n",tt+1,ans);
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    for (scanf("%d",&cases),tt=0;tt<cases;tt++)
    {
        init();
        work();
        print();
    }
    return 0;
}
