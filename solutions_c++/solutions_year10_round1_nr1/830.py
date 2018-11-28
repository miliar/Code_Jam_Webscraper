#include <stdio.h>

int b[100][100];
int r[100][100];

int main()
{
	int t;
	int cnt = 0;
	scanf("%d",&t);

	FILE *fout = fopen("a.out", "w");
		
	while(t--)
	{
		cnt++;
		int n, k;
		scanf("%d %d", &n, &k);
		
		for (int i=0; i<n; i++)
		{
			char str[100];

			scanf("%s", str);
			for (int j=0; j <n; j++) {
				if (str[j] == '.')
					b[i][j] = 0;
				if (str[j] == 'B')
					b[i][j] = 1;
				if (str[j] == 'R')
					b[i][j] = 2;
			}
		}

		for (int i=0; i<n; i++)
		{
			int k=n-1;
			for (int j=n-1; j>=0; j--)
			{
				if (b[n-1-i][j] != 0)
				{
					r[k][i] = b[n-1-i][j];
					k--;
				}
			}
			for (; k>=0; k--)
				r[k][i] = 0;
		}

		int w1 = 0;
		int w2 = 0;

		for (int i=0; i<n; i++)
		{
			int c = 0;
			for (int j=0; j<n; j++)
			{
				if (r[i][j] == 1) c++; else c = 0;
				if (c >= k) break;
			}
			if (c >= k) {
				w1 = 1;
				break;
			}
		}

		if (w1 == 0)
		{
			for (int i=0; i<n; i++)
			{
				int c = 0;
				for (int j=0; j<n; j++)
				{
					if (r[j][i] == 1) c++; else c = 0;
					if (c >= k) break;
				}
				if (c >= k) {
					w1 = 1;
					break;
				}
			}
		}

		if (w1 == 0)
		{
			int x=0;
			int y=n-1;

			for (int i=0; i<n*2-1; i++)
			{
				int c = 0;

				int x1 = x;
				int y1 = y;

				for (; ;)
				{
					if (r[y1][x1] == 1) c++; else c = 0;
					if (c >= k) break;

					y1++; x1++;
					if (y1 == n || x1 == n) break;
				}
				if (c >= k) {
					w1 = 1;
					break;
				}

				if (y > 0) y--; else x++;
			}
		}

		if (w1 == 0)
		{
			int x=n-1;
			int y=n-1;

			for (int i=0; i<n*2-1; i++)
			{
				int c = 0;

				int x1 = x;
				int y1 = y;

				for (; ;)
				{
					if (r[y1][x1] == 1) c++; else c = 0;
					if (c >= k) break;

					y1++; x1--;
					if (y1 == n || x1 < 0) break;
				}
				if (c >= k) {
					w1 = 1;
					break;
				}

				if (y > 0) y--; else x--;
			}
		}

		for (int i=0; i<n; i++)
		{
			int c = 0;
			for (int j=0; j<n; j++)
			{
				if (r[i][j] == 2) c++; else c = 0;
				if (c >= k) break;
			}
			if (c >= k) {
				w2 = 1;
				break;
			}
		}

		if (w2 == 0)
		{
			for (int i=0; i<n; i++)
			{
				int c = 0;
				for (int j=0; j<n; j++)
				{
					if (r[j][i] == 2) c++; else c = 0;
					if (c >= k) break;
				}
				if (c >= k) {
					w2 = 1;
					break;
				}
			}
		}

		if (w2 == 0)
		{
			int x=0;
			int y=n-1;

			for (int i=0; i<n*2-1; i++)
			{
				int c = 0;

				int x1 = x;
				int y1 = y;

				for (; ;)
				{
					if (r[y1][x1] == 2) c++; else c = 0;
					if (c >= k) break;

					y1++; x1++;
					if (y1 == n || x1 == n) break;
				}
				if (c >= k) {
					w2 = 1;
					break;
				}

				if (y > 0) y--; else x++;
			}
		}

		if (w2 == 0)
		{
			int x=n-1;
			int y=n-1;

			for (int i=0; i<n*2-1; i++)
			{
				int c = 0;

				int x1 = x;
				int y1 = y;

				for (; ;)
				{
					if (r[y1][x1] == 2) c++; else c = 0;
					if (c >= k) break;

					y1++; x1--;
					if (y1 == n || x1 < 0) break;
				}
				if (c >= k) {
					w2 = 1;
					break;
				}

				if (y > 0) y--; else x--;
			}
		}

		if (w1 == 1 && w2 == 1)
			fprintf(fout, "Case #%d: Both\n", cnt);
		else if (w1 == 1)
			fprintf(fout, "Case #%d: Blue\n", cnt);
		else if (w2 == 1)
			fprintf(fout, "Case #%d: Red\n", cnt);
		else 
			fprintf(fout, "Case #%d: Neither\n", cnt);

	}

	fclose(fout);
	return 0;
}