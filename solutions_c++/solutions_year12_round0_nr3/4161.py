#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<vector>
#include<stack>
#include<sstream>
#include<cstdlib>
#include<algorithm>
using namespace std;
#define si(n) scanf("%d",&n)
#define sf(n) scanf("%f",&n)
#define sl(n) scanf("%lld",&n)
#define lli long long int

int main()
{
  int t;
  si(t);
  int w=0;
  int r=1;
  int q=0;
  int ans1[1000];
  while(t--)
    {
      bool check[1000]={false};
      int ans=0;
      int A,B;
      si(A); si(B);
      int n=A;
      int dig=0;
      while(n!=0)
	{
	  n/=10;
	  dig++;
	}
      if(dig==1)
	ans=0;
      else
	{
  for(int i=A;i<=B;i++)
	{
	  if(check[i])
	    continue;
	  else
	    {
	  int mul=10;
	  for(int j=0;j<dig;j++)
	    {
	      int a= i/mul;
	      int r= i%mul;
	       r*=pow(10,dig-j-1);
	      r+=a;
	      if(r<=B && r>=A && r!=i)
		{
		ans++;
		}
	      mul*=10;
	    }
	    }
	}
	}
      cout<<"Case #"<<r++<<": "<<ans/2<<"\n";
      }
  return 0;

	       
}
