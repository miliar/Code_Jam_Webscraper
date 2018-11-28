#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <set>
#include <vector>
#include <list>
#include <algorithm>
#include <cmath>
#include <cfloat>
#include <string>

typedef unsigned long long ull;

int mod=10007;
bool rock[100][100];
int sol[100][100];
  int H,W,R;

using namespace std;

int count(int i, int j)
{
  int ret=0;
  if (i==H-1 && j==W-1)
    {
      return 1;
    }
  else
    {
      if (sol[i][j]==-1)
	{
	  if (i+2<H && j+1<W && !rock[i+2][j+1])
	    {
	      ret+=(count(i+2,j+1))%mod;
	    }
	  if (i+1<H && j+2<W && !rock[i+1][j+2])
	    {
	      ret+=(count(i+1,j+2))%mod;
	    }
	  return sol[i][j]=ret%mod;
	}
      else
	return sol[i][j];
    }
}

int main()
{
  int _N;
  cin >> _N;

  for (int _n=0; _n<_N; _n++)
    {
      cout << "Case #" << _n+1 << ": ";

      cin >> H >> W >> R;

      for (int i=0; i<H; i++)
	{
	  for (int j=0; j<W; j++)
	    {
	      rock[i][j]=false;
	      sol[i][j]=-1;
	    }
	}

      int r,c;
      for (int i=0; i<R; i++)
	{
	  cin >> r >> c;
	  rock[r-1][c-1]=true;
	}

      cout << count(0,0);

      cout << endl;
    }

  return 0;
}
