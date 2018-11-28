#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define max(a, b) ((a)>(b)?(a):(b))

//char A[] = "abc";
char A[] = "welcome to code jam";
int lenA = strlen(A);
int count(char B[], int lenB)
{
	int i, n;
	int** L = (int**)malloc(sizeof(int*)*lenA);
	for(i=0;i<lenA;i++)
		L[i] = (int*)calloc(lenB, sizeof(int));
	
	L[0][0] = (A[0] == B[0] ? 1 : 0);
	// fill top border (i=0)
	for(n=1;n<lenB;n++)
	{
		L[0][n] = L[0][n-1];
		if(B[n] == A[0])
			L[0][n] = (L[0][n]+1)%10000;
	}
	for(i=1;i<lenA;i++)
	{
		L[i][0] = 0;
	}
	// fill table
	for(i=1;i<lenA;i++)
	{
		for(n=1;n<lenB;n++)
		{
			L[i][n] = L[i][n-1];
			if(A[i] == B[n])
			{
				L[i][n] = max(L[i][n], (L[i-1][n-1]+L[i][n-1])%10000);
			}
		}
	}
	return L[lenA-1][lenB-1];
}

int main()
{
	int i, N;
	char B[600];
	
	scanf("%d ", &N);
	for(i=0;i<N;i++)
	{
		fgets(B, 600, stdin);
		printf("Case #%d: %04d\n", i+1, count(B, strlen(B)));
	}
	return 0;
}
