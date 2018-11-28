#include <iostream>
#include <climits>
#include <algorithm>
using namespace std;

int main()
{
  int t; cin >> t;
  for (int i = 0; i < t; ++i)
  {
    int n; cin >> n;
    
    int sumc = 0;
    int minc = INT_MAX;
    int pos = 0;

    for (int j = 0; j < n; ++j)
    {
      int c; cin >> c;

      sumc += c;
      minc = min(c, minc);
      pos  = pos^c;
    }

    cout << "Case #" << (i+1) << ": ";
    if (pos)
      cout << "NO";
    else
      cout << (sumc - minc);
    cout << endl;
  }

  return 0;
}
