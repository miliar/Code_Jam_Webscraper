#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#define MAXN 15

using namespace std;

struct coord
{
	int x, y;
};

static struct coord res[MAXN];
static int a[MAXN];
static int perm[MAXN];
int N, W, H;

char CanSolve (int point, char first, int now, int last, int max)
{
	if (point == N) return 1;
	if (now > H) return 0;
	if ((last + a[perm[point]]) <= W)
	{
		if (first)
		{
			res[perm[point]].x = last + a[perm[point]];
			res[perm[point]].y = 0;
			int max2 = max;
			if ((a[perm[point]]) > max2) max2 = a[perm[point]];
			return CanSolve(point+1, 1, now, last + 2 * a[perm[point]], max2);
		}
		else
		{
			res[perm[point]].x = last + a[perm[point]];
			res[perm[point]].y = now + a[perm[point]];
			if (res[perm[point]].y > H) return 0;
			int max2 = max;
			if ((2 * a[perm[point]]) > max2) max2 = 2 * a[perm[point]];
			return CanSolve(point+1, 0, now, last + 2 * a[perm[point]], max2);
		}
	}
	else
	{
		return CanSolve(point, 0, now + max, -a[perm[point]], 0);
	}
}

int main ()
{
	int T, iT;
	scanf("%d",&T);
	for (iT = 0; iT < T; iT++)
	{
		scanf("%d %d %d",&N,&W,&H);
		int i;
		for (i = 0; i < N; i++)
		{
			scanf("%d",&(a[i]));
			perm[i] = i;
		}
		char flag = 0;
		do
		{
			if (CanSolve(0,1,0,-a[perm[0]],0))
			{
				flag = 1;
				break;
			}
		} while (next_permutation (perm, perm+N));
		if (!flag) printf("OOPS!\n");
		printf("Case #%d:",iT+1);
		for (i = 0; i < N; i++) printf(" %d %d",res[i].x,res[i].y);
		printf("\n");
	}
	return 0;	
}
