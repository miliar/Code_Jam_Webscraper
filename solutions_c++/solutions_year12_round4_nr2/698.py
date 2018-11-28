#include <stdio.h>
#include <stdlib.h>
int t,n,tests;
long long xi[1001];
long long yi[1001];
int ri[1001];
long long w,l;
long long ret()
{
 long long tmp1,tmp2,tmp3;
 long long ret1,ret2,ret3;
 tmp1=rand();
 tmp2=rand();
 tmp3=rand();
 ret1=tmp1*tmp2*tmp3;
 tmp1=rand();
  tmp2=rand();
 ret2=tmp1*tmp2;
  tmp1=rand();
 ret3=tmp1;
 return ret1+ret2+ret3;
}
bool chk2(int a,int b)
{
 long long ww,ll,rr;
 ww=xi[a]-xi[b];
 ll=yi[a]-yi[b];
 ww=ww*ww;
 ll=ll*ll;
 rr=ri[a]+ri[b];
 rr=rr*rr;
 //printf("%d %d\n",a,b);
//printf("%I64d %I64d | %I64d %I64d\n",xi[a],yi[a],xi[b],yi[b]);
 //printf("%I64d %I64d | %I64d\n",ww,ll,rr);
 if(ww+ll>=rr){return true;}
 else{return false;}
}
bool chk()
{
 for(int i=1;i<=n;i++)
 {
  for(int j=i+1;j<=n;j++)
  {
   if(chk2(i,j)==false){return false;}
  }
 }
 return true;
}
main()
{
 freopen("B-small-attempt0.in","r",stdin);
 freopen("B-small-attempt0.out","w",stdout);
 scanf("%d",&t);
 for(int tests=1;tests<=t;tests++)
 {
  printf("Case #%d:",tests);
  scanf("%d",&n);
  scanf("%I64d%I64d",&w,&l);
  for(int i=1;i<=n;i++)
  {
   scanf("%d",&ri[i]);
  }
  do
  {
   for(int i=1;i<=n;i++)
   {
   xi[i]=ret()%w;
   yi[i]=ret()%l;
   }
  }
  while(!chk());
  for(int i=1;i<=n;i++)
  {
   printf(" %I64d.0 %I64d.0",xi[i],yi[i]);
  }
  printf("\n");
 }
 return 0;
}
