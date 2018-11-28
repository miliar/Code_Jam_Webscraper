#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstring>
#include <cassert>
#include <cstdlib>
#include <ctime>
#include <cmath>

#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <set>

#define sz(c) ((int)(c).size())
#define pb push_back
#define mp make_pair

#define REP(i, n) for (int i = 0; i < (n); ++i)
#define FOR(i, s, n) for (int i = (s); i < (n); ++i)

using namespace std;
typedef long long ll;
typedef double dbl;
typedef pair<int, int> pii;


int main()
{
  freopen("b.in", "rt", stdin);
  freopen("b.out", "wt", stdout);

  int Tests, C, D;
  cin >> Tests;
  REP(testIt, Tests)
  {
    vector<vector<char> > comb(26, vector<char>(26, 0));
    vector<vector<char> > opp(26);

    cin >> C;
    string s;
    REP(i, C)
    {
      cin >> s;
      assert(sz(s) == 3);
      comb[s[0] - 'A'][s[1] - 'A'] = comb[s[1] - 'A'][s[0] - 'A'] = s[2];
    }

    cin >> D;
    REP(i, D)
    {
      cin >> s;
      assert(sz(s) == 2);
      opp[s[0] - 'A'].pb(s[1]);
      opp[s[1] - 'A'].pb(s[0]);
    }

    int n;
    cin >> n >> s;
    assert(n == sz(s));

    vector<char> st;
    map<char, int> cnt;
    REP(i, sz(s))
    {
//      printf("! %c\n", s[i]);
      if (sz(st) > 0 && comb[s[i] - 'A'][st.back() - 'A'] != 0)
      {
        cnt[st.back()]--;
        st.back() = comb[s[i] - 'A'][st.back() - 'A'];
      }
      else
      {
        bool needClear = false;
        for (vector<char>::iterator j = opp[s[i] - 'A'].begin(); j != opp[s[i] - 'A'].end(); ++j)
          if (cnt[*j] > 0)
          {
            needClear = true;
            break;
          }
        if (needClear)
        {
          st.resize(0);
          cnt.clear();
        }
        else
        {
          st.pb(s[i]);
          cnt[s[i]]++;
        }
      }
    }

    printf("Case #%d: [", testIt + 1);
    REP(i, sz(st))
      printf("%c%s", st[i], (i + 1 == sz(st) ? "" : ", "));
    printf("]\n");
  }

  return 0;
}
