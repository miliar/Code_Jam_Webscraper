#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <memory.h>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

typedef long double Double;
typedef vector<int> VInt;
typedef vector< vector<int> > VVInt;
typedef long long Int;
typedef pair<int, int> PII;

#define FOR(i, n, m) for(i = n; i < m; ++i)
#define RFOR(i, n, m) for(i = (n) - 1; i >= (m); --i)
#define CLEAR(x, y) memset(x, y, sizeof(x))
#define COPY(x, y) memcpy(x, y, sizeof(x))
#define PB push_back
#define MP make_pair
#define SIZE(v) ((int)((v).size()))
#define ALL(v) (v).begin(), (v).end()

char Sub[256] = {0};

char S[1010];

int main()
{
  Sub['o'] = '0';
  Sub['i'] = '1';
  Sub['e'] = '3';
  Sub['a'] = '4';
  Sub['s'] = '5';
  Sub['t'] = '7';
  Sub['b'] = '8';
  Sub['g'] = '9';

  int T, t;
  scanf("%d", &T);
  for (t = 0; t < T; ++t) {
    set<string> Set;
    int K;
    scanf("%d", &K);
    scanf("%s", S);
    for (int i = 0; S[i+1]; ++i) {
      string s;
      s.PB(S[i]);
      s.PB(S[i+1]);
      Set.insert(s);
      if (Sub[s[0]]) {
        s[0] = Sub[s[0]];
        Set.insert(s);
        if (Sub[s[1]]) {
          s[1] = Sub[s[1]];
          Set.insert(s);
        }
      }
      s[0] = S[i];
      s[1] = S[i+1];
      if (Sub[s[1]]) {
        s[1] = Sub[s[1]];
        Set.insert(s);
      }
    }

    int res = Set.size();
    vector<string> vs(ALL(Set));
    /*
    for (int i = 0; i < vs.size(); ++i)
      printf("=== %s\n", vs[i].c_str());
    */
    int chains = 0;
    for (char c = 'a'; c <= 'z'; ++c) {
      int in, out;
      in = out = 0;
      for (int i = 0; i < vs.size(); ++i) {
        if (vs[i][0] == c)
          ++out;
        if (vs[i][1] == c)
          ++in;
      }
      if (out > in)
        chains += out - in;
    }
    for (char c = '0'; c <= '9'; ++c) {
      int in, out;
      in = out = 0;
      for (int i = 0; i < vs.size(); ++i) {
        if (vs[i][0] == c)
          ++out;
        if (vs[i][1] == c)
          ++in;
      }
      if (out > in)
        chains += out - in;
    }
    if (chains == 0)
      chains = 1;
    res += chains;

    printf("Case #%d: %d\n", t+1, res);
  }

  return 0;
};
