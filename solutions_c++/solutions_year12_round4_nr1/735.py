#include<stdio.h>
#include<stdlib.h>
#define INF 1999999999
int T;
int n;
int a[10111],b[10111],c[10111];
int min(int aa,int bb,int cc)
{
  int k=INF;
  if(k>aa)k=aa;
  if(k>bb)k=bb;
  if(k>cc)k=cc;
  return k;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int i,j,k;
    int p,q,r;
    int yes;
    scanf("%d",&T);
    for(int ii=0;ii<T;ii++)
     {
       scanf("%d",&n);
       for(i=1;i<=n;i++)
        {
          scanf("%d %d",&a[i],&b[i]);
          c[i]=-INF;
        }
       scanf("%d",&r);
       a[n+1]=r;
       b[n+1]=INF;
       c[n+1]=-INF;
       
       c[1]=a[1];
       for(i=1;i<=n;i++)
        {
          p=c[i];
          k=c[i]+a[i];
          for(j=i+1;j<=n+1;j++)
           {
          //   printf(">> %d %d\n",a[j],k);
             if(a[j]<=k)
              {
                 if(c[j]==-INF)c[j]=min(b[j],a[j]-a[i],INF);
                 else 
                  {
                    q=min(b[j],a[j]-a[i],INF);
                    if(q>c[j])c[j]=q;
                  }
              }
             else break;
           }
        }
       //for(i=1;i<=n+1;i++)printf("%d %d\n",i,c[i]);
       //printf("\n\n");
       if(c[n+1]==-INF)yes=0;
       else yes=1;
       printf("Case #%d: ",ii+1);
       if(yes==1)printf("YES");
       else printf("NO");
       if(ii<T-1)printf("\n");
     }
    
    scanf(" ");
    return 0;
}
