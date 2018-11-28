#include<iostream>
using namespace std;
int main()
{
  unsigned long int t,k,n,i;
  unsigned long int x;
  cin>>t;
  for(i=1;i<=t;++i)
    {
      cin>>n>>k;
      if(k==0)
	{
	  cout<<"Case #"<<i<<": OFF"<<endl;
	  continue;
	}
      x=1L;
      x<<=n;
      if(k%x == x-1)
	{
	  cout<<"Case #"<<i<<": ON"<<endl;
	}
      else
	{
	  cout<<"Case #"<<i<<": OFF"<<endl;
	}
    }
  return 0;
}
