#include<cstdio>
#include<cstring>

char map[50][50];
int N, K;
int dirs[4][2] = {{0, 1}, {1, 0}, {1, 1}, {1, -1}};

bool testit(int i, int j, char c, int di, int dj)
{
  for (int k = 0 ; ; k++)
    {
      if (map[i][j] != c)
	return false;
      if (k == K - 1)
	return true;
      i += di;
      j += dj;
      if (i < 0 || i >= N || j < 0 || j >= N)
	  return false;
    }
}

int main()
{
  int T;
  scanf("%d", &T);
  for (int t = 1 ; t <= T ; t++)
    {
      memset(map, 0, sizeof(map));
      scanf("%d%d", &N, &K);
      for (int i = 0 ; i < N ; i++)
	for (int j = 0 ; j < N ; j++)
	  {
	    int c;
	    do {
	      c = getchar();
	    } while (c != '.' && c!= 'R' && c!='B');
	    map[i][j] = c;
	  }
      /*      for (int i = 0 ; i < N ; i++)
	{
	  for (int j = 0 ; j < N ; j++)
	    putchar(map[i][j] ? map[i][j] : '.');
	  putchar('\n');
	  }*/
      for (int i = 0 ; i < N ; i++)
	{
	  int jw = N - 1;
	  for (int j = N - 1 ; j >= 0 ; j--)
	    {
	      if (map[i][j] == 'R' || map[i][j] == 'B')
		{
		  if (j < jw)
		    {
		      map[i][jw] = map[i][j];
		      map[i][j] = 0;
		    }
		  jw--;		  
		}
	    }
	}/*
      for (int i = 0 ; i < N ; i++)
	{
	  for (int j = 0 ; j < N ; j++)
	    putchar(map[i][j] ? map[i][j] : '.');
	  putchar('\n');
	  }*/
      bool B = false, R = false;
      for (int i = 0 ; i < N ; i++)
	for (int j = 0 ; j < N ; j++)
	  for (int d = 0 ; d < 4 ; d++)
	    {
	      R = R || testit(i, j, 'R', dirs[d][0], dirs[d][1]);
	      B = B || testit(i, j, 'B', dirs[d][0], dirs[d][1]);
	    }
      printf("Case #%d: ", t);
      if (B)
	puts(R ? "Both" : "Blue");
      else
	puts(R ? "Red" : "Neither");
    }
}
