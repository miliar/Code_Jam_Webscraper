#include<stdio.h>

const int MAX_N = 1000;

int main(){
	int i, j, l;
	char inName[256] = "C-small-attempt0.in";
	char outName[256] = "C-small-attempt0.out";
	FILE *fin = fopen(inName, "r");
	FILE *fout = fopen(outName, "w");

	int T;
	int R, k, N;
	int g[MAX_N];
	int nextIndex[MAX_N];
	int maxSum[MAX_N];

	fscanf(fin, "%d", &T);

	for(i=0; i<T; i++){
		fscanf(fin, "%d %d %d", &R, &k, &N);
		for(j=0; j<N; j++)	fscanf(fin, "%d", &g[j]);
		
		for(j=0; j<N; j++){
			int sum = 0;
			for(l=0; l<N; l++){
				if(k-sum >= g[(j+l)%N])		sum+=g[(j+l)%N];
				else						break;
			}
			maxSum[j] = sum;
			nextIndex[j] = (j+l)%N;
		}
		
		int cost = 0;								//BigInt
		int curIndex =0;
		for(j=0; j<R; j++){
			cost += maxSum[curIndex];				//BigInt
			curIndex = nextIndex[curIndex];
		}

		fprintf(fout, "Case #%d: %d\n", i+1, cost);	//BigInt
	}

	fcloseall();
	return 0;
}