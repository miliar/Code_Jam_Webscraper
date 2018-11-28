#include <iso646.h>
#include <iostream>
using namespace std;

int main()
{
  int T;
  cin>>T;
  for(int t=1;t<=T;t++)
    {
      int N,c,sum,mn,xsum;
      cin>>N;
      cin>>c;
      sum=mn=xsum=c;
      for(int i=1;i<N;i++)
	{
	  cin>>c;
	  if(c<mn)
	    mn=c;
	  sum+=c;
	  xsum^=c;
	}
      cout<<"Case #"<<t<<": ";
      if(xsum)
	cout<<"NO\n";
      else
	cout<<sum-mn<<"\n";
    }
  return 0;
}
