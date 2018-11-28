#include<cstdio>
#include<cstdlib>

#define MAXN 15
#define MAXX 1050

using namespace std;

int popcount(int x) {
	int ans = 0;
	while(x) {
		if(x&1) ans++;
		x>>=1;
	}
	return ans;
}

int main() {
	FILE *fin = fopen("C.in","r"), *fout = fopen("C.out","w");
	int C, M, N, dp[MAXN][MAXX], broken[MAXN];
	fscanf(fin,"%d",&C);
	for(int k = 1; k<=C; k++) {
		for(int i = 0; i<MAXN; i++) {
			for(int j = 0; j<MAXX; j++) {
				dp[i][j] = 0;
			}
			broken[i] = 0;
		}
		fscanf(fin,"%d%d",&N,&M);
		for(int i = 0; i<N; i++) {
			for(int j = 0; j<M; j++) {
				broken[i] <<= 1;
				char c;
				fscanf(fin,"%c",&c);
				while(c != '.' && c!='x') {
					fscanf(fin,"%c",&c);
				}
				if(c == 'x') {
					broken[i]++;
				}
			}
		}
		for(int j = 0; j<(1<<M); j++) {
			if((j & (j<<1)) == 0 && (j & (j>>1)) == 0 && (j & broken[0]) == 0) {
				dp[0][j] = popcount(j);
			} else {
				dp[0][j] = 0;
			}
		}
		for(int i = 1; i<N; i++) {
			for(int j = 0; j<(1<<M); j++) {
				if((((j & (j << 1)) == 0) && (j & (j>>1))==0) && (j&broken[i])==0) {
					for(int k = 0; k<(1<<M); k++) {
						if((j & (k << 1)) == 0 && (j & (k >> 1)) == 0) {
							if(dp[i-1][k] + popcount(j) > dp[i][j]) {
								dp[i][j] = dp[i-1][k] + popcount(j);
							}
						}
					}
				}
			}
		}
		int ans = 0;
		for(int i = 0; i<(1<<M); i++) {
			if(dp[N-1][i] > ans) ans = dp[N-1][i];
		}
		fprintf(fout,"Case #%d: %d\n",k,ans);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}
