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

char grid[10][10];

int main(void)
{
  int NUM_CASES;
  cin >> NUM_CASES;
  for (int c = 1; c <= NUM_CASES; c++) {
    int M, N;
    cin >> M >> N;
    vector <int> masks(M);
    for (int i = 0; i < M; i++)
      for (int j = 0; j < N; j++) {
	cin >> grid[i][j];
	if (grid[i][j] == 'x')
	  masks[i] |= 1<<j;
      }
    int N2 = 1<<N;
    vector < vector <int> > best(M, N2);
    vector < vector <int> > pop(M, N2);
    vector < vector <int> > next(M, N2);
    for (int i = 0; i < M; i++)
      for (int m = 0; m < N2; m++) {
	if ((m&masks[i]) == 0) {
	  bool good = true;
	  for (int j = 0; j < N-1; j++)
	    if (((m>>j)&3) == 3)
	      good = false;
	  if (good)
	    pop[i][m] = __builtin_popcount(m);
	  else
	    pop[i][m] = -1;
	}
	else
	  pop[i][m] = -1;
	for (int j = 0; j < N; j++)
	  if ((m>>j)&1) {
	    if (j > 0)
	      next[i][m] |= 1<<(j-1);
	    if (j+1 < N)
	      next[i][m] |= 1<<(j+1);
	  }
      }
    for (int m = 0; m < N2; m++)
      best[0][m] = pop[0][m];
    for (int i = 1; i < M; i++)
      for (int m = 0; m < N2; m++)
	if (pop[i-1][m] >= 0)
	  for (int m2 = 0; m2 < N2; m2++)
	    if (pop[i][m2] >= 0 && (next[i-1][m]&m2) == 0)
	      best[i][m2] >?= best[i-1][m] + pop[i][m2];
    int ans = 0;
    for (int m = 0; m < N2; m++)
      ans >?= best[M-1][m];
    cerr << c << " " << ans << endl;
    printf("Case #%d: %d\n", c, ans);
  }
}
