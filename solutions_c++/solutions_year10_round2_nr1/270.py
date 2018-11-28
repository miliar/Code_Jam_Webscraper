#include <iostream>
#include <map>
#include <string>

using namespace std;

int main()
{
  freopen("a.in", "r", stdin);
  freopen("a.out", "w", stdout);
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++)
  {
    cout << "Case #" << t << ": ";
    int n, m;
    cin >> n >> m;
    map<string, string> Map;
    for (int i = 0; i < n; i++)
    {
      string s, t = "";
      cin >> s;
      s += "/";
      for (int i = 1; i < s.length(); i++)
      {
        if (s[i] != '/') continue;
        string z = s.substr(0,i);
        Map[z] = t;
        t = z;
      }
    }
    int ans = 0;
    for (int i = 0; i < m; i++)
    {
      string s, t = "";
      cin >> s;
      s += "/";
      for (int i = 1; i < s.length(); i++)
      {
        if (s[i] != '/') continue;
        string z = s.substr(0,i);
        if (Map.find(z) == Map.end()) ans++;
        Map[z] = t;
        t = z;
      }
    }
    cout << ans << endl;
  }
  return 0;
}