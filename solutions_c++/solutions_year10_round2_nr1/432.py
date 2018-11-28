#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int T,N,M;

char bestaat[5000][102];
char maak[100][102];

int compare(const void* a, const void* b)
{
	char* x = (char*) a;
	char* y = (char*) b;
	return strcmp(x,y);
}

void strip(char* str)
{
	int laatste = strlen(str) - 1;
	while (isspace(str[laatste]))
	{
		str[laatste] = '\0';
		laatste--;
	}
}

int find(char* str)
{
	for (int i = 0; i < N; i++)
	{
		if (!strcmp(str, bestaat[i]))
			return i + 1;
	}
	return 0;
}

int aantal(int j)
{
	char * begin = strtok(maak[j], "/");
	char substrings[100][102];
	int n = 0;
	while (begin != NULL)
	{
		strcpy(substrings[n], begin);
		n++;
		begin = strtok(NULL, "/");
	}
	n++;
	char temp[150];
	strcpy(temp, "/");
	strcat(temp, substrings[0]);
	int m = n;
	for (int i = 1; i < n; i++)
	{
		if (find(temp) == 0 && m == n)
		{
			m = i;
		}
		if (m != n)
		{
			strcpy(bestaat[N], temp);
			N++;
		}
		strcat(temp, "/");
		strcat(temp, substrings[i]);
	}
	return n - m;
}

void solve(int num)
{
	int totaal = 0;
	//qsort(bestaat, N, 102 * sizeof(char), compare); //niet noodzakelijk
	qsort(maak, M, 102 * sizeof(char), compare);
	
	for (int j = 0; j < M; j++)
	{
		totaal += aantal(j);
	}
	
	printf("Case #%d: %d\n", num, totaal);
	/*for (int j = 0; j < N; j++)
		printf("bestaat[%d]: %s\n", j, bestaat[j]);
	for (int j = 0; j < M; j++)
		printf("maak[%d]: %s\n", j, maak[j]);*/
}

int main()
{
	scanf("%d", &T);
	for (int i = 0; i < T; i++)
	{
		scanf("%d %d\n", &N, &M);
		for (int j = 0; j < N; j++)
		{
			char temp[105];
			fgets(temp, 102, stdin);
			strip(temp);
			strcpy(bestaat[j], temp);
		}
		for (int j = 0; j < M; j++)
		{
			char temp[105];
			fgets(temp, 102, stdin);
			strip(temp);
			if (find(temp) == 0)
				strcpy(maak[j], temp);
			else
			{
				j--;
				M--;
			}
		}
		solve(i + 1);
	}
	return 0;
}

