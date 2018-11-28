#include <stdio.h>

#define MAX 1000000
int interval[MAX];
int prime[MAX] = {0};

int root(int s)
{
	if(interval[s]==s)
		return s;
	return root(interval[s]);
}

int Union(int s1, int s2)
{
	int r1 = root(s1);
	int r2 = root(s2);
//printf("(%d) %d (%d) %d\n", r1, s1, r2, s2);
	if( r1 == r2 )
		return 0;
	interval[r2] = r1;
	return 1;
}

int main(void)
{
	int C;
	int i, j, k, x;
	int A, B, P, nSets;
	int diff, root;

	int a, b;
	for(a = 2; a < MAX; a++)
	{
		if(!prime[a])
		{
			for(b=2; a*b<MAX; b++)
			{
				prime[a*b] = 1;	
			}
//			printf("%d ", a);
		}
	}
	scanf("%d", &C);
	
	for(i=1; i<=C; i++)
	{
		scanf("%d%d%d", &A, &B, &P);
		diff = B-A;
		for(j=0; j<=diff; j++)
		{
			interval[j] = j;
		}
		nSets = B-A+1;
		for(j=P; j<=B;j++)
		{
			if(!prime[j])
			{
				k = A/j;
				k = j*k;
				if(k<A)
					k+=j;
				root = k;
				k+=j;
				while( k<=B ) 
				{
//					printf("%d %d\n", root, k);
	
					if( Union(root-A, k-A) == 1)
					{
//						printf("Diff set\n");
						nSets--;
					}
					k+=j;
				}
			}
		}
		printf("Case #%d: %d\n", i, nSets);
	}
}

