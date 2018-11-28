#include <cmath>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long lol;

#define sz(c) ((int) (c).size())
#define pb push_back
#define mp make_pair
#define fi first
#define se second

char s[111];
map <char, char> f;

void solve(int testcase)
{
  printf("Case #%d: ", testcase);
  gets(s);
  for (int i=0; s[i]!=0; ++i) {
    assert(isalpha(s[i]) || s[i] == ' ');
    s[i] = f[s[i]];
  }
  puts(s);
}

int main()
{
  f[' '] = ' ';
  f['a'] = 'y';
  f['b'] = 'h';
  f['c'] = 'e';
  f['d'] = 's';
  f['e'] = 'o';
  f['f'] = 'c';
  f['g'] = 'v';
  f['h'] = 'x';
  f['i'] = 'd';
  f['j'] = 'u';
  f['k'] = 'i';
  f['l'] = 'g';
  f['m'] = 'l';
  f['n'] = 'b';
  f['o'] = 'k';
  f['p'] = 'r';
  f['q'] = 'z';
  f['r'] = 't';
  f['s'] = 'n';
  f['t'] = 'w';
  f['u'] = 'j';
  f['v'] = 'p';
  f['w'] = 'f';
  f['x'] = 'm';
  f['y'] = 'a';
  f['z'] = 'q';
  int T;
  scanf("%d\n", &T);
  for (int i = 1; i <= T; ++i) 
    solve(i);
  return 0;
}
