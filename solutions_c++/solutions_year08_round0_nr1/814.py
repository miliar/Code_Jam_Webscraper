#include <stdio.h>
#include <string.h>
#include <math.h>

char search[101][132];
char query[1001][132];
int qr[1001];

void trim (char *str)
{
	int i;
	for (i = 0; i < strlen(str); i++)
		if (str[i] == 10)
		{
			str[i] = 0;
			break;
		}
}

void convertQuerry(int N, int Q)
{
	int i, j;
	for (i = 0; i < Q; i++)
		for (j = 0; j < N; j++)
			if (!strcmp(query[i], search[j]))
			{
				qr[i] = j;
				break;
			}
}

int analRun(int N, int Q)
{
	int i;
	int mas[100];
	int mx, curPos, last;
	int total = 0;

	last = -1;
	curPos = 0;
	while (1)
	{
		for (i = 0; i < N; i++)
			mas[i] = -1;
		for (i = curPos; i < Q; i++)
		{
			if (qr[i] == last)
			{
				mas[qr[i]] = -2;
				continue;
			}

			if (mas[qr[i]] == -1)
				mas[qr[i]] = i;
		}
		
		mx = 0;
		for (i = 0; i < N; i++)
		{
			if (mas[i] == -1)
				break;
			if (mas[i] > mx)
			{
				mx = mas[i];
				last = i;
			}
		}

		if (i != N)
			break;
		
		curPos = mx;
		total++;
	}
	return total;
}

int main ()
{
	int Q, N, res, i, j, t, len;
	FILE *in, *out;
	
	in = fopen("input.txt", "rt");
	out = fopen("output.txt", "wt");

	fscanf(in, "%d", &t);
	for (i = 0; i < t; i++)
	{
		fscanf(in, "%d\n", &N);
		for (j = 0; j < N; j++)
		{
			fgets(search[j], 1024, in);
			trim(search[j]);
		}
		fscanf(in, "%d\n", &Q);
		len = 0;
		for (j = 0; j < Q; j++)
		{
			fgets(query[len], 1024, in);
			trim(query[len]);
			if (len == 0)
				len++;
			else if (strcmp(query[len], query[len-1]))
				len++;
		}
		convertQuerry(N, len);
		res = analRun(N, len);
		fprintf(out, "Case #%d: %d\n", i+1, res);
	}

	fclose(in);
	fclose(out);

	return 0;
}

