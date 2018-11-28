#include <algorithm>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <vector>
#include <sstream>

#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>

#define REP(i, n) for(int i=0; i<(int)n; ++i)
#define FOR(i, c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define ALL(c) (c).begin(),(c).end()
#define each(i, c) FOR(i, c)

#define VAR(a) cout << #a << " : " << a << endl;

typedef long long int lli;

using namespace std;

int main(int argc, char *argv[])
{
  map<char, char> conv;
conv['a'] = 'y';
conv['b'] = 'h';
conv['c'] = 'e';
conv['d'] = 's';
conv['e'] = 'o';
conv['f'] = 'c';
conv['g'] = 'v';
conv['h'] = 'x';
conv['i'] = 'd';
conv['j'] = 'u';
conv['k'] = 'i';
conv['l'] = 'g';
conv['m'] = 'l';
conv['n'] = 'b';
conv['o'] = 'k';
conv['p'] = 'r';
conv['q'] = 'z';
conv['r'] = 't';
conv['s'] = 'n';
conv['t'] = 'w';
conv['u'] = 'j';
conv['v'] = 'p';
conv['w'] = 'f';
conv['x'] = 'm';
conv['y'] = 'a';
conv['z'] = 'q';

  int tc;
  string s;
  cin >> tc;
  getline(cin, s);
  while (tc--) {
    getline(cin, s);    
    static int cnt = 0;
    cout << "Case #" << ++cnt << ": ";
    for (int i = 0; i < (int)s.size(); ++i) {
      if ('a' <= s[i] && s[i] <= 'z') {
        cout << conv[s[i]];
      } else {
        cout << s[i];
      }
    } 
    cout << endl;   
  }
  return 0;
}
