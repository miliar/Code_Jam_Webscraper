#include <stdio.h>
#include <stdlib.h>
int t;
int n;
int runs;
int spruns;
int sp;
int len;
int st[1001];
int ed[1001];
int ww[1001];
int A[1000001];
double ans;
double have;
double want;
double t1,t2,t3,t5;
double can;
double utime;
int t4;
main()
{
 freopen("A-large.in","r",stdin);
 freopen("A-large.out","w",stdout);
 scanf("%d",&t);
 for(int i=1;i<=t;i++)
 {
  scanf("%d%d%d%d%d",&len,&sp,&spruns,&runs,&n);
  ans=0;
  for(int j=1;j<=1000;j++)
  {
   A[j]=0;
  }
  A[sp]=len;
  for(int j=1;j<=n;j++)
  {
   scanf("%d%d%d",&st[j],&ed[j],&ww[j]);
   A[sp]-=ed[j]-st[j];
   A[sp+ww[j]]+=ed[j]-st[j];
  }
  have=runs;
  for(int j=1;j<=1000;j++)
  {
   if(A[j]>0)
   {
    t4=spruns-sp+j;
    t3=t4;
    t4=j;
    t5=t4;
    //t5 normal t3 run
    t2=have*t3;
    t1=A[j];
    if(t2>t1)
    {
     utime=t1/t3;
     have-=utime;
     ans+=utime;
    }
    else if(t2>0)
    {
     have=0;
     utime=t2/t3;
     ans+=utime;
     t1-=t2;
     utime=t1/t5;
     ans+=utime;
    }
    else
    {
     utime=t1/t5;
     ans+=utime;
    }
   }
  }
  printf("Case #%d: %.10lf\n",i,ans);
 }
 return 0;
}
