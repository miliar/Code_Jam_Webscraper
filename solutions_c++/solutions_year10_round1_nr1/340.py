#include <stdio.h>

int n, k;

#define MAX 64

char mat[MAX][MAX];
char m[MAX][MAX];

int acha(char c)
{
	int i, j, k2;

	for (i=0; i<n; i++)
	{
		k2 = 0;
		for (j=0; j<n; j++)
		{
			if (m[i][j] == c)
			{
				k2++;
				if (k2 == k)
				{
					return 1;
				}
			}
			else
				k2 = 0;
		}
	}

	for (i=0; i<n; i++)
	{
		k2 = 0;
		for (j=0; j<n; j++)
		{
			if (m[j][i] == c)
			{
				k2++;
				if (k2 == k)
				{
					return 1;
				}
			}
			else
				k2 = 0;
		}
	}

	
	for (i=1-n; i<n; i++)
	{
		k2 = 0;


		if (i<0)
		{
			j = -i;
		}
		else
			j = 0;
		for (; j<n&&(i+j)<n; j++)
		{
			if (m[j][j+i] == c)
			{
				k2++;
				if (k2 == k)
				{
					return 1;
				}
			}
			else
				k2 = 0;
		}
	}

	for (i=0; i<2*n; i++)
	{
		k2 = 0;


		if (i>=n)
		{
			j = i-(n-1);
		}
		else
			j = 0;
		for (; (i-j)>=0 && j<n; j++)
		{
			if (m[i-j][j] == c)
			{
				k2++;
				if (k2 == k)
				{
					return 1;
				}
			}
			else
				k2 = 0;
		}
	}

	return 0;
}

int vai()
{
	int i, j, k;
	int a = 0, b = 0;
	for (i=0; i<n; i++)
	{
		for (j=n-1, k=0; j>=0; j--)
		{
			if (mat[i][j]!='.')
			{
				m[n-i-1][k] = mat[i][j];
				k++;
			}
		}
		for (; k<n; k++)
		{
			m[n-i-1][k] = '.';
		}
	}

	a = acha('R');
	b = acha('B');

	if (a == 0)
	{
		if (b)
		{
			return -1;
		}
		return 0;
	}

	if (b)
	{
		return 2;
	}
	return 1;

}

int main()
{
	int t;
	int cas;
	scanf("%d", &t);

	for (cas=1; cas<=t; cas++)
	{
		printf("Case #%d: ",cas);

		scanf("%d %d", &n, &k);

		int i;

		for (i=0; i<n; i++)
		{
			scanf("%s", mat[i]);
		}

		switch(vai())
		{
			case -1:
				printf("Blue\n");
				break;
			case 0:
				printf("Neither\n");
				break;
			case 1:
				printf("Red\n");
				break;
			case 2:
				printf("Both\n");
				break;
		}
	}

	return 0;
}

