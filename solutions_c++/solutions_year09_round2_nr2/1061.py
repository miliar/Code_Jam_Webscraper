#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

char sz[50000];

string nn(string s)
{
  for(int i = s.length() - 1; i > 0; i--)
  {
    if(s[i - 1] < s[i])
    {
      int k = i;
      for(int j = i; j < s.length(); j++)
      {
        if(s[j] < s[k] && s[j] > s[i - 1])
        {
          k = j;
        }
      }

      swap(s[i - 1], s[k]);
      sort(s.begin() + i, s.end());
      return s;
    }
  }

  sort(s.begin(), s.end());
  s.insert(s.begin() + 1, '0');

  if(s[0] == '0')
  {
    for(int i = 1; i < s.length(); i++)
    {
      if(s[i] > '0')
      {
        swap(s[0], s[i]);
        break;
      }
    }
  }

  return s;
}

int main(int argc, char *argv[])
{
  int T;

  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  gets(sz);
  T = atoi(sz);
  for(int i = 1; i <= T; i++)
  {
    gets(sz);
    cout << "Case #" << i << ": " << nn(sz) << endl;
  }

  return 0;
}