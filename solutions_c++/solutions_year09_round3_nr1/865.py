#include <iostream>
#include <string>
#include <map>
#include <vector>

using namespace std;

char sz[50000];

long long pw(int b, int p)
{
  long long r = 1;

  for(int i = 0; i < p; i++)
  {
    r *= b;
  }

  return r;
}

long long gm(string s)
{
  map<char, char> m;
  char ch = '0';
  int b = 2;

  if(s.length() == 1) return 1;

  m[s[0]] = '1';
  for(int i = 0; i < s.length(); i++)
  {
    if(m.count(s[i]) == 0)
    {
      m[s[i]] = ch++;
      if(ch == '1') ch++;
      b = max(b, int(ch - '0'));
    }
  }

  for(int i = 0; i < s.length(); i++)
  {
    s[i] = m[s[i]];
  }

  long long r = 0;

  for(int i = 0; i < s.length(); i++)
  {
    r += (s[i] - '0') * pw(b, s.length() - 1 - i);
  }

  return r;
}

int main(int argc, char *argv[])
{
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  int T = atoi(gets(sz));
  for(int i = 1; i <= T; i++)
  {
    printf("Case #%d: %lld\n", i, gm(gets(sz)));
  }

  return 0;
}