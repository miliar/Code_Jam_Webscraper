#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int S, N, Q;
char engine[100][101];	// engine name array
char* engptr[100];	// pointer to engine name
int query[1000];	// queries as index array
int status[2][100][100];	// ...
#define INFINITY2 1001

int compName(const void* a, const void* b)
{
	return strcmp(*(const char**)a, *(const char**)b);
}

void readData()
{
	int i;
	char buffer[100], *line = buffer;

	scanf("%d\n", &S);
	for (i=0; i<S; ++i)
	{
		gets(engine[i]);
		engptr[i] = engine[i];
	}
	qsort(engptr, S, sizeof(char*), compName);
	scanf("%d\n", &Q);
	for (i=0; i<Q; ++i)
	{
		gets(line);
		char** pos = (char**)bsearch(&line, engptr, S, sizeof(char*), compName);
		if (pos==NULL)
			query[i] = -1;
		else
			query[i] = pos - engptr;
	}
}

int minIntArray(int* array, int n)
{
	int r = INFINITY2, i;
	for (i=0; i<n; ++i) if (r>array[i]) r=array[i];
	return r;
}

int solve()
{
	if (Q==0) return 0;
	int i, j, k, r;
	
	for (j=0; j<S; ++j)
		for (k=0; k<S; ++k)
		{
			int sw = j==k ? 0 : 1;
			if (k==query[Q-1]) status[(Q-1)%2][j][k] = INFINITY2;
			else status[(Q-1)%2][j][k] = sw;
		}

	for (i=Q-2; i>=0; --i)
		for (j=0; j<S; ++j)
			for (k=0; k<S; ++k)
			{
				int sw = j==k ? 0 : 1;
				if (k==query[i])
					status[i%2][j][k] = INFINITY2;
				else
					status[i%2][j][k] = sw + minIntArray(status[(i+1)%2][k], S);
			}

	r = INFINITY2;
	for (j=0; j<S; ++j)
	{
		int tempR = minIntArray(status[0][j], S);
		if (r>tempR) r=tempR;
	}

	return r;
}

int main()
{
	int i;
	scanf("%d", &N);
	for (i=1; i<=N; ++i)
	{
		readData();
		printf("Case #%d: %d\n", i, solve());
	}
	return 0;
}
