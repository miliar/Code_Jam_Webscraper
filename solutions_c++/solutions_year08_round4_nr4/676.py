#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

const long MaxN = 1005;

int n, k;
char lajn[MaxN];
char tmp[MaxN];

FILE *fin, *fout;

void solve(int tt){
	vector<int> p;
	for (int i = 0; i < k; i++) p.push_back(i);
	
	int best = 10000;
	do{
		for (int b = 0; b < n; b+=k){
			for (int i = 0; i < k; i++) tmp[b + i] = lajn[b + p[i]];
		}
		int curr = 1;
		for (int i = 1; i < n; i++) if (tmp[i] != tmp[i-1]) curr++;
		best <?= curr;		
	} while(next_permutation(p.begin(), p.end()));
	
	fprintf(fout, "Case #%d: %d\n", tt, best-1);
}

int main(){
	fin = fopen("D_small.in", "r");
	fout = fopen("D_small.out", "w");
	
	int test;
	fscanf(fin, "%d", &test);
	for (int tt = 1; tt <= test; tt++){
		fscanf(fin, "%d\n", &k);
		fgets(lajn, MaxN, fin);
		n = strlen(lajn);
		solve(tt);
	}

	fclose(fin); fclose(fout);
	return 0;
}

