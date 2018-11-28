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
int isPoss(int a,int b,int div,int add,int dig)
{
  int l=0,l1=0,l2=0,k1=div,k=a;
  while(k) l++,k/=10;
  while(k1) k1/=10,l1++;
  if(l1-dig) return 0;
  if(l<=l1) return 0;
  int val=(div*power(10,l-l1))+add;  
  if((val>a)&&(val<=b)) return val;
  return 0;
    
}
int isposs(int a,int b)
{
  set<int> s;  
  int k=10,dig=1,l;
  while(a>k) 
    {
      l=isPoss(a,b,a%k,a/k,dig++);
      if(l) s.insert(l);
      k*=10;
    }
  return s.size();
}
int main()
{
  int kase=GI,i;
  REP(i,kase)
    {
      int a=GI,b=GI,j,count=0;
      FOR(j,a,b)
	{
	  count+=isposs(j,b);
	  //	  int arr[9];
	  //int k=10,dig=1;
	  //while(j>k) count+=isPoss(j,b,j%k,j/k,dig++,arr),k*=10;
	}
      printf("Case #%d: %d\n",i+1,count);
      
    }
}
