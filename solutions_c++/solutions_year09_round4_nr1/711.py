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
#include <list>
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

vector< vector<int> > a;

int main()
{
  freopen(FIN, "r", stdin);
  freopen(FOUT, "w", stdout);

  int T;
  cin >> T;
  REP(zzz, T) {
    int N;
    cin >> N;
    a.clear();
    a.resize(N);
    REP(i, N) {
      a[i].resize(N);
      string s;
      cin >> s;
      REP(j, N) a[i][j] = ((s[j] == '1') ? 1 : 0);
    }
    int cnt = 0;
    REP(i, N) {
      FOR(j, i, N-1) {
        bool ok = true;
        FOR(k, i+1, N-1) {
          if (a[j][k] == 1) {
            ok = false;
            break;
          }
        }
        if (ok) {
          FORD(k, j, i+1) {
            swap(a[k], a[k-1]);
            ++cnt;
          }
          break;
        }
      }
    }
    printf("Case #%d: %d\n", zzz + 1, cnt);
  }


  fclose(stdin);
  fflush(stdout);
  fclose(stdout);
  return 0;
}
