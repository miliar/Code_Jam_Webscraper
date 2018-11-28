#include<cstdio>
#include<algorithm>
#define min(a,b) (a<b?a:b)
#define max(a,b) (a>b?a:b)
#define INF (1<<29)
using namespace std;
int initreq[1050];
int p;
int inp[11][1050];
void recfunc(int at,int lvl,int retreq[11])
{
  //cost = inp[lvl][at]
   int req1[11],req2[11],i,j;
   int curm;
   for(i=0;i<=10;i++)
   retreq[i]=INF;
   if(lvl==p)
   {
      
      retreq[initreq[at]]=0;
      if(initreq[at]>0)
      retreq[initreq[at]-1]=inp[lvl][at];
   }
   else
   {
       recfunc(2*at-1,lvl+1,req1);
       recfunc(2*at,lvl+1,req2);
       for(i=0;i<=10;i++)
       {
         for(j=0;j<=10;j++)
         {
            curm=max(i,j);
            if(req1[i]+req2[j]<retreq[curm])
            retreq[curm]=req1[i]+req2[j];
         }
       }
       for(i=1;i<=10;i++)
       {
         curm=inp[lvl][at]+retreq[i];
         if(curm<retreq[i-1])
         retreq[i-1]=curm;
       }
   }
}
int main()
{
  int t,tit;
  int i,j;
  int tmp1,tmp2;
  int tmpar[11];
  scanf("%d",&t);
  for(tit=1;tit<=t;tit++)
  {
    scanf("%d",&p);
    p--;
    for(i=1;i<=(1<<p);i++)
    {
      scanf("%d%d",&tmp1,&tmp2);
      tmp1 = min(tmp1,tmp2);
      initreq[i] = p+1-tmp1;
      
    }
    for(i=p;i>=0;i--)
    {
      for(j=1;j<=(1<<i);j++)
      {
        scanf("%d",&inp[i][j]);
      }
    }
    recfunc(1,0,tmpar);
    printf("Case #%d: %d\n",tit,tmpar[0]);
  }
  return 0;
}
