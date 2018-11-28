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

#define MOD 100003

int *R,*B;

int b(int n, int k)
{
  //cout << n << ":" << k << endl;

  if (k==0 || k==n)
    return 1;

  if (k<0 || k>n)
    return 0;

  if (B[n*501+k]!=-1)
    return B[n*501+k];
  else
    {
      B[n*501+k]=(b(n-1,k)+b(n-1,k-1))%MOD;
      return B[n*501+k];
    }
}

int r(int n, int k)
{
  //cout << n << " . " << k << endl;

  if (k==1)
    return 1;
  if (k==n)
    return 0;

  if (R[n*501+k]!=-1)
    return R[n*501+k];
  else
    {
      R[n*501+k]=0;
      for (int l=1; l<k; l++)
	{
	  R[n*501+k]=(R[n*501+k]+r(k,l)*b(n-k-1,k-l-1))%MOD;

// 	  if (R[n*501+k]<0)
// 	    {
// 	      cout  << n << " * " << k << " : " << l  << endl;
// 	      cout << b(n-k-1,k-l-1) << " , " << r(k,l) << endl;
// 	    }
	}

      return R[n*501+k];
    }
}

int main()
{
  int _N;
  cin >> _N;

  int n;

  R=new int[501*501];
  B=new int[501*501];

  memset(R,-1,501*501*sizeof(int));
  memset(B,-1,501*501*sizeof(int));

  for (int _n=0; _n<_N; _n++)
    {
      cout << "Case #" << _n+1 << ": ";

      cin >> n;
      int ret=0;

      for (int k=1; k<n; k++)
	{
// 	  cout << r(n,k)%MOD << endl;
	  ret=(ret+r(n,k))%MOD;
	}

      cout << ret;

      cout << endl;
    }

  delete[] R;
  delete[] B;

  return 0;
}
