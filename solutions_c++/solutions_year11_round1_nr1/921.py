#include <iostream>

using namespace std;

typedef long long ll;


ll gcd(ll a, ll b)
{
  if(a<b)
    return gcd(b, a);
  if(b==0)
    return a;
  return gcd(b, a%b);
}

int main()
{
  ll tc, N, Pd, Pg;
  cin>>tc;
  for(int T=1; T<=tc; T++)
    {
      cin>>N>>Pd>>Pg;
      cout<<"Case #"<<T<<": ";
      bool pos = true;
      if(Pg==0)
	{
	  if(Pd==0)
	    pos = true;
	  else
	    pos = false;
	}
      else
	{
	  if(Pg==100)
	    {
	      if(Pd==100)
		pos = true;
	      else
		pos = false;
	    }
	  else
	    {
	      if( N >= 100 / gcd(Pd, 100) )
		pos = true;
	      else
		pos = false;
	    }
	}
      
      if(pos)
	cout<<"Possible"<<endl;
      else
	cout<<"Broken"<<endl;
      
    }
  
  return 0;
}
