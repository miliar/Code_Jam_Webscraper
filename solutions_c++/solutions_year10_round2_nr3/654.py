#include <stdio.h>
#define MOD 100003

int pd[600][600];
int pd2[600][600];

int binom(int N,int K){
	if(K<0) return 0;
	if(pd[N][K] == 0 && N>K) return pd[N][K] = (binom(N-1,K-1)+binom(N-1,K))%MOD;
	
	if(N<K) return 0;
	return pd[N][K];
}

int calc(int n,int k){
	if(k == 1){
		if(n < 1) return 0;
		else return 1;
	}
	if(pd2[n][k] != -1) return pd2[n][k]; 
	int resp = 0;
	int pos = n-k-1;
	for(int i = 1;i<k;i++){
		int var;
		var = binom(pos,k-i-1);
		resp=(resp+calc(k,i)*var%MOD)%MOD;
	}
	return pd2[n][k] = resp;
}

int main(){
	int T,n;
	scanf("%d",&T);
	for(int i =0;i<550;i++){
		for(int j = 0;j<550;j++){
			if(i == j) pd[i][j] = 1;
			else pd[i][j] = 0;
			pd2[i][j] = -1;
		}
	}
	for(int Case = 1;Case<=T;Case++){
		scanf("%d",&n);
		int resp = 0;
		for(int i =1;i<n;i++){
			resp=(resp+calc(n,i))%MOD;

		}
		printf("Case #%d: %d\n", Case,resp);
	}

	


	return 0;
}
