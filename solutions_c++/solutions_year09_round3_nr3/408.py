#include <stdio.h>
#include <string.h>

#include <algorithm>
#include <set>
using namespace std;

#define		DEBUG	0

int		CAS = 0, T;
int		P, Q;

int		per[100];

int		cost;
bool	vit[110];
int		order[100];


int		pay()
{
	int		i, j, k;
	bool	bd[100];
	int		rnt = 0;
	
	memset(bd, false, sizeof(bd));

	for (k=0; k<Q; k++)
	{
		bd[order[k]] = true;
		
		for (i=order[k]-1; i>=0; i--)
		{
			if (bd[i] == true)	break;
			rnt++;
		}
		for (i=order[k]+1; i<P; i++)
		{
			if (bd[i] == true)	break;
			rnt++;
		}
	}
	return rnt;
}

void	DFS(int dep)
{
	if (dep >= Q)
	{
		int		cur = pay();
		if (cur <= cost)
			cost = cur;
		return ;
	}
	
	int		i;
	for (i=0; i<Q; i++)
	{
		if (vit[i] == true)
		{
			vit[i] = false;
			order[dep] = per[i];
			DFS(dep+1);
			vit[i] = true;
		}
	}
}

int main()
{
	int		i, j, k;

	if (!DEBUG)
	{
		freopen("D:/round1/3.in", "r", stdin);
		freopen("D:/round1/3.out", "w", stdout);
	}

	scanf("%d", &T);	
	while (T--)
	{
		scanf("%d %d", &P, &Q);
		for (i=0; i<Q; i++)
		{
			scanf("%d", &per[i]);
			per[i]--;
		}
		memset(vit, true, sizeof(vit));
		cost  = 1 << 30;
		
		DFS(0);
		
		printf("Case #%d: %d\n", ++CAS, cost);

	}

	return 0;
}