#include<iostream>
using namespace std;
const int maxn=16;
int ans,f[2][1<<maxn],a[maxn][maxn],n,m,test,t;
void init()
{
     int i,j;
     scanf("%d%d\n",&n,&m);
     for (i=0;i<n;i++)
     {
         for (j=0;j<m;j++) scanf("%c",&a[i][j]);
         scanf("\n");
     }
}

void work()
{
     memset(f[0],-1,sizeof(f[0]));
     f[0][0]=0;
     int i,j,k,l,x,now;
     now=0;
     for (i=0;i<n;i++)
         for (j=0;j<m;j++)
         {
             now=1-now;
             memset(f[now],-1,sizeof(f[now]));
             for (k=0;k<(1<<m);k++)
             if (f[1-now][k]!=-1)
             {
                 x=4;
                 if (k&(1<<(m-1))) x-=2;
                 if ((j!=0)&&(k&1)) x-=2;
                 l=(k*2)%(1<<m);
                 if (a[i][j]!='.') f[now][l+1]>?=f[1-now][k]+x;
                 if (a[i][j]!='#') f[now][l]>?=f[1-now][k];
             }
         }
     ans=-1;
     for (i=0;i<(1<<m);i++) ans>?=f[now][i];
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
