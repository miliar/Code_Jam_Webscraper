#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

#define filename "C-small-attempt0"

int grid[128][128];

int main()
{
  freopen (filename ".in", "rt", stdin);
  freopen (filename ".out", "wt", stdout);
  
  int T;
  cin >> T;
  for (int test = 1; test <= T; ++test) {
	  memset (grid, 0, sizeof (grid));
	  int r, x1, x2, y1, y2;
	  cin >> r;
	  for (int i = 0; i < r; ++i) {
			  cin >> x1 >> y1 >> x2 >> y2;
			  for (int x = x1; x <= x2; ++x)
				  for (int y = y1; y <= y2; ++y)
					  grid[x][y] = 1;
	  }
	  int ans = 0;
	  while (true) {
		  bool ok = false;
		  for (int i = 1; i <= 100; ++i)
			  for (int j = 1; j <= 100; ++j)
				  if (grid[i][j] == 1)
					  ok = true;
		  if (!ok) break;
		  for (int i = 100; i > 0; --i)
			  for (int j = 100; j > 0; --j)
				  if (grid[i][j] == 1) {
					  if (grid[i-1][j] == 0 && grid[i][j-1] == 0)
						  grid[i][j] = 0;
				  } else {
					  if (grid[i-1][j] == 1 && grid[i][j-1] == 1)
						  grid[i][j] = 1;
				  }
		  ++ans;
	  }
      cout << "Case #" << test << ": " << ans << endl;
  }

  return 0;
}