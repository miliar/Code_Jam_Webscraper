#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <vector>
#include <list>
#include <algorithm>

typedef unsigned long long ull;

using namespace std;

ull divceil(ull A, ull X)
{
  if (A%X==0)
    return A/X;
  else
    return A/X+1;
}

int main()
{
  int _N;
  cin >> _N;

  ull N,M;
  ull A;
  bool fin;

  for (int _n=0; _n<_N; _n++)
    {
      cout << "Case #" << _n+1 << ": ";

      cin >> N >> M >> A;

      fin=false;
      for (ull X=1; X<=N && !fin; X++)
	{
	  for (ull Y=divceil(A,X); Y<=M && !fin; Y++)
	    {
	      ull z=X*Y-A;
	      if (z==0)
		{
		  ull x=0;
		  ull y=0;
		  cout << "0 0 " << X << " " << y << " " << x << " " << Y;
		  fin=true;
		}
	      for (ull x=1; x<=z && x<=X && !fin; x++)
		{
		  if (z%x==0)
		    {
		      ull y=z/x;
		      if (y<=Y)
			{
			  cout << "0 0 " << X << " " << y << " " << x << " " << Y;
			  fin=true;
			}
		    }
		}
	    }
	}

      if (!fin)
	cout << "IMPOSSIBLE";

      cout << endl;
    }

  return 0;
}
