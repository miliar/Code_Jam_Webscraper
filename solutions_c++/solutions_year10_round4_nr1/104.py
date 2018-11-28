#include <iostream>
using namespace std;

int main()
{
  freopen("A.in", "r", stdin);
  freopen("A.out", "w", stdout);
  
  int T; cin >> T;
  for (int tcase = 1; tcase <= T; tcase++)
  {
    int N; cin >> N;
    
    char grid[200][200] = {0};
    gets(grid[0]); //read empty
    for (int i = 0; i < N+N-1; i++)
      gets(grid[i]);
      
    bool vsym[200] = {}, hsym[200] = {};
      
    //vertical symmetry
    for (int i = 0; i < N+N-1; i++) //is it symmetrical about the ith row
    {
      bool fail = false;
      for (int col = 0; col < N+N-1; col++)
        for (int j = 0; j < N+N-1; j++)
        {
          unsigned jj = i - (j-i);
          if (jj < N+N-1 && grid[j][col] != grid[jj][col])
            fail |= isdigit(grid[j][col]) && isdigit(grid[jj][col]);
        }
      
        vsym[i] = !fail;
    }
    
    //horiz
    for (int j = 0; j < N+N-1; j++)
    {
      bool fail = false;
      for (int row = 0; row < N+N-1; row++)
        for (int i = 0; i < N+N-1; i++)
        {
          unsigned ii = j - (i-j);
          if (ii < N+N-1 && grid[row][i] != grid[row][ii])
            fail |= isdigit(grid[row][i]) && isdigit(grid[row][ii]);
        }
        
        hsym[j] = !fail;
    }
    
    int mid = N-1;
    int sz = INT_MAX;
    for (int i = 0; i < N+N-1; i++)
      for (int j = 0; j < N+N-1; j++)
        if (vsym[i] && hsym[j])
        {          
          int dist = 0;
          for (int k = 0; k < N+N-1; k++)
            for (int l = 0; l < N+N-1; l++)
              if (isdigit(grid[k][l]))
              {
                dist = max(dist, abs(k-i) + abs(j-l));
              }
          
          sz = min(sz, dist+1);
        }
    
    printf("Case #%d: %d\n", tcase, sz*sz - N*N);
  }
}