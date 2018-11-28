#include<iostream>
#include<vector>
#include<cstdlib>
#include<string>
#include<cstring>
#include<cmath>
#include<map>
#include<set>
#include<cstdio>
#include<algorithm>
using namespace std;
#define FOR(i,k,l) for(i=k;i<l;i++)
#define REP(i,k) for(i=0;i<k;i++)  
#define LL long long
#define GI ({int t;scanf("%d",&t);t;})
#define GL ({LL t;scanf("%lld",&t);t;})
#define GD ({double t;scanf("%lf",&t);t;})
#define MOD 10000007
/**calculate inverse(1/a)%n*/

LL int modInverse(LL int a, LL int n) 
{
  LL int i = n, v = 0, d = 1;
  while (a>0) 
    {
      LL int t = i/a, x = a;
      a = i % x;
      i = x;
      x = d;
      d = v - t*x;
      v = x;
    }
  v %= n;
  if (v<0) v = (v+n)%n;
  return v;
}
/**calculate inverse(1/n)%MOD ENDS*/


/**Calculate Fastpower n^k ENDS*/
LL power(LL n,LL k)
{
  LL t,l;
  if(k%2) t=n;else t=1;
  if(k==1) return n;
  if(!k) return 1;
  return ((l=power(n,k/2))*l*t)%MOD;
}
/**Calculate nCr*/
LL comb(LL n,LL r)
{
  //  return (((fact[n]*rfact[n-r])%MOD)*rfact[r])%MOD;


}
/**Calculate nCr ENDS*/
int bsearch(int a[],int front,int end,int k)
{
  int mid,val=0,i;
  while(front<=end)
    {
      mid=(front+end)/2;
      if(a[mid]==k) {i=mid;while(a[i]==mid)i--;return i;}  
      else if(a[mid]>k) end=mid-1;
      else if(a[mid]<k) front =mid+1;
    }
  return -1;
}
int main()
{
  int kase=GI,i;
  REP(i,kase)
    {
      int n=GI,s=GI,p=GI,k,j;
      int sass=0,cnt=0;
      REP(j,n) 
	{
	  k=GI;	  
	  if(k>=max((3*p-4),0))
	    {	    
	      if(k>1&&k<28)if(((k==(3*p-4))||(k==(3*p-3))))sass++,cnt++;
	      if(k>=(3*p-2)) cnt++;
	    }
	}
      if(s<sass) cnt-=(sass-s);
      printf("Case #%d: %d\n",i+1,cnt);
	
    }
      
}
  
