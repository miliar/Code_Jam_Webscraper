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

int M[2048][11];
int C[2048];
//int C[1024][1024];

int main()
{
  int _N;
  cin >> _N;

  int P;

  for (int _n=0; _n<_N; _n++)
    {
      cout << "Case #" << _n+1 << ": ";

      memset(M,-1,2048*11*sizeof(int));

      cin >> P;
      for (int i=0; i<(1<<P); i++)
	{
	  int x;
	  cin >> x;
	  x=P-x;
	  M[(1<<P)-1+i][x]=0;
	  //	  	  cout << M[(1<<P)-1+i] << " ";
	}
      //      cout << endl;

      for (int i=P-1; i>=0; i--)
	{
	  for (int j=(1<<i)-1; j<(1<<i)-1+(1<<i); j++)
	    {
	      cin >> C[j];
	    }
	}

      for (int i=P-1; i>=0; i--)
	{
	  for (int j=(1<<i)-1; j<(1<<i)-1+(1<<i); j++)
	    {
	      for (int k=0; k<11; k++)
		{
		  for (int l=0; l<11; l++)
		    {
		      if (M[2*j+1][k]!=-1 && M[2*j+2][l]!=-1)
			{
			  //	  printf("%d %d %d %d %d %d\n",i,j,k,l,M[2*j+1][k],M[2*j+2][l]);

			  if (M[j][max(k,l)]==-1)
			    M[j][max(k,l)]=M[2*j+1][k]+M[2*j+2][l];
			  else
			    M[j][max(k,l)]=min(M[j][max(k,l)],M[2*j+1][k]+M[2*j+2][l]);

			  if (max(k,l)-1>=0)
			    {
			      if (M[j][max(k,l)-1]==-1)
				{
				  M[j][max(k,l)-1]=M[2*j+1][k]+M[2*j+2][l]+C[j];
				  //	  cout << "ok" << endl;
				}
			      else
				M[j][max(k,l)-1]=min(M[j][max(k,l)-1],M[2*j+1][k]+M[2*j+2][l]+C[j]);

			    }
			}
		    }
		}
	    }
	}

      cout << M[0][0];// << endl;
      //      cout << M[0] << endl;

//       for (int i=P-1; i>=0; i--)
// 	{
// 	  for (int j=0; j<(1<<i); j++)
// 	    cin >> C[P-1-i][j];
// 	}



      cout << endl;
    }

  return 0;
}
