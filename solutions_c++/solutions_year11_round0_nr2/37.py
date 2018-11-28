#include<iostream>
#include<algorithm>

#include<vector>
#include<cstring>

using namespace std;

void pv(vector<char>& v)
{
  int sz = v.size();
  if (sz == 0)
  {
    cout << "[]";
  }
  else
  {
    cout << "[";
    for (int i = 0; i < sz - 1; i++)
    {
      cout << v[i] << ", ";
    }
    cout << v[sz - 1] << "]";
  }
}

char combine[256][256] = {};
bool opposed[256][256] = {};
vector<char> v;

bool try_combine()
{
  int sz = v.size();
  if (sz < 2)
  {
    return false;
  }
  char c = combine[(int) v[sz - 2]][(int) v[sz - 1]];
  if (c)
  {
    v.pop_back();
    v[sz - 2] = c;
    return true;
  }
  else
  {
    return false;
  }
}

bool try_oppose()
{
  int sz = v.size();
  bool clr = false;
  for (int i = 0; i < sz; i++)
  {
    if (opposed[(int)v[i]][(int)v[sz - 1]])
    {
      clr = true;
    }
  }
  if (clr) v.clear();
  return clr;
}

void solve()
{
  memset(opposed,0,sizeof opposed);
  memset(combine,0,sizeof combine);
  v.clear();
  
  int c, d, n;
  cin >> c;
  for (int i = 0; i < c; i++)
  {
    string s; cin >> s;
    int s0 = (int)s[0], s1 = (int)s[1];
    combine[s0][s1] = s[2];
    combine[s1][s0] = s[2];
  }
  cin >> d;
  for (int i = 0; i < d; i++)
  {
    string s; cin >> s;
    int s0 = (int)s[0], s1 = (int)s[1];
    opposed[s0][s1] = true;
    opposed[s1][s0] = true;
  }
  cin >> n;
  string s; cin >> s;
  for (int i = 0; i < n; i++)
  {
    v.push_back(s[i]);
    if (!try_combine())
    {
      try_oppose();
    }
  }
  pv(v);
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
