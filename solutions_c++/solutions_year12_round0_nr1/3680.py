#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<ctime>
#include<cstring>
#include<string>
#include<map>
#include<set>
#include<cassert>
#include<cstdlib>
using namespace std;

#define taskname "a"

map<char, char> m;

int main()
{
  freopen(taskname".in", "r", stdin);
  freopen(taskname".out", "w", stdout);
  m['a'] = 'y';
  m['b'] = 'h';
  m['c'] = 'e';
  m['d'] = 's';
  m['e'] = 'o';
  m['f'] = 'c';
  m['g'] = 'v';
  m['h'] = 'x';
  m['i'] = 'd';
  m['j'] = 'u';
  m['k'] = 'i';
  m['l'] = 'g';
  m['m'] = 'l';
  m['n'] = 'b';
  m['o'] = 'k';
  m['p'] = 'r';
  m['q'] = 'z';
  m['r'] = 't';
  m['s'] = 'n';
  m['t'] = 'w';
  m['u'] = 'j';
  m['v'] = 'p';
  m['w'] = 'f';
  m['x'] = 'm';
  m['y'] = 'a';
  m['z'] = 'q';
  m[' '] = ' ';
  int n;
  scanf("%i\n", &n);
  char s[200];
  for(int i = 0; i < n; i++)
  {
    gets(s);
    for(int j = 0; j < (int)strlen(s); j++)
      s[j] = m[s[j]];
    printf("Case #%i: %s\n", i+1, s);
  }
  return 0;
}
