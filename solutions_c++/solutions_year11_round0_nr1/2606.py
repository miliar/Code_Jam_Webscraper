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

#define REP(i, n) for (int (i) = 0; (i) < (n); ++(i))
#define FOR(i, s, n) for (int (i) = (s); (i) < (n); ++(i))

using namespace std;
typedef long long ll;
typedef double dbl;
typedef pair<int, int> pii;


int main()
{
  freopen("a.in", "rt", stdin);
  freopen("a.out", "wt", stdout);

  int T;
  cin >> T;
  REP(ti, T)
  {
    int n;
    cin >> n;
    vector<int> seq[2], turns;
    REP(i, n)
    {
      string s;
      int x;
      cin >> s >> x;
      turns.pb(s != "O");
      seq[turns.back()].pb(x);
    }

    
    int ptr[2] = {0, 0};
    int pos[2] = {1, 1};
    int ans = 0;
    for (int t = 0; t < sz(turns); )
    {
      int turn = turns[t];
//      printf("robot #%d", turn);

      int need = abs(pos[turn] - seq[turn][ptr[turn]]);
      int cnt = max(1, need);
      if (need == 0)
      {
//        printf(" press #%d button", pos[turn]);
        ptr[turns[t++]]++;
      }
      else
      {
//        printf(" goes to %d coord", seq[turn][ptr[turn]]);
        pos[turn] = seq[turn][ptr[turn]];
      }

      turn = 1 - turn;
      if (ptr[turn] < sz(seq[turn]))
      {
        int from = pos[turn];
        int to = seq[turn][ptr[turn]];
        int need = abs(to - from);
        if (need > 0)
        {
          pos[turn] += min(cnt, need) * ((to - from) / need);
//          printf(", while robot #%d goes to %d coord\n", turn, pos[turn]);
        }
      }
//      printf("\n");
      ans += cnt;
    }
    printf("Case #%d: %d\n", ti + 1, ans);
  }

  return 0;
}
