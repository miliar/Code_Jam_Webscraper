#include <stdio.h>
#include <string.h>

char *searchSentence = "welcome to code jam";
int lenInSentence;
char inStr[501];

long int oldSolution[501], newSolution[501];

long int SolveCase()
{
	int i,j, k;

	memset(oldSolution, 0, sizeof(oldSolution));

	// Buscar las w y marcarlas como combinaciones de 1 de largo
	for (i=0; i<lenInSentence; i++)
	{
		if (inStr[i] == 'w')
			oldSolution[i] = 1;
	}

	// Buscar cada letra ahora y marcar si aumenta la frase
	for (i=1; i<strlen(searchSentence); i++)
	{
		memset(newSolution, 0, sizeof(newSolution));

		// Recorrer cada letra de la frase de entrada buscando si coincide con la letra actual
		for (j=0; j<lenInSentence; j++)
		{
			if (inStr[j] == searchSentence[i])
			{
				// Ir hacia atrás e ir sumando las que puede concatenar
				long int sum = 0;
				for (k=j-1; k>=0; k--)
				{
					if (inStr[k] == searchSentence[i-1])
						sum += oldSolution[k];
				}

				newSolution[j] = sum;
			}
		}

		// Ya tenemos la solucion hasta la letra i, se convierte ahora en oldSolution
		memcpy(oldSolution, newSolution, sizeof(newSolution));
	}

	// Sumar los totales en oldSolution, esta será la respuesta
	long int result = 0;

	for (i=0; i<lenInSentence; i++)
		result += oldSolution[i];

	return result;
}

int main()
{
	int testCase, N;
	long int result;
	FILE *inFile, *outFile;


	inFile = fopen("input.txt", "rt");
	outFile = fopen("output.txt", "wt");

	fgets(inStr, 501, inFile);
	sscanf(inStr, "%d", &N);

	for (testCase=1; testCase<=N; testCase++)
	{
		fgets(inStr, 500, inFile);
		lenInSentence = strlen(inStr);

		result = SolveCase();

		result = result % 10000L;

		fprintf(outFile, "Case #%d: %04d\n", testCase, result);
	}

	fclose(inFile);
	fclose(outFile);

	return 0;
}

