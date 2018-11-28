#include <iostream>
#include <sstream>
#include <math.h>
#include <stdio.h>
#include <string>
#include <map>

using namespace std;

string revx(string s, int a, int b)
{
  if(a>=b)
    return s;
  swap(s[a],s[b]);
  return revx(s,a+1,b-1);    
}

int str2int(string s)
{
  int ret;
  sscanf(s.c_str(),"%d",&ret);
  return ret;
}

string int2str(int x)
{
  ostringstream s;
  s << x;
  return s.str();
}

int main()
{
  ios_base::sync_with_stdio(0);
  int t;
  cin >> t;
  for(int j = 1; j <= t; j++)
    {
      int a, b;
      cin >> a >> b;
      int sum = 0;
      for(int i = a; i < b; i++)
	{
	  string tmp = int2str(i);
	  map<string,int> mp;
	  for(int k = 1; k < tmp.length(); k++)
	    {
	      //cout << tmp << "->";
	      string neu = tmp.substr(tmp.length()-k,k) + tmp.substr(0,tmp.length()-k);
	      //cout << neu << endl;
	      int neu2 = str2int(neu);
	      if(neu2 > i && neu2 <= b && mp[neu]==0)
		{
		  //cout << tmp << "->" << neu << endl;
		  sum++;
		  mp[neu] = 1;
		}
	    }
	}
      cout << "Case #" << j << ": " << sum << endl;
    }
  return 0;
}
