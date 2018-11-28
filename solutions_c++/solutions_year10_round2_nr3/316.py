#include <stdio.h>
#define MAX 500
#define MOD 100003
long long sol[505][505], dap[505];
long long combi[505][505];
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	long long n, T, i, j, k;
	combi[0][0] = 1;
	for(i=1;i<=MAX;i++){
		combi[i][0] = 1;
		for(j=1;j<=MAX;j++){
			combi[i][j] = combi[i-1][j-1] + combi[i-1][j];
		}
	}
	for(i=2;i<=MAX;i++){
		sol[i][1] = 1;
		for(j=1;j<=MAX;j++){
			if(sol[i][j] != 0){
				for(k=i+1;k<=MAX;k++){
					sol[k][i] += sol[i][j] * combi[k-i-1][i-j-1];
					sol[k][i] %= MOD;
				}
				dap[i] = (dap[i]+sol[i][j])%MOD;
			}
		}
	}
	for(scanf("%lld",&T);T>0;T--){
		scanf("%lld",&n);
		static int t=1;
		printf("Case #%d: %lld\n", t++, dap[n]);
	}
	return 0;
}