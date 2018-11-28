#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <map>
#include <cmath>
#include <cstdlib>
#include <cstdio>

using namespace std;

#define FORI(_i, _j, _size) for (size_t _i = _j; _i < _size; ++_i)
#define FORI1(_i, _j, _size, _inc) for (size_t _i = _j; _i < _size; _i += _inc)
#define FORVI(_i, _j, _v) FORI(_i, _j, _v.size())
#define FORVI1(_i, _j, _v, _inc) FORI1(_i, _j, _v.size(), _inc)
#define FOR(_i, _size) FORI(_i, 0, _size)
#define FOR1(_i, _size, _inc) FORI1(_i, 0, _size, _inc)
#define FORV(_i, _v) FOR(_i, _v.size())
#define FORV1(_i, _v, _inc) FOR1(_i, _v.size(), _inc)
#define MEMZ(_array) memset(_array, 0, sizeof(_array))
#define OUT(_i, _n) cout << "Case #" << _i << ": " << _n << endl 

int main()
{

  int T;
  cin >> T;

  FOR(i, T)
  {
    int R, C;
    cin >> R >> C;

    int a[R][C];
    MEMZ(a);

    FOR(j, R)
    {
      string s;
      cin >> s;

      FOR(k, C)
      {
	if (s.at(k) != '.')
	{
	  a[j][k] = 1;
	}
      }
    }

    bool fail = false;
    FOR(j, R)
    {
      FOR(k, C)
      {
	if (a[j][k] == 1)
	{
	  if (k == C - 1 || (a[j][k + 1] == 0))
	  {
	    fail = true;
	    break;
	  }
	  if (j == R - 1 || (a[j + 1][k] == 0) || (a[j + 1][k + 1] == 0))
	  {
	    fail = true;
	    break;
	  }

	  a[j][k] = 2;
	  a[j][k + 1] = 3;
	  a[j + 1][k] = 4;
	  a[j + 1][k + 1] = 5;
	}
      }
      if (fail)
      {
	break;
      }
    }

    if (fail)
    {
      cout << "Case #" << (i + 1) << ":" <<  endl << "Impossible" << endl;
    }
    else
    {
      cout << "Case #" << (i + 1) << ":" << endl;

      FOR(j, R)
      {
	FOR(k, C)
	{
	  switch(a[j][k])
	  {
	  case 0:
	    cout << ".";
	    break;
	  case 2:
	    cout << "/";
	    break;
	  case 3:
	    cout << "\\";
	    break;
	  case 4:
	    cout << "\\";
	    break;
	  case 5:
	    cout << "/";
	    break;
	  }
	}
	cout << endl;
      }
    }
  }

  return 0;
}
