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

#define FOR(i,n) for (int i=0; i<(n); i++)
#define ALL(v) (v).begin(),(v).end()
#define PV(v) for (int __i=0; __i<(v).size(); __i++) cout << (v)[__i] << " "; cout << endl;

using namespace std;

typedef struct chicken
{
  int x;
  int v;
} chicken;

int main()
{
  int _N;
  cin >> _N;

  int N,K,B,T;

  chicken *chicks;

  for (int _n=0; _n<_N; _n++)
    {
      cout << "Case #" << _n+1 << ": ";

      cin >> N >> K >> B >> T;

      chicks=new chicken[N];

      for (int i=0; i<N; i++)
	{
	  cin >> chicks[i].x;
	}
      for (int i=0; i<N; i++)
	{
	  cin >> chicks[i].v;
	}

      int toswap=0;
      int ok=0;
      int ret=0;
      for (int i=N-1; i>=0; i--)
	{
	  if ((B-chicks[i].x) <= T*chicks[i].v)
	    {
	      ok++;
	      ret+=toswap;
	    }
// 	  else if ((B-chicks[i].x)/chicks[i].v == T)
// 	    {
// 	      ok++;
// 	      ret+=toswap;
// 	      toswap++;
// 	    }
	  else
	    toswap++;

	  if (ok==K)
	    break;
	}

      if (ok==K)
	cout << ret;
      else
	cout << "IMPOSSIBLE";

      cout << endl;

      delete[] chicks;
    }

  return 0;
}
