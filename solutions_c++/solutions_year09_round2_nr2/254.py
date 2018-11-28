#include <iostream>
#include <string>

using namespace std;

void out (int num[])
{
  for (int j = 0; j < 10; j++)
  {
    for (int k = 0; k < num[j]; k++)
      cout << j;
  }
}

int main ()
{
  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++)
  {
    cout << "Case #" << t << ": ";
    string s;
    cin >> s;
    int num[11] = {0};
    int ok = 0;
    for (int i = s.length()-1; i >= 0; i--)
    {
      num[s[i]-'0']++;
      int j;
      for (j = s[i]-'0'+1; j < 10; j++)
      {
        if (num[j] > 0) break;
      }
      if (j == 10) continue;
      cout << s.substr(0,i);
      cout << j;
      num[j]--;
      out(num);
      ok = 1;
      break;
    }
    if (!ok)
    {
      num[0]++;
      int j;
      for (j = 1; j < 10; j++)
      {
        if (num[j] > 0) break;
      }
      cout << j;
      num[j]--;
      out(num);
    }
    cout << endl;
  }
  return 0;
}