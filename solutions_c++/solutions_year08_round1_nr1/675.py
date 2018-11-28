
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long int int64;

template <typename T>
struct more
{
  bool operator()(const T &a, const T &b) const
  {
    return a > b;
  }
};

int main()
{
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t)
  {
    int n;
    cin >> n;
    vector<int> x(n), y(n);
    for (int i = 0; i < n; ++i)
      cin >> x[i];
    for (int i = 0; i < n; ++i)
      cin >> y[i];

    sort(x.begin(), x.end(), less<int>());
    sort(y.begin(), y.end(), more<int>());

    int64 total = 0;
    for (int i = 0; i < n; ++i)
      total += x[i] * y[i];
    cout << "Case #" << t << ": " << total << endl;
  }
  return 0;
}
