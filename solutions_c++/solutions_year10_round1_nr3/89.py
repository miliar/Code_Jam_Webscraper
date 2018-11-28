#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;
#define p(x) cout<<#x<<":"<<x<<"\n"
#define lim 1000001
#define ll long long

ll i,a1,b1,a2,b2,cs,c,s,a,b,n,x;
bool f;
ll A[lim],S[lim],E[lim];

ll fun(ll a,ll b)
{
  n=0;
  if(a<b)
    swap(a,b);
  while(b)
  {
	A[n++]=a/b;
    x=a;
    a=b;
	b=x%b;
  }
  f=1;
  for(i=n-1;i>=0;i--)
    if(f)
	  if(A[i]==1)
	    f=0;
	  else
	    f=1;
	else
	  f=1;
  return f;
}
int main()
{
  for(a=b=1;a<lim;a++)
  {
	for(;fun(a,b);b++);
    S[a]=b-1;
  }
  for(a=b=lim-1;a>0;a--)
  {
	for(;fun(a,b);b--);
    E[a]=b+1;
  }
  cin>>cs;
  for(c=1;c<=cs;c++)
  {
    cin>>a1>>a2>>b1>>b2;
	for(s=0,a=a1;a<=a2;a++)
	{
	  s+=max(min(S[a],b2)-b1+1,0ll);
	  s+=max(b2-max(E[a],b1)+1,0ll);
	}
    cout<<"Case #"<<c<<": "<<s<<"\n";
  }  
  return 0;
}
