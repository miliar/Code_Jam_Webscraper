#include <stdio.h>
#include <string.h>
const int MAX = 2000;

int solve(int* queries, int S, int Q)
{
	int A[2000][200];
	int i,j,k,MIN;
	for(i=0;i<=Q;i++)
		for(j=0;j<=S;j++)
			A[i][j] = MAX;

	for(j=1;j<=S;j++) A[0][j] = 0;
	for(i=1;i<=Q;i++)
		for(j=1;j<=S;j++)
		{//A[i,j] query I search Engine J
			if (queries[i] == j) {A[i][j] = MAX; continue;}
			MIN = A[i-1][j];
			for (k=1;k<=S;k++)
				if (k != j)
					if (A[i-1][k]+1 < MIN) MIN = A[i-1][k]+1;
			A[i][j] = MIN;
		}

	MIN = MAX;
	for(j=1;j<=S;j++)
		if (A[Q][j]<MIN) MIN = A[Q][j];
	return MIN;
}


int main(void){
	FILE* fin = fopen("universe.in","rt");
	FILE* fout = fopen("universe.out","wt");

	int N;
	fscanf(fin,"%d",&N);
	for(int i=0;i<N;i++){
		char names[200][200];
		char str[200];
		int queries[2000];
		int Q=0,S=0;
		memset(queries,0,sizeof(queries));
		fscanf(fin, "%d\n", &S);
		for (int j=0;j<S;j++) fscanf(fin,"%[a-zA-Z0-9 ]\n", names[j]);
		fscanf(fin, "%d\n", &Q);
		for(int j=0;j<Q;j++) {
			fscanf(fin, "%[a-zA-Z0-9 ]\n", str);
			for(int k=0; k<S; k++)
				if (strcmp(str, names[k]) == 0) queries[j+1] = k+1;
		}

		fprintf(fout,"Case #%d: %d\n",i+1, solve(queries,S,Q));

	}

	fclose(fin);
	fclose(fout);
}