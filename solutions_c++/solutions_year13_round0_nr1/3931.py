#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cmath>
#include <ctime>
#include <cstring>
#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <algorithm>

#define sz(c) ((int)(c).size())
#define all(c) (c).begin(), (c).end()
#define mp make_pair

using namespace std;
typedef long long ll;

bool Check( vector<string> const& s, char c, int x, int y, int dx, int dy )
{
  for (int i = 0; i < 4; i++, x += dx, y += dy)
    if (s[y][x] != 'T' && s[y][x] != c)
      return false;
  printf("%c won\n", c);
  return true;
}

void testCase()
{
  int const n = 4;
  vector<string> s(n);
  for (int i = 0; i < n; i++)
    getline(cin, s[i]);
  for (int i = 0; i < 4; i++)
    cerr << s[i] << endl;

  char pl[] = {'X', 'O'};
  for (int pi = 0; pi < 2; pi++)
  {
    for (int i = 0; i < 4; i++)
      if (Check(s, pl[pi], i, 0, 0, 1) || Check(s, pl[pi], 0, i, 1, 0))
        return;
    if (Check(s, pl[pi], 0, 0, 1, 1) || Check(s, pl[pi], 0, 3, 1, -1))
      return;
  }

  for (int i = 0; i < 4; i++)
    for (int j = 0; j < 4; j++)
      if (s[i][j] == '.')
      {
        printf("Game has not completed\n");
        return;
      }
  printf("Draw\n");
}

int main() {
//  freopen("sample.in", "rt", stdin);
//  freopen("output.txt", "wt", stdout);
  int n;
  cin >> n;
  string s;
  getline(cin, s);
  for (int ti = 0; ti < n; ++ti) {
    printf("Case #%i: ", ti + 1);
    testCase();
    getline(cin, s);
  }
  return 0;
}
