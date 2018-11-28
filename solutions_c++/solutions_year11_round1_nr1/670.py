#include <string>
#include <cstdio>
#include <iostream>
using namespace std;

int gcd(int a, int b )
{
  return b == 0 ? a : gcd(b, a%b);
}

int main()
{
  int T;
  cin >> T;
  int C = 1;
  while(T--)
    {

      long long N;
      int Pd, Pg;
      cin >> N >> Pd >> Pg;
      
      int sa = Pd / gcd(Pd, 100);
      int sb = 100 / gcd(Pd, 100);
      int ta = Pg / gcd(Pg, 100);
      int tb = 100 / gcd(Pg, 100);
      
      bool ok = true;
      // cout<<sb<<" "<<gcd(Pd, 100)<<" "<<Pd<<endl;
      if( sb > N )
	ok = false;
      if( Pg == 100 && Pd != 100 )
	ok = false;
      if( Pg == 0 && Pd != 0 )
	ok = false;
      string ans;
      if( ok )
	ans = "Possible";
      else
	ans = "Broken";
	
      printf("Case #%d: %s\n", C++, ans.c_str());
    }
}
