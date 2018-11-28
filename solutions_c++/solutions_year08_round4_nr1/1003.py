#include <cstdio>
#include <cstdlib>
#include <iostream>

using namespace std;
#define NODENUM 50

int node[NODENUM];
int nodechange[NODENUM];
int computenode[NODENUM];
int loop[NODENUM];
int m, v;
int minchange = NODENUM;

int main()
{
	int numCase;
	int ci, tx, ty;

	freopen("A-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	scanf("%d", &numCase);
	for(int cases = 0; cases < numCase; cases++)
	{
		scanf("%d%d", &m, &v);
		for(ci = 1; ci <= m / 2; ci++)
		{
			scanf("%d%d", &tx, &ty);
			node[ci] = tx;
			nodechange[ci] = ty;
		}
		for(ci = m / 2 + 1; ci <= m; ci++)
		{
			scanf("%d", &tx);
			node[ci] = tx;
			computenode[ci] = tx;
		}
		
		for(ci = 1; ci <= m / 2; ci++)
		{
			if(nodechange[ci] == 1)
				loop[ci] = 0;
			else
				loop[ci] = node[ci];
		}
		minchange = NODENUM;
		while(1)
		{
			for(ci = m / 2; ci >= 1; ci--)
			{
				if(loop[ci] == 1)
					computenode[ci] = computenode[ci * 2] & computenode[ci * 2 + 1];
				else
					computenode[ci] = computenode[ci * 2] | computenode[ci * 2 + 1];
			}
			if(computenode[1] == v)
			{
				tx = 0;
				for(ci = 1; ci <= m / 2; ci++)
				{
					if(loop[ci] != node[ci])
						tx++;
				}
				if(tx < minchange)
					minchange = tx;
			}

			for(ci = m / 2; ci >= 1; ci--)
			{
				if(nodechange[ci] == 1)
				{
					loop[ci]++;
					if(loop[ci] < 2)
						break;
					loop[ci] = 0;
				}
			}
			if(ci < 1)
				break;
		}
		
		if(minchange < 50)
			cout << "Case #" << cases + 1 << ": " << minchange << endl;
		else
			cout << "Case #" << cases + 1 << ": IMPOSSIBLE" << endl;
	}

	return 0;
}