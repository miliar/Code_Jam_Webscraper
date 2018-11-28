#include <iostream>
#include <cstdio>
#include <string>

#define MAX_L 15
#define MAX_D 5000
#define MAX_N 500

char WORD[MAX_D][MAX_L+1];
char PATTERN[28 * MAX_L + 1];

bool exam(int index)
{
	int i;
	int token = 0;

	for(i=0;i<strlen(PATTERN);i++)
	{
		if( PATTERN[i]=='(' )
		{
			bool isFound = false;
			while( PATTERN[++i]!=')' )
			{
				if( PATTERN[i]==WORD[index][token] )
				{
					isFound = true;
					break;
				}
			}
			if( !isFound )
				return false;
			while( PATTERN[i]!=')' )
				i++;
		}
		else
		{
			if( WORD[index][token]!=PATTERN[i] )
				return false;
		}
		token++;
	}
	return true;
}

int main()
{
	int i, j, k;
	int L, D, N;
	int count;

	scanf("%d %d %d", &L, &D, &N);

	for(i=0;i<D;i++)
	{
		scanf("%s", WORD[i]);
	}

	for(i=0;i<N;i++)
	{
		scanf("%s", PATTERN);

		count = 0;

		for(j=0;j<D;j++)
		{
			if( exam(j) )
			{
				count++;
			}
		}

		printf("Case #%d: %d\n", i+1, count);
	}
	return 0;
}

