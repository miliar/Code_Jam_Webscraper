#include <iostream>
#include <set>

using namespace std;

int main()
{
  int cases;
  cin >> cases;

  multiset<int> v1;
  multiset<int, greater<int> > v2;

  int sum;
  int n;
  int k;
  int j;
  multiset<int>::iterator it1;
  multiset<int, greater<int> >::iterator it2;

  for (int i = 0; i < cases; ++i)
  {
    v1.clear();
    v2.clear();
    cin >> n;
    for (k = 0; k < n; ++k)
    {
      cin >> j;
      v1.insert(j);
    }
    for (k = 0; k < n; ++k)
    {
      cin >> j;
      v2.insert(j);
    }

    sum = 0;
    for (it1 = v1.begin(), it2 = v2.begin(); it1 != v1.end(); ++it1, ++it2)
    {
      sum += *it1 * *it2;
    }

    cout << "Case #" << i + 1 << ": " << sum << endl;
  }

  return 0;
}
