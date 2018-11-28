#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

#define MAX_N 100001

typedef struct {
	long int x, y;
} Tree;

Tree tree[MAX_N];

long int N, M;
long int triangles;

void LoadData(FILE *inFile)
{
	// Cargar los datos de los árboles
	long int i, n, A, B, C, D, x0, y0, m;
	long int X, Y;

	fscanf(inFile, "%ld %ld %ld %ld %ld %ld %ld %ld", &n, &A, &B, &C, &D, &x0, &y0, &m);

	N = n;
	M = m;

	tree[0].x = X = x0;
	tree[0].y = Y = y0;

	for (i=1; i<n; i++)
	{
		tree[i].x = X = ((long long)A * (long long)X + (long long)B) % (long long)M;
		tree[i].y = Y = ((long long)C * (long long)Y + (long long)D) % (long long)M;
	}
}

void SolveCase()
{
	long int i, j, k;

	triangles = 0;

	// Probar cada tripleta de árboles para revisar su centro
	for (i=0; i<N-2; i++)
		for (j=i+1; j<N-1; j++)
			for (k=j+1; k<N; k++)
			{
				// Verificar si el triángulo en esos vértices tiene centro entero
			    long long centerX, centerY;

				centerX = tree[i].x + tree[j].x + tree[k].x;
				centerY = tree[i].y + tree[j].y + tree[k].y;

				if ( centerX % 3 == 0 && centerY % 3 == 0 )
					triangles++;
			}
}

int main()
{
	FILE *inFile, *outFile;

	inFile = fopen("input.txt", "rt");
	outFile = fopen("output.txt", "wt");

	int i, numCases;

	fscanf(inFile, "%d", &numCases);

	for (i=0; i<numCases; i++)
	{
		LoadData(inFile);

		SolveCase();

		fprintf(outFile, "Case #%d: %ld\n", i+1, triangles);

//		system("PAUSE");
	}

	fclose(inFile);
	fclose(outFile);

	return 0;
}
