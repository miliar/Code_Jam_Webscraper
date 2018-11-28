#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <cstring>
using namespace std;
int main()
{
	FILE *in = fopen("A-large.in", "r");
	FILE *out = fopen("out.txt", "w");
	char bd[55][55], ch;
	int ts, tc, i, j, k, tp;
	int K, N, resr, resb;
	fscanf(in, "%d", &ts); fgetc(in);
	for (tc = 1; tc <= ts; ++tc)
	{
		resr = resb = 0;
		fscanf(in, "%d %d", &N, &K);
		for (i = 1; i <= N; ++i)
		{
			fgetc(in);
			fgets(bd[i], N + 1, in);
		}
		for (j = N - 2; j >= 0; --j)
		{
			for (i = 1; i <= N; ++i)
			{
				if (bd[i][j + 1] == '.')
				{
					for (k = 1; j + k <= N && bd[i][j + k] == '.'; ++k)
					{
						ch = bd[i][j + k];
						bd[i][j + k] = bd[i][j + k - 1];
						bd[i][j + k - 1] = ch;
					}
				}
			}
		}
		for (i = 1; i <= N; ++i)
		{
			for (j = 0; j < N; ++j)
			{
				if (bd[i][j] != '.')
				{
					for (k = j, ch = bd[i][j], tp = 0; k < N && ch == bd[i][k]; ++k, ++tp)
						;
					if (ch == 'R' && tp > resr) resr = tp;
					if (ch == 'B' && tp > resb) resb = tp;

					for (k = i, ch = bd[i][j], tp = 0; k <= N && ch == bd[k][j]; ++k, ++tp)
						;
					if (ch == 'R' && tp > resr) resr = tp;
					if (ch == 'B' && tp > resb) resb = tp;

					for (ch = bd[i][j], tp = 0; i - tp >= 1 && j + tp < N && ch == bd[i - tp][j + tp]; ++tp)
						;
					if (ch == 'R' && tp > resr) resr = tp;
					if (ch == 'B' && tp > resb) resb = tp;
					
					for (ch = bd[i][j], tp = 0; i + tp <= N && j + tp < N && ch == bd[i + tp][j + tp]; ++tp)
						;
					if (ch == 'R' && tp > resr) resr = tp;
					if (ch == 'B' && tp > resb) resb = tp;
				}
			}
		}
		for (j = 0; j < N; ++j)
		{
			for (i = 1; i <= N; ++i)
			{
				
			}
		}
		if (resr >= K && resb >= K)
		{
			fprintf(out, "Case #%d: Both\n", tc);
			continue;
		}
		if (resr >= K)
		{
			fprintf(out, "Case #%d: Red\n", tc);
			continue;
		}
		if (resb >= K)
		{
			fprintf(out, "Case #%d: Blue\n", tc);
			continue;
		}
		fprintf(out, "Case #%d: Neither\n", tc);
	}
	return 0;
}
