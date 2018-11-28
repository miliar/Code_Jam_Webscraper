#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
 freopen("in","r",stdin);
 freopen("out","w",stdout);
 int t;
 cin >> t;
 for(int tt=0; tt<t; tt++)
 {
  string s;
  cin >> s;
  vector<char> a(s.length()+1);
  a[0]='0';
  for(int i=0; i<s.length(); i++)
  {
   a[i+1]=s[i];
  }
  next_permutation(a.begin(), a.end());
  cout << "Case #" << tt+1 << ": ";
  if(a[0]!='0')cout << a[0];
  for(int i=1; i<a.size(); i++)cout << a[i];
  cout << endl;
 }
 return 0;
}
