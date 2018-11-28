#include <stdio.h>
#include <stdlib.h>
#include <algorithm>

using namespace std;

int main()
{
	int num_test, t;
	
	scanf("%d\n", &num_test);
	for (t = 1; t <= num_test; t++)
	{
		int qlist[110];
		int i, j, k, l;
		int p, q;
		
		scanf("%d %d\n", &p, &q);
		for (i = 0; i < q; i++)
		{
			scanf("%d ", &qlist[i]);
		}
		
		int min_cost = 99999999;
		do
		{
			int cost = 0;		
			
			for (i = 0; i < q; i++)
			{
				int start = 1, end = p;
				for (j = 0; j < i; j++)
				{
					if (qlist[j] < qlist[i])
					{
						if (start < qlist[j]) start = qlist[j] + 1;
					}
					else
					{
						if (end > qlist[j]) end = qlist[j] - 1;
					}
				}
				//printf(" -> %d % d <- \n", start, end);
				cost += (end - start);
			}	
			/*
			for (i = 0; i < q; i++)
				printf("%d ", qlist[i]);
			printf("-> %d \n", cost);
			
			*/

			if (cost < min_cost) min_cost = cost;
		}
		while (next_permutation(qlist, qlist + q));
		
		printf("Case #%d: %d\n", t, min_cost);
		
	}
	return 0;
}

