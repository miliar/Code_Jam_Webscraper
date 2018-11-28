#include <stdio.h>
#include <string.h>

#define NMAX 600
#define MASK1 0x8
#define MASK2 0x4
#define MASK3 0x2
#define MASK4 0x1


int t, test, n, m, a[NMAX][NMAX], b[NMAX][NMAX], v[NMAX];

int min(int a, int b, int c)
{
	if (a < b)
	{
		if (a < c) return a;
		return c;
	}
	if (b < c) return b;
	return c;
}

int extrage()
{
	int max = 0, x, y, i, j;
	for (i = 0; i < m; i++)
		if (a[i][0] != -1) b[i][0] = 1;
		else b[i][0] = 0;
	for (i = 0; i < n; i++) 
		if (a[0][i] != -1) b[0][i] = 1;
		else b[0][i] = 0;
	for (i = 1; i < m; i++)
		for (j = 1; j < n; j++)
		{
			if (a[i][j] == -1) 
			{
				b[i][j] = 0;
				continue;
			}
			x = min(b[i-1][j-1], b[i-1][j], b[i][j-1]);
			if (x == 0) 
			{
				b[i][j] = 1;
				continue;
			}
			if (x == 1 && a[i-1][j-1] == a[i][j] && a[i][j] != a[i-1][j] && a[i][j] != a[i][j-1])
			{
				b[i][j] = 2;
				continue;
			}
			if (x > 1 && a[i-1][j-1] == a[i][j])
			{
				b[i][j] = x + 1;
				continue;
			}
			b[i][j] = 1;
		}
	for (i = 0; i < m; i++)
		for (j = 0; j < n; j++)
			if (b[i][j] > max) 
			{
				max = b[i][j];
				x = i;
				y = j;
			}
	for (i = 0; i < max; i++)
		for (j = 0; j < max; j++)
			a[x-i][y-j] = -1;
	return max;
}


int main()
{
	FILE *fin, *fout;
	fin = fopen("date.in", "rt");
	fout = fopen("date.out", "wt");
	fscanf(fin, "%d", &t);
	for (test = 1; test <= t; test++)
	{
		fscanf (fin, "%d %d\n", &m, &n);
		int i, j, x, max, nr, total = 0, k = 0;
		char s[NMAX];
		for (i = 0; i < m; i++)
		{
			fgets(s, NMAX, fin);
			for (j = 0; j < n/4; j++)	
			{
				if (s[j] >= '0' && s[j] <='9') x = s[j] - '0';
				else x = s[j] - 'A' + 10;
				if ((x & MASK1) == 0) a[i][4*j] = 0;
				else a[i][4*j] = 1;
				if ((x & MASK2) == 0) a[i][4*j+1] = 0;
				else a[i][4*j+1] = 1;
				if ((x & MASK3) == 0) a[i][4*j+2] = 0;
				else a[i][4*j+2] = 1;
				if ((x & MASK4) == 0) a[i][4*j+3] = 0;
				else a[i][4*j+3] = 1;
			}
		}
		memset(v, 0, sizeof(v));
		do
		{
			x = extrage();
			if (v[x] == 0 && x != 0)
			{
				total++;
				k = x;
			}
			v[x]++;
		}while(x > 1);
		if (x == 1)
			for (i = 0; i < m; i++)
				for (j = 0; j < n; j++)
					if (a[i][j] != -1) v[1]++;
		fprintf(fout, "Case #%d: %d\n", test, total);
		for (i = min(n, m, m); i > 0; i--)
			if (v[i] != 0) fprintf(fout, "%d %d\n", i, v[i]);
	}
		
fclose(fin);
fclose(fout);
return 0;
}
