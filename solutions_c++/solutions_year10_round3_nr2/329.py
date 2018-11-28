#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;


int logC(int k,int c)
{
  long long t=1;
  int wyk=0;
  while(t<k){t*=c;wyk++;}
  return wyk;
}

long long ipow(int a, int b)
{
  long long t=1;int c=a;
  for(int i=1;i<=b;i++)t*=c;
  return t;
}

int main()
{
  int T;
  scanf("%d",&T);
  for(int w=1;w<=T;w++)
  {
    long long L,P,C;
    scanf("%lld %lld %lld",&L,&P,&C);
    int l1=logC(L,C),l2=logC(P,C);
    int r=l2-l1;
    r+=((long long)(P)>L*ipow(C,r));
    int wynik=int(ceil(log2(r)));
    printf("Case #%d: %d\n",w,wynik);
  }
  return 0;
}
