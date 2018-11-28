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
#include <cstring>

typedef unsigned long long ull;

#define FOR(i,n) for (int i=0; i<(n); i++)
#define ALL(v) (v).begin(),(v).end()
#define PV(v) for (int __i=0; __i<(v).size(); __i++) cout << (v)[__i] << " "; cout << endl;

using namespace std;

#define SS 102

int G[SS][SS];
int H[SS][SS];
typedef pair<int,int> coord;

#define EX(S,E) (S.find(E)!=S.end())

int main()
{
  int _N;
  cin >> _N;

  int R;
  int x1,y1,x2,y2;

  for (int _n=0; _n<_N; _n++)
    {
      cout << "Case #" << _n+1 << ": ";

      memset(G,0,SS*SS*sizeof(int));
      memset(H,0,SS*SS*sizeof(int));
 
      cin >> R;
      int mx=0,my=0;
      for (int i=0; i<R; i++)
	{
	  cin >> x1 >> y1 >> x2 >> y2;
	  for (int x=x1; x<=x2; x++)
	    for (int y=y1; y<=y2; y++)
	      {
		G[x][y]=1;
		mx=max(mx,x);
		my=max(my,y);
	      }
	}

      int ret=0;
      int alive;

      while (1)
	{
	  alive=0;
	  for (int x=1; x<=mx; x++)
	    {
	      for (int y=1; y<=my; y++)
		{
		  if (G[x-1][y]==0 && G[x][y-1]==0)
		    H[x][y]=0;
		  else if (G[x-1][y]==1 && G[x][y-1]==1)
		    H[x][y]=1;
		  else
		    H[x][y]=G[x][y];

		  if (H[x][y])
		    alive=1;
		}
	    }
	  //	  G=H;
	  memcpy(G,H,SS*SS*sizeof(int));
	  ret++;

	  if (!alive)
	    break;
	}

      cout << ret;

      cout << endl;
    }

  return 0;
}
