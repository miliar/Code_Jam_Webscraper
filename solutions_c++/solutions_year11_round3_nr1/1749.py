#include <cstdio>
#include <cstring>

FILE* f1, *f2;

const int MAX = 55;
char g[MAX][MAX], red[4] = {'/', '\\', '\\', '/'};
int n, m;

bool check(int i, int j)
{
	return i >= 0 && i < n && j >= 0 && j < m && g[i][j] == '#';
}
bool changecolor(int p, int q)
{
	for(int i = 0; i < 2; i ++)
		for(int j = 0; j < 2; j ++)
			if(check(p+i, q+j))
				g[p+i][q+j] = red[i*2+j];
			else 
				return 0;
	return 1;
}
int main()
{
	f1 = fopen("input.in", "r");
	f2 = fopen("output.out", "w");

	int numcase;
	fscanf(f1, "%d", &numcase);
	for(int cas = 1; cas <= numcase; cas ++)
	{
		fscanf(f1, "%d%d", &n, &m);
		for(int i = 0; i < n; i ++)
			fscanf(f1, "%s", g[i]);
		int ok = 1;
		for(int i = 0; i < n && ok; i ++)
			for(int j = 0; j < m && ok; j ++)
				if(g[i][j] == '#')
					ok = changecolor(i,j);
		fprintf(f2, "Case #%d:\n", cas);
		if(!ok) fprintf(f2, "Impossible\n");
		else
			for(int i = 0; i < n; i ++)
				fprintf(f2, "%s\n", g[i]);

	}

	fclose(f1);
	fclose(f2);

	return 0;
}