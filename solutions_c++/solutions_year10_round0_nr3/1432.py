#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;
#define p(x) ;//cout<<#x<<":"<<x<<"\n"
#define ll long long
#define lim 1001

ll cs,c,r,k,n,i,j,s,sz,s2;
ll N[lim],S[lim],A[lim];
bool B[lim];

int main()
{
  cin>>cs;
  for(c=1;c<=cs;c++)
  {
    cin>>r>>k>>n;
	for(i=s=0;i<n;i++)
	{
	  cin>>A[i];
	  s+=A[i];
	}
	if(s<=k)
	  s*=r;
	else
	{
	  for(i=0;i<n;i++)
	  {
	    for(j=i,s=A[j];s<=k;)
		{
		  j=(j+1)%n;
		  s+=A[j];
		}
	    N[i]=j;
		p(N[i]);
		S[i]=s-A[j];
		p(S[i]);
	  }
	  s=0;
	  if(r>=n)
	  {
	    i=0;
	    memset(B,0,sizeof B);
	    while(!B[i])
	    {
	      B[i]=1;
		  i=N[i];
	    }
		p(i);
	    j=0;
	    while(j!=i)
	    {
		  p(j);
	      s+=S[j];
		  r--;
	      j=N[j];
	    }
	    memset(B,0,sizeof B);
	    j=N[i];
	    sz=1;
		s2=S[i];
	    while(j!=i)
	    {
		  p(j);
		  p(S[j]);
		  s2+=S[j];
	      sz++;
		  j=N[j];
	    }
		p(sz);
		p(s2);
		s+=r/sz*s2;
		r%=sz;
		j=i;
		while(r)
		{
		  s+=S[j];
		  j=N[j];
		  r--;
		}
	  }
	  else
	  {
	    i=0;
		for(j=0;j<r;j++)
		{
		  s+=S[i];
		  i=N[i];
		}
	  }
	}
	cout<<"Case #"<<c<<": "<<s<<"\n";
  }
  return 0;
}
