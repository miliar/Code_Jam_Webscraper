#include <stdio.h>
#include <string.h>

char oldpath[100][120];
char newpath[100][120];

int commonPath(char* a, char *b)
{
	int path=0;

	while (*a != NULL && *b != NULL)
	{
		a++;
		b++;
		if (*a == NULL && *b == '/') path++;
		if (*a == '/' && *b == NULL) path++;
		if (*a == NULL && *b == NULL) path++;
		if (*a == '/' && *b == '/') path++;
		if (*a != *b) {
			break;
		}
	}

	return path ;
}

int main()
{
	FILE *fout = fopen("a.txt","w");
	int caseN;
	scanf("%d",&caseN);
	for (int caseID=1; caseID<=caseN; caseID++)
	{
		int n, m;
		scanf("%d %d", &n, &m);
		for (int i=0; i<n; i++)
		{
			for(int j=0; j<120; j++) oldpath[i][j] =0;
			scanf("%s", oldpath[i]);
		}
		for (int i=0; i<m; i++)
		{
			for(int j=0; j<120; j++) newpath[i][j] =0;
			scanf("%s", newpath[i]);
		}

		int mk = 0;
		for (int i=0; i<m; i++)
		{
			int sn = strlen(newpath[i]);
			int path = 0;

			for (int j=0; j<sn; j++)
				if (newpath[i][j] == '/') path++;

			int min=path;
			for (int j=0; j<n; j++)
			{
				int cp = path - commonPath(newpath[i], oldpath[j]);
				if (min > cp)
					min = cp;
			}
			for (int j=0; j<i; j++)
			{
				int cp = path - commonPath(newpath[i], newpath[j]);
				if (min > cp)
					min = cp;
			}
			mk += min;
		}

		fprintf(fout, "Case #%d: %d\n", caseID, mk);
	}

	fclose(fout);
	return 0;
}