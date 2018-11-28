#include <stdio.h>
#include <stdlib.h>

void swap(int &a, int &b)
{
	int tmp = a;
	a=b;
	b=tmp;
}

void MinToMax(int* v, int N)
{
	int PosMin;
	for (int i=0; i<N-1; i++)
	{
		PosMin = i;
		for (int j=i+1; j<N; j++)
		{
			if (v[j]<v[PosMin])
				PosMin = j;
		}
		swap(v[i], v[PosMin]);
	}
}

void MaxToMin(int* v, int N)
{
	int PosMax;
	for (int i=0; i<N-1; i++)
	{
		PosMax = i;
		for (int j=i+1; j<N; j++)
		{
			if (v[j]>v[PosMax])
				PosMax = j;
		}
		swap(v[i], v[PosMax]);
	}
}

int ScalarProduct(int* v1, int *v2, int N)
{
	int result =0;
	for (int i=0; i<N; i++)
		result += v1[i]*v2[i];
	return result;
}

void StrToVector(char* str, int* v, int N)
{
	int curr = 0;
	for (int i=0; i<N; i++)
	{
		char* MyInt = new char [7];
		int MyCurr=0;
		while ((str[curr] != ' ') && (str[curr] != '\0'))
		{
			MyInt[MyCurr] = str[curr];
			MyCurr++;
			curr++;
		}
		MyInt[MyCurr] = '\0';
		curr++;
		v[i] = atoi(MyInt);
		delete [] MyInt;
	}
}


void main()
{
	int NCases;
	char* NCasesStr = new char [20];
	int* v1;
	int* v2;

	char* v1Str;
	char* v2Str;

	int Size;
	char *SizeStr;

	FILE* InFile = fopen("input.txt", "a+");
	FILE* OutFile = fopen("output.txt", "a+");

	fgets(NCasesStr, 20, InFile);
	NCases = atoi(NCasesStr);

	for (int i=0; i<NCases; i++)
	{
		SizeStr = new char [20];
		fgets(SizeStr, 20, InFile);
		Size = atoi(SizeStr);

		v1 = new int [Size];
		v2 = new int [Size];

		v1Str = new char [6000];
		v2Str = new char [6000];

		fgets(v1Str, 6000, InFile);
		fgets(v2Str, 6000, InFile);

		StrToVector(v1Str, v1, Size);
		StrToVector(v2Str, v2, Size);

	/*	printf ("FirstVector:\n");
		for (int j=0; j<Size; j++)
			printf("%d ", v1[j]);
		printf ("SecondVector:\n");
		for (int j=0; j<Size; j++)
			printf("%d ", v2[j]);*/


		MinToMax(v1, Size);
		MaxToMin(v2, Size);
		int res = ScalarProduct(v1, v2, Size);
		fprintf(OutFile, "Case #%d: %d\n", i+1, res);

		delete [] v1;
		delete [] v2;
		delete [] v1Str;
		delete [] v2Str;
		delete [] SizeStr;
	}

	delete [] NCasesStr;

	fclose(InFile);
	fclose(OutFile);
}