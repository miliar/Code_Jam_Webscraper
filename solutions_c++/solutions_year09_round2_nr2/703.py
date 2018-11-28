#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

string Solve()
{
  string t;
  cin >> t;
  
  int n = t.size();
  for (int i = n - 2; i >= 0; i -- )
    {
      char minn = '9' + 1; int pos = -1;
      for (int j = i + 1; j < n; j++)
        if(t[i] < t[j] && t[j] < minn) { minn = t[j]; pos = j; } 
      //cout << i << " " << pos << endl;
      if ( pos != -1) { swap(t[i],t[pos]); sort(t.begin() + i + 1, t.end()); return t; }
    }
  
  string res = t + "0";
  sort(res.begin(), res.end());
  for(int i = 0; i < res.size(); i++)
    if ( res[i] != '0' ) { swap(res[0], res[i]); sort(res.begin() + 1, res.end()); break; }
  return res;
}

int main() 
{ 
  int tests;
  scanf("%d", &tests);
  for (int i = 1; i <= tests; i++)
    {
      string res = Solve();
      printf("Case #%d: %s\n", i, res.c_str());
    }
    
  //system("pause");
  return 0;
}
