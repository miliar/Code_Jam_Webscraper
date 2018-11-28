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

bool	rock[1000][1000];
int	path[1000][1000];

int	dr[] = {2,1};
int	dc[] = {1,2};

int main()
{
	int	T,cs;
	int	H,W,R;
	int	i,j,k;

	scanf("%d",&T);

	rab(cs,1,T)
	{
		scanf("%d %d %d",&H,&W,&R);

		Fi(H) Fj(W) rock[i][j] = false;

		while(R--)
		{
			int	r,c;

			scanf("%d %d",&r,&c);

			rock[r-1][c-1] = true;
		}

		path[H - 1][W - 1] = 1;

		for(i = H - 1; i >= 0; i--)
		{
			for(j = W - 1; j >= 0; j--)
			{
				if(i == H - 1 && j == W - 1) continue;

				path[i][j] = 0;

				for(k = 0; k < 2; k++)
				{
					int	nr,nc;

					nr = i + dr[k];
					nc = j + dc[k];

					if(nr >= H || nc >= W) continue;
					if(rock[nr][nc]) continue;

					path[i][j] = (path[i][j] + path[nr][nc]) % 10007;
				}
			}
		}

/*		for(i = 0; i < H; i++)
		{
			for(j = 0; j < W; j++)
				printf("%d ",path[i][j]);
			printf("\n");
		}*/

	//	printf("%d %d\n",H,W);

		printf("Case #%d: %d\n",cs,path[0][0]);
	}
	return 0;
}
