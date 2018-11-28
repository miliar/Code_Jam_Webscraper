#include <stdio.h>
#include <string.h>


void sort(int* a, int c)
{
	int t;
	for(int i=1;i<c;i++)
		for(int j=i-1;(j>=0)&&(a[j+1]<a[j]);j--)
		{
			t = a[j+1];
			a[j+1] = a[j];
			a[j] = t;
		}
}

void main(void){
	FILE* fin = fopen("scaler.in","rt");
	FILE* fout = fopen("scaler.out","wt");

	int N;
	fscanf(fin,"%d",&N);
	for(int i=0;i<N;i++){
		int dimension;
		int X[800],Y[800];
		memset(X,0,sizeof(X));memset(Y,0,sizeof(Y));

		fscanf(fin, "%d\n", &dimension);
		for (int j=0;j<dimension;j++) fscanf(fin,"%d", &X[j]);
		for (int j=0;j<dimension;j++) fscanf(fin,"%d", &Y[j]);
		sort(X,dimension);
		sort(Y,dimension);
		__int64 result = 0;
		
		for (int j=0;j<dimension;j++)
			result += __int64(X[j])*__int64(Y[dimension-1-j]);
		

		fprintf(fout,"Case #%d: %I64d\n",i+1, result);

	}

	fclose(fin);
	fclose(fout);
}