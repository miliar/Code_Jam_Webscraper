#include <cstdio>
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
#define REP(i, end) for(int i = 0; i < (end); i++)
#define CLEAR(arr) memset(arr, 0, sizeof(arr))
#define ALL(cont) (cont).begin(),(cont).end()

char a[100][100];
double owp[100];
double rpi[100];

int main() {
  int cases;
  scanf("%d", &cases);
  for (int cs = 1; cs <= cases; cs++) {
      int n;
      scanf("%d ", &n);
      REP(r, n)
	  REP(c, n) 
	    scanf("%c ", &a[r][c]);

      REP(i, n) {
	  double p = 0;
	  double q = 0;
	  REP(j, n)
	      if (a[i][j] != '.') {
		  double x = 0;
		  double y = 0;
		  REP(k, n)
		      if (k != i) {
			  if (a[j][k] == '1')
			      x += 1;
			  if (a[j][k] != '.')
			      y += 1;
		      }
		  p += x/y;
		  q += 1;
	      }
	  owp[i] = p/q;
      }

      REP(i, n) {
	  double p = 0;
	  double q = 0;
	  REP(j, n) {
	      if (a[i][j] == '1')
		  p += 1;
	      if (a[i][j] != '.') {
		  p += owp[j];
		  q += 1;
	      }
	  }
	  rpi[i] = 0.25*p/q+0.5*owp[i];
      }

    printf("Case #%d:\n", cs);
    REP(i, n)
	printf("%.9lf\n", rpi[i]);
  }
}
