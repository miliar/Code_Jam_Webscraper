#include <iostream>
#include <sstream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

bool grid[311][311];
bool grid2[311][311];

int main()
{
  freopen("C.in", "r", stdin);
  freopen("C.out", "w", stdout);
  
	int n_cases; cin >> n_cases;
	for (int tcase = 1; tcase <= n_cases; tcase++)
	{
    memset(grid, 0, sizeof grid);
    int R; cin >> R;
    for (int i = 0; i < R; i++)
    {
      int x1, x2, y1, y2;
      cin >> x1 >> y1 >> x2 >> y2;
      for (int x = x1; x <= x2; x++)
        for (int y = y1; y <= y2; y++)
          grid[x][y] = true;
    }
    
    int rep = 0;
    while (true)
    {
      rep++;
      memset(grid2, 0, sizeof grid2);
      for (int i = 1; i <= 300; i++)
        for (int j = 1; j <= 300; j++)
        {
          if (grid[i][j])
          {
            if (!grid[i-1][j] && !grid[i][j-1])
              grid2[i][j] = false;
            else
              grid2[i][j] = true;
          }
          else
            grid2[i][j] = grid[i-1][j] && grid[i][j-1];
        }
      
        bool emp = true;
        for (int i = 1; i <= 300; i++)
          for (int j = 1; j <= 300; j++)
          {
            grid[i][j] = grid2[i][j];
            if (grid[i][j]) emp = false;
            if (grid[i][j] && (i == 300 || j == 300)) throw;
          }
      
          if (emp) break;
    }
    
		printf("Case #%d: %d\n", tcase, rep);
	}

	return 0;
}