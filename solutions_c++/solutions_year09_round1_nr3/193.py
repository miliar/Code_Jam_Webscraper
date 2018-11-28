
#include <iostream>

using namespace std;

double x[10000][41];

int max(int a, int b){
	if(a > b)
		return a;
	return b;
}

double xxx(int n, int k){
	
	double rtn = 1.0;

	for(int i=0; i<=k-1; ++i){
		rtn *= ((double)n-i)/(k-i);
	}
	return rtn;
}

double comb(int c, int n, int j, int i){

	return xxx(j, n-i+j) * xxx(c -j, i-j) / xxx(c, n);
}

int main(){

	int T;
	int C, N;

	cin >> T;

	for(int testcase=1; testcase <= T; ++testcase){
		
		cin >> C >> N;
		
		for(int i=0; i<=C; ++i){
			x[0][i] = x[1][i] = 0.0;
		}
		x[1][N] = 1.0;

		for(int t=2; t<=10000; ++t){
			for(int i=0; i<=C; ++i){
				if(i < N){
					x[t][i] = 0.0;
				}else{
					x[t][i] = 0.0;
					for(int j=max(N, i-N); j<=i; ++j){
						x[t][i] += x[t-1][j]*comb(C, N, j, i);
					}
				}
			}
		}

		double exp = 0;

		for(int t = 1; t<=10000; ++t){
			exp += (x[t][C] - x[t-1][C]) * t;
		}
		
		printf("Case #%d: %.7lf\n", testcase, exp);
	}
	return 0;
}
