#include <iostream>
#include <string>
#include <map>
#include <sstream>
#include <cstdlib>
#include <algorithm>

using namespace std;

map<string, bool> mpp;

string conv(int n)
{
  stringstream ss;
  ss << n;
  return ss.str();
}

bool func(string s1, string s2)
{
  for(int i = 0; i < s2.size(); ++i){
    if(s2[0] != '0' && s1 == s2) return true;
    s2 = s2.substr(1) + s2[0];
  }

  return false;
}

int main()
{
  int n, m, tcs, cnt;
  string str;

  while(cin>>tcs && tcs)
    for(int cs = 1; cs <= tcs; ++cs){
      cin >> n >> m;
      cnt = 0;
      for(int i = n; i <= m; ++i)
	for(int j = i+1; j <= m; ++j)
	  if(func(conv(i), conv(j))) ++cnt;

      cout << "Case #" << cs << ": " << cnt << endl;
      mpp.clear();
    }

  return 0;
}
