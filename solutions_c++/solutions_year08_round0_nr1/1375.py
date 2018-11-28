#include <stdio.h>
#include <string.h>


int main(void)
{
	int N, S, Q;
	int a, b, c, d;
	char name[100][110];
	char query[110];
	int queries[1000];
	int table[100][1001];
	int value;

	scanf("%d", &N);
	
	for(a=1; a<=N; a++)
	{
		scanf("%d\n", &S);
		for(b=0; b<S; b++)
		{
			fgets(name[b], sizeof(name[b]), stdin);
		}
		scanf("%d\n", &Q);
		queries[0] = -1;
		for(c=1; c<=Q; c++)
		{
			fgets(query, 110, stdin);
			for(b=0; b<S; b++)
			{
				if( strcmp(name[b], query)==0 )
				{
					queries[c] = b;
					break;
				}
			}
		}
/*		
		for(b=0; b<S; b++)
		{
			printf("%d %s\n", b, name[b]);
		}
		for(c=0; c<Q; c++)
		{
			printf("%d ", queries[c]);
		}
		printf("\n\n");
*/
		for(b=0; b<S; b++)
			table[b][0] = 0;

		for(c=1; c<=Q; c++)
		{
			for(b=0; b<S; b++)
			{
				if(queries[c] == b)
				{
					table[b][c] = 3000;
				}
				else
				{
					value = table[b][c-1];
					for(d=0; d<S; d++)
					{
						if(value > table[d][c-1]+1)
							value = table[d][c-1]+1;
					}
					table[b][c] = value;
				}
			}
		}
/*
		for(b=0; b<S; b++)
		{
			for(c=1; c<=Q; c++)
			{
				printf("%4d ", table[b][c]);
			}
			printf("\n");
		}
*/
		value = 3000;
		for(b=0; b<S; b++)
		{
			if(value > table[b][Q] )
				value = table[b][Q];
		}
		printf("Case #%d: %d\n", a, value);
	}
}

