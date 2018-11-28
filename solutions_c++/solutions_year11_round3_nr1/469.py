#include <iostream>
#include <cstdio>
using namespace std;

char c[55][55];
int n, m;
int dx[] = {0, 0, +1, +1};
int dy[] = {0, +1, 0, +1};

void solve ()
{
  
  scanf ("%d%d\n", &n, &m);
  
  int i, j, k;
  
  for (i =0; i < n; i ++)
  {
    for (j =0; j < m; j ++)
      scanf ("%c", &c[i][j]);
    getchar ();
  }
  
  char buf[] = {'/',  '\\', '\\', '/'};
  
  for (i = 0; i< n; i ++)
    for (j = 0; j < m; j ++)
    {
      if (c[i][j] == '#')
      {
	if (i == n-1|| j == m-1)
	{
	  printf ("Impossible\n");
	  return;
	}
	for (k = 0; k < 4; k ++)
	{
	  if (c[i + dx[k]][j + dy[k]] != '#')
	  {
	    printf ("Impossible\n");
	    return; 
	  }
	  c[i + dx[k]][j + dy[k]] = buf[k]; 
	}
      }
    }
  
  for (i =0; i < n; i ++)
  {
    for (j =0; j < m; j ++)
      printf ("%c", c[i][j]);
    printf ("\n");
    
  }
  
}

int main ()
{
  int t; 
  scanf ("%d", &t);
  
  for (int i = 1; i <=t; i ++)
  {
    printf ("Case #%d:\n", i);
    solve ();
  }
  
  
  return 0;
}