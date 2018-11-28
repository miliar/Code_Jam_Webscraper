
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

bool match(string str,vector<string>& pattern)
{
  int L = str.size();
  for(int i=0;i<L;++i)
  {
    if(find(pattern[i].begin(),pattern[i].end(),str[i])==pattern[i].end())
      return false;
  }
  return true;
}

int main(int,char**)
{
  int L,D,N;
  cin >> L >> D >> N;

  vector<string> dict(D);
  for(int i=0;i<D;++i)
    cin >> dict[i];

  for(int i=0;i<N;++i)
  {
    cout << "Case #" << (i+1) << ": ";
    vector<string> pattern(L);

    for(int j=0;j<L;++j)
    {
      char c;
      cin >> c;
      if(c=='(')
	getline(cin,pattern[j],')');
      else
	pattern[j] = c;
    }

    int res = 0;
    for(int j=0;j<D;++j)
      if(match(dict[j],pattern))
	++res;
    cout << res << '\n';
  }

  return 0;
}
