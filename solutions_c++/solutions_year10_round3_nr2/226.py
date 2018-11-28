#include <iostream>
using namespace std;

int main()
{
  int T,tcase;
  cin>>T;
  for(tcase=1;tcase<=T;tcase++)
    {
      long long int L,P,C;
      cin>>L>>P>>C;
      long long int x=P/L,ans=0;
      if(!(P%L))
	x--;
      while(x/C)
	{
	  C*=C;
	  ans++;
	}
      cout<<"Case #"<<tcase<<": "<<ans<<"\n";
    }
}
