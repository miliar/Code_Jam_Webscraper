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

int ind(int a)
{
  if (a>='0' && a<='9')
    return a-'0';
  else
    return a-'a'+10;
}

int main()
{
  int _N;
  cin >> _N;

  string s;

  int val[10+26];
  int base;

  for (int _n=0; _n<_N; _n++)
    {
      cout << "Case #" << _n+1 << ": ";

      cin >> s;
      base=0;
      for (int i=0; i<36; i++)
	val[i]=-2;
      for (int i=0; i<s.size(); i++)
	{
	  if (val[ind(s[i])]==-2)
	    {
	      val[ind(s[i])]=-1;
	      base++;
	    }
	}
      if (base==1)
	base=2;

      val[ind(s[0])]=1;

      ull mult=1;
      ull ret;
      for (int i=1; i<s.size(); i++)
	mult*=(ull)base;

      ret=mult;
      int cval=0;
      for (int i=1; i<s.size(); i++)
	{
	  mult/=base;
	  if (val[ind(s[i])]==-1)
	    {
	      val[ind(s[i])]=cval;
	      cval++;
	      if (cval==1)
		cval++;
	    }

	  ret+=mult*val[ind(s[i])];
	}

      cout << ret;
      cout << endl;
    }

  return 0;
}
