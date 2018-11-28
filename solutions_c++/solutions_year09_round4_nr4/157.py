#include <iostream>
#include <cassert>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <set>
#include <map>
#include <functional>
#include <queue>
#include <bitset>
#include <sstream>
#include <vector>
using namespace std;

#define	sz(v)	(int)v.size()
#define	rep(i,n)	for((i)=0;(i) < (n); (i)++)
#define	rab(i,a,b)	for((i)=(a);(i) <= (b); (i)++)
#define	Fi(N)		rep(i,N)
#define	Fj(N)		rep(j,N)
#define	Fk(N)		rep(k,N)

int main()
{
	int	T,cs;
	int	N;
	int	X[3],Y[3],R[3];
	int	i,j,k;
	double	s,t1,t2;

	scanf("%d",&T);

	rab(cs,1,T)
	{
		scanf("%d",&N);

		Fi(N) scanf("%d %d %d",&X[i],&Y[i],&R[i]);

		if(N < 3)
		{
			s = 0;

			Fi(N) if(R[i] > s) s = R[i];
		}
		else
		{
			s = 1e+20;

			for(i = 0; i < N; i++)
			{
				for(j = i+1; j < N; j++)
				{
					t1 = hypot(X[i] - X[j],Y[i] - Y[j]) + R[i] + R[j];
					t1 /= 2;

					for(k = 0; k < N; k++)
					{
						if(i != k && j != k)
							break;
					}
					t2 = R[k];

					t1 = max(t1,t2);

					s = min(s,t1);
				}
			}
		}

		printf("Case #%d: %.10lf\n",cs,s);
	}
	return 0;
}
