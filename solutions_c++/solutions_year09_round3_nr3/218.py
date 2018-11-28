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
#include <climits>

typedef unsigned long long ull;

#define FOR(i,n) for (int i=0; i<(n); i++)
#define ALL(v) (v).begin(),(v).end()
#define PV(v) for (int __i=0; __i<(v).size(); __i++) cout << (v)[__i] << " "; cout << endl;

using namespace std;

int rel[100];
char occ[10000];

int fact(int x)
{
  int ret=1;
  for (int i=2; i<=x; i++)
    ret*=i;

  return ret;
}

int main()
{
  int _N;
  cin >> _N;

  int P,Q;

  for (int _n=0; _n<_N; _n++)
    {
      cout << "Case #" << _n+1 << ": ";

      cin >> P >> Q;
      memset(occ,1,P*sizeof(char));
      for (int i=0; i<Q; i++)
	{
	  cin >> rel[i];
	  rel[i]--;
	}

      int sol=INT_MAX;
      for (int i=0; i<fact(Q); i++)
	{
	  int sol1=0;
	  memset(occ,1,P*sizeof(char));
	  for (int j=0; j<Q; j++)
	    {
	      occ[rel[j]]=0;
	      for (int i=rel[j]-1; i>=0; i--)
		{
		  if (occ[i])
		    sol1++;
		  else
		    break;
		}
	      for (int i=rel[j]+1; i<P; i++)
		{
		  if (occ[i])
		    sol1++;
		  else
		    break;
		}
	    }
	  sol=min(sol,sol1);

	  next_permutation(rel,rel+Q);
	}

      cout << sol;

      cout << endl;
    }

  return 0;
}
