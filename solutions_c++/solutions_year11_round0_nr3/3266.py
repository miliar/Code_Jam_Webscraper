#include <iostream>
#include <cstdio>
using namespace std;
long long n, a[1010], k, tmp, len, ans, s1, s2, k1, k2;
string st;
string bin(int x)
{
  string res = "";
  while(x)
  {
    res = char(x % 2 + 48) + res;
    x /= 2;
  }
  return res;
}
int dec(string s)
{
  int res = 0, a = 1;
  for(int i = s.size() - 1; i >= 0; i--)
  {
    res += (s[i] == '1') * a;
    a *= 2;
  }
  return res;
}
int main()
{
  freopen("C-small-attempt2.in","r",stdin);
  freopen("output.txt","w",stdout);
  cin >> n;
  for(int i = 0; i < n; i++)
  {
    cin >> k;
    tmp = ans = 0;
    for(int j = 0; j < k; j++)
    {
      cin >> a[j];
      tmp ^= a[j];
    }
    if (tmp == 0)
    {
      int p = 1 << k;
      for(int q = 1; q < p; q++)
      {
        s1 = s2 = k1 = k2 = 0;
        st = bin(q);
        while(st.size() < k)
          st = '0' + st;
        for(int r = 0; r < st.size(); r++)
          if (st[r] == '0')
            k1++, s1 += a[r];
          else
            k2++, s2 += a[r];
        if (k1 != k && k2 != k)
          ans = max(ans, max(s1, s2));
      }
    }
    cout << "Case #" << i + 1 << ": ";
    if (ans == 0)
      cout << "NO" << endl;
    else
      cout << ans << endl;
  }
  return 0;
}