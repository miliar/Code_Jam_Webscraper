#include <stdio.h>

int main()
{
	int t;
	char tile[100][100];
	int n[100][100];

	scanf("%d", &t);
	int cnt = 0;
	FILE *fout = fopen("out.out", "w");
	while (t--)
	{
		int x,y;
		scanf("%d %d", &y, &x);
		for (int i=0; i<y;i++)
			scanf("%s", tile[i]);

		for (int i=0; i<y; i++)
			for (int j=0; j<x; j++)
				n[i][j] = 0;

		bool im = false;
		for (int i=0; i<y;i++)
		{
			if (im) break;

			for (int j=0; j<x; j++)
				if (tile[i][j] == '#' && n[i][j] == 0)
				{	
					if (i == y - 1 || j == x - 1)
					{
						im = true;
						break;
					}	

					if (tile[i][j+1] != '#' || tile[i+1][j] != '#' ||tile[i][j+1] != '#' || tile[i+1][j+1] != '#')
					{
						im = true;
						break;
					}

					n[i][j] = 1;
					n[i][j+1] = 2;
					n[i+1][j] = 3;
					n[i+1][j+1] = 4;
				}
		}

		
		fprintf(fout, "Case #%d:\n", ++cnt);
		if (im)
			fprintf(fout, "Impossible\n");
		else 
		{
			for (int i=0; i<y; i++)
			{
				for (int j=0; j<x; j++)
				{
					if (n[i][j] == 0) fprintf(fout, ".");
					if (n[i][j] == 1) fprintf(fout, "/");
					if (n[i][j] == 2) fprintf(fout, "\\");
					if (n[i][j] == 3) fprintf(fout, "\\");
					if (n[i][j] == 4) fprintf(fout, "/");
				}
				fprintf(fout,"\n");
			}
		}
	}
	fclose(fout);
	return 0;
}