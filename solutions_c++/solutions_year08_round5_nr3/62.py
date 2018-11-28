#include<iostream>
using namespace std;
const int maxn=10;
const int maxd=1<<maxn;
int s[maxd],f[2][maxd],a[maxn],n,m,t,test,ans;
void prepare()
{
     int i;
     for (i=1;i<maxd;i++) s[i]=s[i/2]+(i&1);
}


void init()
{
     scanf("%d%d\n",&n,&m);
     int i,j;
     char ch;
     for (i=0;i<n;i++)
     {
         a[i]=0;
         for (j=0;j<m;j++)
         {
             a[i]<<=1;
             scanf("%c",&ch);
             if (ch=='x') a[i]+=1;
         }
         scanf("\n");
     }                    
     m=1<<m;
}

void work()
{
     memset(f[0],0,sizeof(f[0]));
     int i,j,k,l;
     for (i=0;i<m;i++)
     if ((i&(i/2))==0)
        if ((i&a[0])==0) f[0][i]=s[i];
     for (l=0,i=1;i<n;i++)
     {
         l=1-l;
         memset(f[l],0,sizeof(f[l]));
         for (j=0;j<m;j++)
         if ((j&(j/2))==0)
            if ((j&a[i])==0)
               for (k=0;k<m;k++)
               if (((j*2)&k)==0)
                  if (((j/2)&k)==0) 
                  f[l][j]>?=s[j]+f[1-l][k];
     }
     for (ans=0,i=0;i<m;i++) ans>?=f[l][i];
}

void print()
{
     printf("Case #%d: %d\n",t,ans);
}

int main()
{
    prepare();
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    for (scanf("%d\n",&test),t=1;t<=test;t++)
    {
        init();
        work();
        print();
    }
    return 0;
}
