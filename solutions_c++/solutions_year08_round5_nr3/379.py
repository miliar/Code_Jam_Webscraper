#include<cstdio>
#include<algorithm>
using namespace std;
#define N ((1<<10)+10)
int E[N][N];
int board[20][20];
int boardmask[20];
int dp[11][N];


int gen(){
	int clear = 0;
	for(int i = 0; i < 10; ++i) clear |= 1<<i;

	for(int i = 0; i < (1<<10); ++i){
		int invalid = i;
		invalid = invalid | (invalid << 1);
		invalid = invalid | (invalid >> 1);
		invalid = invalid & clear;
	       	for(int j = 0; j < (1<<10); ++j) if ((invalid & j) == 0) {  E[i][j] = 1;} 
	}

}

int countbits(int a){
	int ret = 0;
	for(int i = 0; i < 12; ++i) if (a & (1<<i)) ret++;
	return ret;
}


int main(){
	gen();

	int c;
	scanf("%d\n",&c);
	for(int testCase = 1; testCase <= c; ++testCase){
		int m,n;
		char buffer[100];
		scanf("%d %d\n",&m,  &n);
		for(int i = 0; i < m; ++i){
			int mask = 0;
			scanf("%s\n",buffer);
			for(int j = 0; j < n; ++j) {
				board[i][j] = buffer[j] == 'x' ? 0 : 1;
				if (board[i][j] == 1) mask |= 1<<j;	
			}
		}
		for(int i = 0; i < max(n,m); ++i) boardmask[i] = 0;
		for(int i = 0; i < m; ++i) for(int j = 0; j < n; ++j) if (board[i][j]) boardmask[j] |= 1<<i;

		
		int limit = 1<<m;
		for(int i = 0; i < limit; ++i) if ((i & boardmask[0]) == i) dp[0][i] = countbits(i); else dp[0][i] = 0;



		for(int col = 1; col < n; ++col){
			for(int mask = 0; mask < limit; ++mask) 
			if ((mask & boardmask[col]) == mask){
				int best = 0;
				for(int prevmask = 0; prevmask < limit; ++prevmask) if (E[prevmask][mask]) best = max(best, dp[col-1][prevmask]);
				dp[col][mask] = best + countbits(mask);
			}
			else dp[col][mask] = 0;
		}


		int ret = 0;
		for(int mask = 0; mask < limit; ++mask) ret = max(ret, dp[n-1][mask]);
		printf("Case #%d: %d\n",testCase, ret);
	}
}
