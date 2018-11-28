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

#define RES "res.out"
#define FIN "test.in"
#define FOUT "test.out"

int a[1 << 9];

int main()
{
    freopen(RES, "r", stdin);
    REP(i, 1 << 9) {
      int t; cin >> t;
      cin >> a[i];
    }

    freopen(FIN, "r", stdin);
    freopen(FOUT, "w", stdout);

    int T;
    cin >> T;
    string s;
    getline(cin, s);
    REP(zzz, T) {
      getline(cin, s);
      stringstream ss(s);
      int t, mask = 0;
      while (ss >> t) {
        mask += 1 << (t - 2);
      }
      printf("Case #%d: %d\n", zzz + 1, a[mask]);
    }

    fflush(stdout);
    fclose(stdin);
    fclose(stdout);

    return 0;
}
