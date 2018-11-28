#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>
#include<math.h>




#define FOR(i,s,n) for(int i=(s);i<(n);i++)
#define FORE(i,s,n) for(int i=(s);i<=(n);i++)

#define GETU(i) scanf("%u",&i)
#define GETI(i) scanf("%d",&i)
#define GETW(s) scanf("%s",s)
#define GETS(s) gets(s)
#define llu unsigned long long

#define surp 1
#define error 0
#define ki 2

int MAX(int a,int b)
{
  if(a>b)
    return a;
  return b;
}

int MIN(int a,int b)
{
  if(a<b)
    return a;
  return b;
}
int cheack(int ar[3])
{
  if( ar[0]<0 || ar[1]<0 || ar[2]<0 ||  ar[0]>10 || ar[1]>10 || ar[2]>10 )
    return error;

  int min=MIN(MIN(ar[0],ar[1]),ar[2]);
  int max=MAX(MAX(ar[0],ar[1]),ar[2]);
  int minus=max-min;

  if(minus>2)
    return error;

  if(minus==2)
    return surp;

  return ki;

}

int solve()
{
  int n,s,p;
  int total;
  int ex[3];
  int surpp=0,kii=0;

  GETI(n);
  GETI(s);
  GETI(p);


  FOR(i,0,n)
  {
    int suki=0,kiki=0;
    GETI(total);

    FORE(j,p,total)
    {
      const int minu=(total-j);
      ex[0]=j;
      ex[1]=ex[2]=(minu)/2;
      ex[2]+=minu%2;

      int res=cheack(ex);
      if(res==ki)
        {
          kiki=1;
          break;
        }
       if(res==surp)
        suki=1;
    }


    if(kiki==1)
      kii++;
    else if(suki==1)
      surpp++;
  }


  kii+=MIN(s,surpp);


  return kii;

}

int main()
{
#define contest
#undef contest


#ifndef contest
  freopen("B-large.in","r",stdin);
 freopen("B-large.out","w",stdout);
#endif
  int t;
  GETI(t);
  FORE(tc,1,t)
  {
    printf("Case #%d: %d\n",tc,solve());
  }

  return 0;
}