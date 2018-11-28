#include<iostream>
#include<algorithm>

#include<vector>

using namespace std;

void solve()
{
  int n;
  cin >> n;
  double tot = 0;
  for (int i = 1; i <= n; i++)
  {
    int val;
    cin >> val;
    if (val != i)
    {
      tot++;
    }
  }
  cout << tot;
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
