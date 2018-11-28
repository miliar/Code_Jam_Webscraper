
#include <cstring>
#include <cstdio>

const int N = 64;

char board[N][N];
char rotate[N][N];
int r_len[N];

int dx[] = {0, 1, 1, 1};
int dy[] = {1, 1, 0, -1};

int check(int n, int k, int x, int y)
{
  for (int d = 0; d < 4; d++)
    {
      int kk;
      int xx = x, yy = y;
      for (kk = 0; kk < k - 1; kk++)
	{
	  xx += dx[d];
	  yy += dy[d];

	  if (xx >= n || yy >= n || yy < 0)
	    break;
	  if (yy >= r_len[xx])
	    break;

	  if (rotate[xx][yy] != rotate[x][y])
	    break;
	}

      if (kk >= k - 1)
	return 1;
    }

  return 0;
}

int solve(int n, int k)
{
  for (int i = n - 1; i >= 0; i--)
    {
      int ii = n - 1 - i;
      r_len[ii] = 0;

      for (int j = n - 1; j >= 0; j--)
	{
	  if (board[i][j] != '.')
	    rotate[ii][r_len[ii]++] = board[i][j];
	}

      rotate[ii][r_len[ii]] = '\0';
    }

  //debug
  /*
  putchar('\n');
  for (int i = 0; i < n; i++)
    printf("%s\n", rotate[i]);
  */

  bool red = false, blue = false;

  for (int i = 0; i < n; i++)
    for (int j = 0; j < r_len[i]; j++)
      {
	if (check(n, k, i, j))
	  {
	    if (rotate[i][j] == 'R')
	      red = true;
	    else
	      blue = true;
	  }
      }

  if (red && blue)
    printf("Both\n");
  else
    {
      if (red)
	printf("Red\n");
      else if (blue)
	printf("Blue\n");
      else
	printf("Neither\n");
    }

  return 0;
}

int main()
{
  int T;
  scanf("%d", &T);

  for (int t = 1; t <= T; t++)
    {
      int n, k;
      scanf("%d%d", &n, &k);

      for (int i = 0; i < n; i++)
	scanf("%s", board[i]);

      printf("Case #%d: ", t);
      solve(n, k);
    }

  return 0;
}
