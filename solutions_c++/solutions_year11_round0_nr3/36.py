#include<iostream>
#include<algorithm>

#include<vector>

using namespace std;

void solve()
{
  vector<int> a;
  int n; cin >> n;
  int x_val = 0, s_val = 0;
  for (int i = 0; i < n; i++)
  {
    int t; cin >> t;
    a.push_back(t);
    x_val ^= t;
    s_val += t;
  }
  if (x_val)
  {
    cout << "NO";
  }
  else
  {
    sort(a.begin(), a.end());
    cout << s_val - a[0];
  }
}

int main()
{
  int t; cin >> t;
  for (int i = 1; i <= t; i++)
  {
    cout << "Case #" << i << ": ";
    solve();
    cout << endl;
  }
}
