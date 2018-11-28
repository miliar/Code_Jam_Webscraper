#include <fstream>
#include <iostream>
using namespace std;

char a[80][80];
int f[80][80];
bool flag[80][80];
int m, n, matching;

int dy[6] = {-1, 0, 1, -1, 0, 1};
int dx[6] = {-1, -1, -1, 1, 1, 1};

ofstream out("c.out");
int augment( int y, int x )
{
  if (flag[y][x]) return 0;
  flag[y][x] = true;
  for (int i=0; i<6; i++)
    {
      int yy = y + dy[i];
      int xx = x + dx[i];
      if (yy<0 || yy>=m || xx < 0 || xx >= n) continue;
      if (a[yy][xx] == 'x') continue;
      if (f[yy][xx] == -1) 
	{
	  f[yy][xx] = 5-i;	  
	  return 1;
	}
      else 
	{
	  int d = f[yy][xx];
	  int t = augment(yy+dy[d], xx+dx[d]);
	  if (t == 1) 
	    {
	      f[yy][xx] = 5-i;
	      return 1;
	    }
	}
    }
  return 0;
} 

int main()
{
  int i, j;
  int c; cin >> c;
  for (int lp=1; lp<=c; lp++)
    {
      cin >> m >> n;
      for (i=0; i<m; i++)
	cin >> a[i];
      for (i=0; i<m; i++)
	for (j=0; j<n; j++)
	  f[i][j] = -1;
      matching = 0;
      for (j=0; j<n; j += 2)
	{
	  for (i=0; i<m; i++)
	    if (a[i][j] == '.')
	      {
		int k, l;
		for (k=0; k<m; k++)
		  for (l=0; l<n; l++)
		    flag[k][l] = false;
		matching += augment(i, j);
	      }
	}
      int minus = 0;
      for (i=0; i<m; i++)
	for (j=0; j<n; j++)
	  if (a[i][j] == 'x') minus++;
      out << "Case #" << lp << ": " << n*m-matching-minus << endl; 
    }
  out.close();
  return 0;
}
