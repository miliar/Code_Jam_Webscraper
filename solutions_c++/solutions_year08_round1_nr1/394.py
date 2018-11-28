#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;
#define lim 801
#define ll long long
#define print(x) cout<<#x<<":"<<x<<"\n"

ll cs,c,n,i,res;
ll A[lim],B[lim];

int main()
{
  scanf("%lld",&cs);
  for(c=0;c<cs;c++)
  {
    scanf("%lld",&n);
	for(i=0;i<n;i++)
	  cin>>A[i];
	for(i=0;i<n;i++)
	  cin>>B[i];
    sort(A,A+n);
    sort(B,B+n);
    reverse(B,B+n);
	res=0;
	for(i=0;i<n;i++)
	{
	  res+=A[i]*B[i];
	}
	cout<<"Case #"<<c+1<<": "<<res<<"\n";
  }
  return 0;
}
