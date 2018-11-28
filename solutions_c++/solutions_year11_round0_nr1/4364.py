#include <iostream>
#include <algorithm>
#include <cmath>

#define P(c) (c=='O'?0:1)

using namespace std;
using namespace __gnu_cxx;

int main()
{
  int p[2];
  int t, n;
  int q, s, r;
  char c, c_;

  cin >> t;
  for(int i=1; i<=t; i++)
  {
    p[P('B')] = 1;
    p[P('O')] = 1;
    s = 0;
    r = 0;
    c_ = 'X';

    cin >> n;

    for(int j=0; j<n; j++)
    {
      cin >> c >> q;
      
      if(c != c_)
      {
	s = max(0, abs(p[P(c)] - q) - s) + 1;
	r += s;
      }
      else
      {
	s += abs(p[P(c)] - q) + 1;
	r += abs(p[P(c)] - q) + 1;
      }
      p[P(c)] = q;
      c_ = c;
    }

    cout << "Case #" << i << ": " << r << endl;
  }
  return 0;
}

