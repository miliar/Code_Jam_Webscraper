#include<stdio.h>
using namespace std;
int T,p;
int pd,pg,k;
long long n;
int gcd(int x,int y)
{
  if(x%y==0) return y;
  return gcd(y,x%y);
}
int main()
{
  freopen("A.in","r",stdin);
  freopen("A.out","w",stdout);
  scanf("%d",&T);
  for(p=1;p<=T;p++){
    scanf("%I64d%d%d",&n,&pd,&pg);
    k=gcd(pd,100);
    printf("Case #%d: ",p);
    if(n<(100/k)){
      printf("Broken\n");continue;}
    if(pg==0 && pd!=0){
      printf("Broken\n");continue;}
    if(pd!=100 && pg==100){
      printf("Broken\n");continue;}
    printf("Possible\n");
  }
  scanf("%d",&T);
  return 0;
}
    
