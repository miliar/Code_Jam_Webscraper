#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool check(string const& s1, int k)
{
  if (k + 1 == s1.size())
    return true;
  return s1.find('1', k + 1) == -1;
}

bool less(string const& s1, string const& s2, int k, int n)
{
  bool c11 = check(s1, k);
  bool c12 = check(s1, k + 1);
  bool c21 = check(s2, k + 1);
  bool c22 = check(s2, k);

  if (c11 && c21)
    return false;

  if (!c11 && !c21)
    return false;

  if (c22)
    return true;

  return false;
}

int main()
{
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);


  int tests;
  cin >> tests;
  for (int t = 0; t < tests; ++t)
  {
    int n;
    cin >> n;
    vector<string> a(n);
    for (int i = 0; i < n; ++i)
      cin >> a[i];

    int res = 0;
    bool ok;
    do {
      ok = false;
      for (int i = 0; i < n - 1; ++i)
        if (!check(a[i], i))
        {
          for (int j = i + 1; j < n; ++j)
          {
            if (check(a[j], j) && check(a[j], i))
            {
              for (int k = j; k > i; --k, ++res)
                swap(a[k], a[k - 1]);
ok = true;
              break;
            }
          }

          
          break;
        }
    }
    while (ok);

    cout << "Case #" << t + 1 << ": " << res << "\n";
  }
  return 0;
}
