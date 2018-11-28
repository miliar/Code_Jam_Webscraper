#include <iostream>
#include <cstdio>
using namespace std;

const long MaxN = 105;

long n;
long long A, B, C, D;
long x[MaxN], y[MaxN];

long long MOD;

FILE *f;
FILE *fin;

void solve(int casa){
	long res = 0;
	for (int i = 0; i < n; i++) for (int j = i + 1; j < n; j++) for (int k = j + 1; k < n; k++){
		long  _x = x[i] + x[j] + x[k];
		long  _y = y[i] + y[j] + y[k];
		if (_x % 3 == 0 && _y % 3 == 0) res++;
	}
	
	fprintf(f,"Case #%d: %ld\n", casa, res);
} 


int main(){
	f = fopen("a_small.out", "w");
	fin = fopen("A_small.in", "r");

	int N;
	fscanf(fin, "%d", &N);
	for (int test = 1; test <= N; test++){
		fscanf(fin, "%ld %ld %ld %ld %ld %ld %ld %ld", &n, &A, &B, &C, &D, &x[0], &y[0], &MOD);
		
		long long X = x[0], Y = y[0];
		for (int i = 1; i < n; i++){
			X = (A * X + B) % MOD;
			Y = (C * Y + D) % MOD;
			x[i] = X; y[i] = Y;
		}
		solve(test);
	
	}
	
	fclose(fin);
	fclose(f);
	int asd; cin >> asd;
	return 0;
}	
