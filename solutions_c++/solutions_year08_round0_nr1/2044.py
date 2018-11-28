#include <stdio.h>
#include <string.h>
const int MAXS = 100;
const int MAXQ = 1000;
const int INFINITY = 10000000;
char name[MAXS][105];
char query[MAXQ][105];
int table[MAXQ][MAXS];
char str[500];
int S, Q;
int main()
{
	int t;
	gets(str);
	sscanf(str, "%d", &t);
	for (int cases = 1; cases <= t; cases++) {
		gets(str);
		sscanf(str, "%d", &S);
		for (int i = 0; i < S; i++) gets(name[i]);
		gets(str);
		sscanf(str, "%d", &Q);
		for (int i = 0; i < Q; i++) gets(query[i]);
		for (int i = 0; i < S; i++)
			if (strcmp(query[0], name[i]) == 0) table[0][i] = INFINITY;
			else table[0][i] = 0;
		for (int i = 1; i < Q; i++)
			for (int j = 0; j < S; j++) {
				if (strcmp(query[i], name[j]) == 0) table[i][j] = INFINITY;
				else {
					int temp = table[i - 1][j];
					for (int k = 0; k < S; k++)
						if (k != j && table[i - 1][k] + 1 < temp)
							temp = table[i - 1][k] + 1;
					table[i][j] = temp;
				}
			}
		int min = INFINITY;
		for (int i = 0; i < S; i++)
			if (table[Q - 1][i] < min) min = table[Q - 1][i];
		printf("Case #%d: %d\n", cases, min);
	}
}