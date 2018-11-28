#include <iostream>
using namespace std;

int main()
{
  int i,n,k,t,tc;
  cin>>t;
  for(tc=1;tc<=t;tc++)
    {
      cin>>n>>k;
      k++;
      for(i=0;i<n;i++)
	{
	  if(k%2)
	    break;
	  else
	    k/=2;
	}
      cout<<"Case #"<<tc<<": O";
      if(i==n)
	cout<<"N";
      else
	cout<<"FF";
      cout<<"\n";
    }
}
