#include <iostream>
using namespace std;


int main()
{
  int t,i;
  unsigned long long int n,k;

  cin>>t;
  for(int caseNo=1;caseNo<=t;caseNo++)
    {
      cin>>n>>k;
      for(i=0;i<n;i++)
	{
	  if(k%2==0)
	    {cout<<"Case #"<<caseNo<<": OFF"<<endl;
	      break;
	    }
	  k/=2;
	}
      if(i==n)
	cout<<"Case #"<<caseNo<<": ON"<<endl;
    }
}
