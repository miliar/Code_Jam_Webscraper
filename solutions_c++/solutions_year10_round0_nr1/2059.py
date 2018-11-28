#include<string>
#include<vector>
#include<iostream>
#include<utility>
#include<algorithm>
#include<set>
#include<stack>
#include<sstream>
#include<math.h>

using namespace std;

#define PB push_back
#define ll long long
#define VI vector<int>
#define VS vector<string>

int main(int argc, char** argv)
{
  int T;
  cin >> T;
  for(int i = 0; i < T; ++i)
    {
      ll N,K;
      cin >> N >> K;
      
      ll count = 0;
      bool ON = true;
      ll num = K+1;

      if(num%(long)(pow(2, N)) == 0)
	ON = true;
      else
	ON = false;

      cout << "Case #" << (i+1) << ": " ;

      if(ON)
	{
	  cout << "ON" << endl;
	}
      else
	{
	  cout << "OFF" << endl;
	}
    }
  return 0;
}
