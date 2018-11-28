#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void main()
{
	FILE *InStream, *OutStream;
	InStream = fopen("in.txt", "a+");
	OutStream = fopen("out.txt", "w");

	int NumCases;
	fscanf(InStream, "%d", &NumCases);

	for (int Case=1; Case<=NumCases; Case++)
	{
		bool flag = true;
		int R;
		fscanf(InStream, "%d", &R);
		int C;
		fscanf(InStream, "%d", &C);

		char** Tiles = new char* [R];
		for (int i=0; i<R; i++)
		{
			Tiles[i] = new char [C+1];
			fscanf(InStream, "%s", Tiles[i]);
		}

		for (int i=0; i<R; i++)
		{
			for (int j=0; j<C; j++)
			{
				if (Tiles[i][j]=='#')
				{
					if ((i<R-1)&&(j<C-1)&&(Tiles[i+1][j]=='#')&&(Tiles[i][j+1]=='#')&&(Tiles[i+1][j+1]=='#'))
					{
						Tiles[i][j] = Tiles[i+1][j+1] = '/';
						Tiles[i+1][j] = Tiles[i][j+1] = 92;
					}
					else
						flag = false;
				}
			}
		}


		fprintf(OutStream, "Case #%d:\n", Case);
		if (flag)
			for (int i=0; i<R; i++)
				fprintf(OutStream, "%s\n", Tiles[i]);
		else
			fprintf (OutStream, "Impossible\n");

		for (int i=0; i<R; i++)
			delete [] Tiles[i];
		delete [] Tiles;
	}

	fclose(InStream);
	fclose(OutStream);
}