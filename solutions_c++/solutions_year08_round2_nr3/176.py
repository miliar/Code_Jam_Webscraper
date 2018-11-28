#include <iostream>
#include <cstdio>
using namespace std;

const int MaxN = 5001;

int num[MaxN];
int prev[MaxN], next[MaxN];
int K;

int n, d[MaxN];

FILE *f;
FILE *fin;

void solve(int test){
	prev[1] = K; next[K] = 1;
	for (int i = 1; i < K; i++) next[i] = i + 1;
	for (int i = 2; i <= K; i++) prev[i] = i - 1;
	
	int curr = 1;
	for (int k = 1; k <= K; k++){
		for (int t = 1; t < k; t++)	curr = next[curr];
		int post = next[curr];
		
		num[curr] = k;
			
		next[prev[curr]] = next[curr];
		prev[next[curr]] = prev[curr];
			
		curr = post;
	}
	
	fprintf(f, "Case #%d: ", test);
	for (int i = 0; i < n; i++) fprintf(f,"%d ", num[d[i]]);
	fprintf(f,"\n");
}

int main(){
	f = fopen("C_small.out", "w");
	fin = fopen("C_small.in", "r");
	
	int T;
	fscanf(fin, "%ld", &T);
	for (int test = 1; test <= T; test++){
		fscanf(fin, "%ld", &K);
		fscanf(fin, "%ld", &n);
		for (int i = 0; i < n; i++) fscanf(fin, "%ld", &d[i]);
		
		solve(test);
	}
	
	fclose(f);
	fclose(fin);
	
	return 0;
}
