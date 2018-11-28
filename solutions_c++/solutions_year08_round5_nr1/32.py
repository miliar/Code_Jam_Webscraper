#include <string>
#include <vector>
#include <cmath>
#include <cctype>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <utility>
#include <numeric>
#include <complex>

using namespace std;

int dx[] = {1, 0, -1, 0};
int dy[] = {0, 1, 0, -1};

int main(void)
{
  int NUM_CASES;
  cin >> NUM_CASES;
  for (int c = 1; c <= NUM_CASES; c++) {
    int L;
    cin >> L;
    int x = 3003, y = 3003, k = 1;
    int area2 = 0;
    vector <int> rows(6006, 6006), Rows(6006, 0),
      cols(6006, 6006), Cols(6006, 0);
    for (int l = 0; l < L; l++) {
      string S; int T;
      cin >> S >> T;
      int slen = S.length();
      for (int t = 0; t < T; t++)
	for (int s = 0; s < slen; s++) {
	  if (S[s] == 'L')
	    k = (k+1)%4;
	  else if (S[s] == 'R')
	    k = (k+3)%4;
	  else {
	    if (k == 0) {
	      cols[x] <?= y; Cols[x] >?= y;
	    }
	    else if (k == 1) {
	      rows[y] <?= x; Rows[y] >?= x;
	    }
	    else if (k == 2) {
	      cols[x-1] <?= y; Cols[x-1] >?= y;
	    }
	    else {
	      rows[y-1] <?= x; Rows[y-1] >?= x;
	    }
	    int nx = x+dx[k], ny = y+dy[k];
	    area2 += x*ny-y*nx;
	    x = nx; y = ny;
	  }
	}
    }
    cerr << x << " " << y << " ";
    area2 = abs(area2 / 2);
    cerr << area2 << " ";
    int areatot = 0;
    for (int x = 0; x < 6006; x++)
      for (int y = 0; y < 6006; y++)
	if (cols[x] <= y && y < Cols[x] || rows[y] <= x && x < Rows[y])
	  areatot++;
    cerr << areatot << " ";
    cerr << c << endl;
    int ans = areatot - area2;
    printf("Case #%d: %d\n", c, ans);
  }
}
