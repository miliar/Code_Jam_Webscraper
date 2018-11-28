#include<stdio.h>

int _pow(int a, int b){
	int ans = 1;
	for(int i=0; i<b; i++)
		ans *= a;
	return ans;
}

int main(){
	FILE *fin = fopen("A-large.in", "r");
	FILE *fout = fopen("output.txt", "w");

	int T, N, K;
	fscanf(fin, "%d", &T);

	for(int i=0; i<T; i++){
		fscanf(fin, "%d %d", &N, &K);
		if((K+1) % _pow(2, N) == 0)		fprintf(fout, "Case #%d: ON\n", i+1);
		else							fprintf(fout, "Case #%d: OFF\n", i+1);
	}

	fcloseall();
	return 0;
}