#include<iostream>
#include<algorithm>

#include<vector>

using namespace std;

void solve()
{
  int l_time[2], l_place[2];
  l_time[0] = l_time[1] = 0;
  l_place[0] = l_place[1] = 0;
  int earliest[200] = {};
  int n; cin >> n;
  for (int i = 1; i <= n; i++)
  {
    string who;
    int pos;
    cin >> who >> pos;
    pos--;
    int wh = (who == "B") ? 0 : 1;
    earliest[i] = max(l_time[1 - wh], l_time[wh] + abs(l_place[wh] - pos));
    l_place[wh] = pos;
    l_time[wh] = earliest[i] + 1;
  }
  cout << earliest[n] + 1;
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
