#include <iostream>
#include <sstream>
#include <algorithm>
#include <iterator>
#include <numeric>

#include <cmath>
#include <cctype>

#include <string>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>

using namespace std;

#define FOREACH(iter, cont) for(__typeof((cont).begin()) iter = (cont).begin(); iter != (cont).end(); iter++)
#define FOR(i, begin, end) for(int i = (begin); i < (end); i++)
#define CLEAR(arr) memset(arr, 0, sizeof(arr))
#define ALL(cont) (cont).begin(),(cont).end()

const int INF = 999999999;

const int maxs = 105;
const int maxq = 1005;

int a[maxq][maxs];
int s, q;

int main() {
  int cases;
  cin >> cases;
  for (int cs = 1; cs <= cases; cs++) {
    cin >> s >> ws;
    vector<string> eng(s);
    FOR(i, 0, s) 
      getline(cin, eng[i]);

    cin >> q >> ws;
    vector<string> qry(q);
    FOR(i, 0, q)
      getline(cin, qry[i]);

    CLEAR(a[0]);
    FOR(i, 0, q) 
      FOR(j, 0, s) {
        if (qry[i] == eng[j])
          a[i+1][j] = INF;
        else {
          a[i+1][j] = a[i][j];
          FOR(k, 0, s)
            if (k != j)
              a[i+1][j] <?= 1+a[i][k];
        }
      }

    int res = INF;
    FOR(j, 0, s)
      res <?= a[q][j];

    cout << "Case #" << cs << ": " << res << endl;
  }
}
