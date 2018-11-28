#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

vector<char> d;

int main()
{  
  freopen("B.large", "r", stdin);
  int t,n,i,j;
  cin >> t;
  string s,z;
  bool flag;
  char min;
  string::iterator it;
  for(i = 1; i<=t; i++)
  {
    cin >> s;
    if (!next_permutation(s.begin(), s.end()))
    {
      sort(s.begin(), s.end());
      for (it = s.begin(); *it=='0'; ++it)
      {}
      char c = *it;
      s.erase(it);
      cout << "Case #" << i << ": " << c << '0' << s << endl;      
    }
    else
      cout << "Case #" << i << ": " << s << endl;
    // min = '9';
    // flag = false;
    // for(j = s.length()-1; j >=0; j--)
    // {
    //   if (s[j] < min)
    //     min = s[j];
    // }
    // 
    // for (j = s.length()-1; j>0; j--)
    // {
    //   for ()
    //   flag = s[j] > s[j-1];
    //   if (flag)
    //     break;
    // }
    // 
    // if (flag)
    // {
    //   min = s[j];
    //   s[j] = s[j-1];
    //   s[j-1] = min;
    // }
    // else 
    // {
    //   s = '0'+s;
    //   s = min+s;
    // }
    // for(j = 0; j < s.size(); j++)
    //   cout << d[j];
    // cout << endl;
  }
  return 0;
}