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

int T[40];

int main()
{
  int _N;
  cin >> _N;

  int N;

  string l;

  for (int _n=0; _n<_N; _n++)
    {
      cout << "Case #" << _n+1 << ": ";

      cin >> N;
      //  cout << "n: " << N << endl;
      for (int i=0; i<N; i++)
	{
	  cin >> l;
	  T[i]=0;
	  for (int j=0; j<N; j++)
	    if (l[j]=='1')
	      T[i]=max(T[i],j);

	  //	  cout << T[i] << endl;
	}
      //    cout << "---" << endl;


      int ret=0;
      for (int i=0; i<N; i++)
	{
	  for (int j=i; j<N; j++)
	    {
	      if (T[j]<=i)
		{
		  int tmp=T[j];
		  for (int k=j; k>i; k--)
		    T[k]=T[k-1];
		  T[i]=tmp;
		  ret+=j-i;
		  //		  cout << "swapped " << j-i << endl;
		  break;
		}
	    }
	  /*
	  FOR(i,N)
	    cout << T[i] << endl;
	  cout << "...." << endl;
	  */
	}

      cout << ret;
 
      cout << endl;
    }

  return 0;
}
