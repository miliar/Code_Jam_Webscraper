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

const int w[9][2] = {{0,0},{0,1},{0,2},{1,0},{1,1},{1,2},{2,0},{2,1},{2,2}};

int main() {
  int cases;
  cin >> cases;
  for (int cs = 1; cs <= cases; cs++) {
    long long n, a, b, c, d, xx, yy, m;
    cin >> n >> a >> b >> c >> d >> xx >> yy >> m;

    long long p[3][3];
    CLEAR(p);
    FOR(i, 0, n) {
      p[xx%3][yy%3]++;
      xx = (a*xx+b) % m;
      yy = (c*yy+d) % m;
    }

    long long res = 0;
    FOR(i, 0, 9)
      FOR(j, i, 9)
        FOR(k, j, 9)
          if ((w[i][0]+w[j][0]+w[k][0])%3==0 && (w[i][1]+w[j][1]+w[k][1])%3==0) {
#define q(i) p[w[i][0]][w[i][1]]
            if (i == k)
              res += q(i)*(q(i)-1)*(q(i)-2)/6;

            else if (i == j)
              res += q(i)*(q(i)-1)/2 * q(k);

            else if (j == k)
              res += q(i) * q(j)*(q(j)-1)/2;

            else
              res += q(i) * q(j) * q(k);
          }


    cout << "Case #" << cs << ": " << res << endl;
  }
}
