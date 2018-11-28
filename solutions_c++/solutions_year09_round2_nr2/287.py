#include <iostream>
#include <functional>
#include <sstream>
#include <vector>
#include <algorithm>
#include <bitset>
#include <iomanip>
#include <set>
#include <queue>

using namespace std;

int main()
{  
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  int tests;
  cin >> tests;

  for (int t = 0; t < tests; ++t)
  {
    string n;
    cin >> n;

    int digits[11] = {0};
    string n2;
    for (int i = 0; i < n.size(); ++i)
    {
      if (n[i] != '0')
        n2 += n[i];
      ++digits[n[i] - '0'];
    }

    string n3 = n;
    sort(n3.begin(), n3.end(), greater<char>());
    
    if (n3 == n)
    {
      n3 = n2;
      reverse(n3.begin(), n3.end());
      n3.insert(1, string(digits[0] + 1, '0'));
    }
    else
    {
      n3 = n;
      next_permutation(n3.begin(), n3.end());
    }
 
 
    cout << "Case #" << t + 1 << ": " << n3 << "\n";
  }

  return 0;
}