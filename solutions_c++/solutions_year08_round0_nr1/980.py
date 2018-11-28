#include <stdio.h>
#include <string.h>

#define MAX 100
#define EMAX 100
#define QMAX 1000

char engineName[EMAX][MAX];
char quiries[QMAX][MAX];

int GetLength(int engine, int point, int end)
{
	int result = 0;

	for(int i=point;i<end;i++)
	{
		if(!strcmp(engineName[engine], quiries[i]))
			break;

		result++;
	}

	return result;
}

int main()
{
	FILE *fp = fopen("input.txt","r");
	FILE *fp2 = fopen("output.txt","w");

	int N;
	int S;
	int Q;

	int result;
	int point;

	fscanf(fp, "%d\n",&N);

	for(int i=0;i<N;i++)
	{
		fscanf(fp, "%d\n",&S);

		for(int j=0;j<S;j++)
		{
			fgets(engineName[j], EMAX, fp);
			if(engineName[j][strlen(engineName[j]) - 1] == '\n')
				engineName[j][strlen(engineName[j]) - 1 ] = 0;
			//printf("%s<<\n", engineName[j]);
		}

		fscanf(fp, "%d\n", &Q);
		//printf(">>%d\n",Q);

		for(j=0;j<Q;j++)
		{
			fgets(quiries[j], QMAX, fp);
			if(quiries[j][strlen(quiries[j]) - 1] == '\n')
				quiries[j][strlen(quiries[j]) - 1 ] = 0;

		//	printf("%s<<\n",quiries[j]);
		}

		point = 0;
		result = 0;

		int maxLen;
		int len;

		while(point < Q)
		{
			maxLen = 0;

			for(int k=0;k<S;k++)
			{
				len = GetLength(k, point, Q);

				if(len > maxLen)
					maxLen = len;
			}

			point += maxLen;
			result++;
		}

		if(result > 0)
			result--;

		fprintf(fp2, "Case #%d: %d\n", i+1, result);

	}

	fclose(fp2);
	fclose(fp);

	return 0;
}