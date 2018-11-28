#include<cstdio>

using namespace std;

#define REP(z,n) for(int (z)=0;(z)<(n);++(z))

int main()
{
 int t; scanf("%d", &t);
 char num[62];
 int val[256];
 long long sum,exp;
 int c,p,base;
 scanf("%c", &num[0]);
 for(int q=0;q<t;++q)
 {
  c=0;
  do
  {
   scanf("%c", &num[c]);
  }while(num[c++]!='\n');
  c--;
  REP(i,255) val[i]=-1;
  val[num[0]]=1;
  p=0;
  for(int i=1;i<c;++i)
  {
   if(val[num[i]]==-1) { val[num[i]]=p++; if(p==1) p++; }
  }
  base=0;
  REP(i,255) if(val[i]!=-1) base++;
  if(base==1) base++;
/*
  REP(i,c)
  {
   printf("%d ", val[num[i]]);
  }
  printf("\nBASE: %d\n", base);
*/
  sum=0;
  exp=1;
  for(int i=c-1;i>=0;--i)
  {
   sum+=exp*val[num[i]];
   exp*=base;
  }
  printf("Case #%d: %lld\n",q+1, sum);
 }
}
