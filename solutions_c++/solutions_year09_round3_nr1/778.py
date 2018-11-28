#include <iostream>
#include <vector>
#include <list>
#include <map>
#include <algorithm>
#include <istream>
#include <string>
#include <math.h>

using namespace std;

long long int
intpow(int x, int y)
{
  long long int ans = 1;
  if (y == 0)
    return 1;
  if (x == 0)
    return 0;

  while (y--)
    ans *= x;
  return ans;
}

long long int
smallest(string str)
{
  vector<int> in;
  map<int, int> m;
  int ctr = 1;
  for (int i = 0; i < str.size(); ++i)
    {
      int digit = str[i];
      /*      if (isdigit(str[i]))
	{
	  digit = str[i]-'0';
	}
      else
	{
	  digit = str[i]-'a'+10;
	}
      */
      in.push_back(digit);
      if (m.find(digit) == m.end())
	{
	  if (ctr == 2 && m.size() == 1)
	    {
	      m[digit] = 0;
	    }
	  else
	    {
	      m[digit] = ctr;
	      ++ctr;
	    }
	}
    }

  int base = m.size();
  if (base == 1)
    ++base;
  cerr<<"Base: "<<base<<endl;

  long long int ans = 0;
  ctr = 0;
  for (int i = in.size()-1; i>=0; --i)
    {
      ans += (((long long int)(m[in[i]])) * intpow(base, ctr));
      ++ctr;
    }
  return ans;
}


int
main()
{
  int t;
  cin>>t;
  // cerr<<sizeof(long long int)<<endl;
  for (int i = 0; i < t; ++i)
    {
      string line;
      cin>>line;
      cout<<"Case #"<<i+1<<": "<<smallest(line)<<endl;
    }
}
