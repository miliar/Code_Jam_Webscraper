#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;
#define p(x) cout<<#x<<":"<<x<<"\n"
#define ll long long

ll cs,c,i,g,n;
ll A[1001];

ll gcd(ll a,ll b)
{
  if(a<b)
    return gcd(b,a);
  if(!b)
    return a;
  return gcd(b,a%b);
}
int main()
{
  cin>>cs;
  for(c=1;c<=cs;c++)
  {
    cin>>n;
	for(i=0;i<n;i++)
	  cin>>A[i];
	g=0;
	for(i=1;i<n;i++)
	  g=gcd(g,abs(A[i]-A[0]));
	cout<<"Case #"<<c<<": "<<(g-A[0]%g)%g<<"\n";
  }
  return 0;
}
