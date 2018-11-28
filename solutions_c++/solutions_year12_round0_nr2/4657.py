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
  int r=1;
  while(t--)
    {
      int N,A[100];
      si(N);
      int S;
      si(S);
      int p;
      si(p);
      for(int i=0;i<N;i++)
	si(A[i]);
      int ans=0;
      for(int i=0;i<N;i++)
	{
	  int a= A[i]/3;
	  int r= A[i]%3;
	  if(a>=p)
	    ans+=1;
	  else
	    {
	      if(a==0 && r==0)
		{
		 continue;
		}

	     else if(p-a==1)
		{
		  if(r!=0)
		    ans+=1;
		  else if(S>0)
		    {
		    ans+=1;
		    S--;
		    }
		}
	      else if(p-a==2)
		{
		  if(r==2)
		    if(S>0)
		      {
		      ans+=1;
		      S--;
		      }
		}
	    }
	}
      cout<<"Case #"<<r++<<": "<<ans<<"\n";
    }
  return 0;

	       
}
