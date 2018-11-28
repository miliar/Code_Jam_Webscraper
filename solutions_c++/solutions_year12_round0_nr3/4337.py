#include <sstream>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;

string IntToString(int number)
{
  ostringstream s ;
  s << number ;
  return s.str() ;
}

int main()
{

  int T;
  cin>>T;

  for(int i = 1;i <= T;i++)
    {

      
      int A,B;
      cin >> A >> B;
      int ans = 0;
      string Blim = IntToString(B);
      string Alim = IntToString(A);
      int slen = Blim.size();

      for(int j = A; j <= B; j++)
	{
	  string str = IntToString(j);
	  string strmem = str;
	  if(slen == 1)break;

	  else if(slen == 2)
	    {
	      swap(str[0],str[1]);
	      if(strmem != str && Blim >= str && Alim <= str)
		ans++;
	    }
	  else if(slen == 3)
	    {
	      string strmem2 = str;
	      swap(str[0],str[2]);
	      swap(str[1],str[2]);

	      if(strmem != str && Blim >= str && Alim <= str)
		ans++;
	      str = strmem2;

	      swap(str[0],str[1]);
	      swap(str[1],str[2]);

	      if(strmem != str && Blim >= str && Alim <= str)
		ans++;

	    }
	}

	  cout << "Case #" << i << ":" << " " << ans/2 <<endl;
    }
}
