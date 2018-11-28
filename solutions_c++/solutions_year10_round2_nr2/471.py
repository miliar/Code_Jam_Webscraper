#include <stdio.h>

int x[100];
int v[100];

int c[100];
int m[100];


int main()
{
	FILE *fout = fopen("b.out","w");
	int caseN;
	scanf("%d",&caseN);
	for (int caseID=1; caseID<=caseN; caseID++)
	{
		int n, k, b, t;
		scanf("%d %d %d %d", &n, &k, &b, &t);
		for (int i=0; i<n; i++)
			scanf("%d", &x[i]);
		for (int i=0; i<n; i++)
			scanf("%d", &v[i]);

		for (int i=0; i<n; i++)
			if (x[i] + v[i] * t >= b) c[i] = 1; else c[i] = 0;

		for (int i=0; i<n; i++){
			m[i] = 0;
			for (int j=i+1; j<n; j++)
				if (v[i] > v[j] && (c[i] == 1 && c[j] == 0))
				{
					m[i]++;
				}
		}

		int cnt = 0;
		int min = 0;

		while (k--)
		{
			min = -1;
			for (int i=0; i<n; i++)
				if (c[i] == 1) {
					min = i; break;
				}

			if (min == -1) break;

			for (int i=0; i<n; i++)
				if (c[i] == 1 && m[i] < m[min]) min = i;

			cnt += m[min];
			c[min] = 0;
		}

		if (min != -1)
			fprintf(fout, "Case #%d: %d\n", caseID, cnt);
		else 
			fprintf(fout, "Case #%d: IMPOSSIBLE\n", caseID);
	}

	fclose(fout);
	return 0;
}