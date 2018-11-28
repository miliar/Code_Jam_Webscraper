#include <iostream>
#define maxl 102
int a[maxl][maxl],s[maxl*maxl],o[maxl*maxl],b,c,d,e,n,m,tt,t;
void reans(int i,int j)
{
     if (a[i][j]<a[d][e])
     {
                       d=i;
                       e=j;
     }
}
int ss(int i,int j)
{
    return ((i-1)*m+j);
}
int find(int i)
{
    int x,y;
    x=i;
    while (s[x]!=x) x=s[x];
    while (i!=x)
    {
          y=s[i];
          s[i]=x;
          i=y;
    }
    return x;
}
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d\n",&tt);
    for (b=0;b<maxl;b++)
    {
        a[0][b]=1000000;
        a[b][0]=1000000;
    }
    for (t=1;t<=tt;t++)
    {
        scanf("%d %d\n",&n,&m);
        for (b=1;b<=n;b++)
        {
            for (c=1;c<m;c++)
              scanf("%d ",&a[b][c]);
            scanf("%d\n",&a[b][c]);
        }
        for (b=1;b<=n+1;b++)
          a[b][m+1]=1000000;
        for (c=1;c<=m+1;c++)
          a[n+1][c]=1000000;
        for (b=1;b<=n*m;b++) s[b]=b;
        memset(o,0,sizeof(int)*maxl*maxl);
        for (b=1;b<=n;b++)
          for (c=1;c<=m;c++)
          {
              d=b-1;e=c;
              reans(b,c-1);
              reans(b,c+1);
              reans(b+1,c);
              if (a[d][e]<a[b][c]) s[find(ss(b,c))]=find(ss(d,e));
          }
        e=0;
        printf("Case #%d:\n",t);
        for (b=1;b<=n;b++)
          for (c=1;c<=m;c++)
          {
              d=find(ss(b,c));
              if (o[d]==0)
              {
                                      e++;
                                      o[d]=e;
              }
              printf("%c",o[d]+'a'-1);
              if (c==m) printf("\n");
                   else printf(" ");
          }  
    }
}
