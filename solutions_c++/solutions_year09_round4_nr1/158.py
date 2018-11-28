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

vector <string>	mat;
vector <string>	temp;

int main()
{
	int	T,cs;
	char	s[1000];
	int	i,j,k;
	int	N;
	int	t;

	scanf("%d",&T);

	rab(cs,1,T)
	{
		scanf("%d",&N);

		mat.clear();
		t = 0;

		Fi(N)
		{
			scanf("%s",s);
			mat.push_back(s);
		}

		Fi(N)
		{
			for(j = i + 1; j < N; j++) if(mat[i][j] == '1') break;
			if(j >= N) continue;

			for(j = i + 1; j < N; j++)
			{
				for(k = i + 1; k < N; k++)
				{
					if(mat[j][k] == '1') break;
				}
				if(k >= N) break;
			}
			string	temp = mat[j];

			for(k = j - 1; k >= i; k--)
			{	mat[k+1] = mat[k];
				t++;
			}
			mat[i] = temp;
		}
		printf("Case #%d: %d\n",cs,t);
	}
	return 0;
}
