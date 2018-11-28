#include<iostream>
#include<stdio.h>
using namespace std ;
#define MAXN 1000002
#define MOD 20100713
int fac[MAXN] ;

int power(int a,int b)
{
 if(b == 0) return 1 ;
 long long ret = power(a,b/2) ;
 ret *= ret ;
 ret %= MOD ;
 if(b%2 == 1) ret = ret*a%MOD ;
 return ret ;
}

int main()
{
 int i,j,n,k,t ;
 fac[0] = 1 ;
 for(i=1;i<MAXN;i++)
 {
  fac[i] = (1LL*i*fac[i-1])%MOD ;
 }
 scanf("%d",&t) ;
 while(t--)
 {
  scanf("%d%d",&n,&k) ;
  int ret = (1LL*fac[k]*(power(k+1,n-k) - power(k,n-k) + MOD))%MOD ;
  printf("%d\n",ret) ;
 }
 return 0 ;
}
