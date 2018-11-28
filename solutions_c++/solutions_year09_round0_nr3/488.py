#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <sstream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iomanip>
#include <memory>
#include <cstring>
#include <climits>
#include <cassert>
using namespace std;

#define ALL(a) (a).begin(), (a).end()
#define PB push_back
#define MP make_pair
#define FOR(i, a, b) for(int (i) = (a); (i) <= (b); (i)++)
#define FORD(i, a, b) for(int (i) = (a); (i) >= (b); (i)--)
#define REP(i, n) for (int (i) = 0; (i) < n; (i)++)
#define SIZE(a) (int)(a).size()
#define DBGN(x) cout << #x << " = " << x << endl;
#define DBG(x) cout << #x << " = " << x << ", ";
#define DBGARR(x, n) REP(i, n) cout << #x << '[' << i << "] = " << x[i] << endl;
#define DBGTBL(x, a, b) REP(i, a) REP(j, b) cout << #x << '[' << i << "][" << j << "] = " << x[i][j] << endl;

#define FIN "test.in"
#define FOUT "test.out"

#define MAXL 500
#define TL 19
#define MD 10000

const string text = "welcome to code jam";
int a[MAXL][TL];
string s;

int doit(int start_pos, int text_pos) {
  if (text_pos == TL) {
    return 1;
  } else if (start_pos >= SIZE(s)) {
    return 0;
  }
  if (a[start_pos][text_pos] == -1) {
    a[start_pos][text_pos] = 0;
    int text_remain = TL - text_pos;
    int s_remain = SIZE(s) - start_pos;
    if (text_remain > s_remain)
      goto park;
    FOR(i, start_pos, SIZE(s) - 1)
      if (s[i] == text[text_pos]) {
        a[start_pos][text_pos] += doit(i + 1, text_pos + 1);
        a[start_pos][text_pos] %= MD;
      }
  }
park:
  return a[start_pos][text_pos];
}

int main()
{
    freopen(FIN, "r", stdin);
    freopen(FOUT, "w", stdout);

    int T;
    cin >> T;
    getline(cin, s);
    REP(zzz, T) {
      getline(cin, s);
      REP(i, MAXL) REP(j, TL)
        a[i][j] = -1;
      doit(0, 0);
      printf("Case #%d: %04d\n", zzz + 1, a[0][0]);
    }

    fflush(stdout);
    fclose(stdin);
    fclose(stdout);

    return 0;
}
