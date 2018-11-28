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
using namespace std;

#define ALL(a) (a).begin(), (a).end()
#define PB push_back
#define MP make_pair
#define FOR(i, a, b) for(int (i) = (a); (i) <= (b); (i)++)
#define FORD(i, a, b) for(int (i) = (a); (i) >= (b); (i)--)
#define REP(i, n) for (int (i) = 0; (i) < n; (i)++)
#define SIZE(a) (int)(a).size()
#define DBG(x) cout << #x << " = " << x << endl;
#define DBGARR(x, n) REP(i, n) cout << #x << '[' << i << "] = " << x[i] << endl;
#define DBGTBL(x, a, b) REP(i, a) REP(j, b) cout << #x << '[' << i << "][" << j << "] = " << x[i][j] << endl;

#define FIN "test.in"
#define FOUT "test.out"

#define MAXN 500
#define MAXL 15

int matches[MAXN];
int patterns[MAXN][MAXL][26];

int main()
{
    freopen(FIN, "r", stdin);
    freopen(FOUT, "w", stdout);

    memset(matches, 0, sizeof(matches));
    memset(patterns, 0, sizeof(patterns));

    int L, D, N;
    cin >> L >> D >> N;
    vector<string> words(D);
    REP(i, D) cin >> words[i];
    REP(i, N) {
      string s = "";
      cin >> s;
      int current_token = 0;
      bool inside = false;
      REP(j, SIZE(s)) {
        if (s[j] == '(') {
          inside = true;
        } else if (s[j] == ')') {
          inside = false;
          ++current_token;
        } else {
          patterns[i][current_token][s[j] - 'a'] = 1;
          if (!inside)
            ++current_token;
        }
      }
    }
    REP(i, D) {
      REP(j, N) {
        bool ok = true;
        REP(k, L) {
          if (!patterns[j][k][words[i][k] - 'a']) {
            ok = false;
            break;
          }
        }
        if (ok)
          ++matches[j];
      }
    }

    REP(i, N)
      printf("Case #%d: %d\n", i + 1, matches[i]);

    fflush(stdout);
    fclose(stdin);
    fclose(stdout);

    return 0;
}
