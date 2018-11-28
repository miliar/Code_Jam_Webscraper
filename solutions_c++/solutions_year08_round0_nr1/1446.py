#include<cstdio>
#include<map>
#include<string>
#include<iostream>
using namespace std;

#define INF 1000000
int s,q;
map<string,int> engines;
int queries[1010];
int dp[1010][105];

int main(){
	int n;
	scanf("%d\n",&n);
	for(int testCase = 1; testCase <= n; ++testCase){
		engines.clear();

		char buffer[256];
		scanf("%d\n",&s);
		for(int i = 0; i < s; ++i){
			gets(buffer);
			int bsize = strlen(buffer);
			if (buffer[bsize-1]=='\r') buffer[bsize-1] = 0;
			engines[string(buffer)] = i;
			//cout << string(buffer) << "   " << i << endl;
		}	

		scanf("%d\n",&q);
		for(int i = 1; i <= q; ++i){
			gets(buffer);
			int bsize = strlen(buffer);
			if (buffer[bsize-1] == '\r') buffer[bsize-1] = 0;
			queries[i] = engines.find(string(buffer))->second;
		}	

		for(int i = 0; i < s; ++i) dp[0][i] = 0;
		for(int i = 1; i <= q; ++i){
			for(int j = 0; j < s; ++j){
				if(queries[i]==j) {
					dp[i][j] = INF;
					continue;
				}
				int best = INF;
				for(int k = 0; k < j; ++k) best = min(best, dp[i-1][k]+1);
				best = min(best, dp[i-1][j]);
				for(int k = j+1; k < s; ++k) best = min(best, dp[i-1][k]+1);
				dp[i][j] = best;
			}
		}
		/*
		for(int row = 0; row < s; ++row){
			for(int col = 0; col <= q; ++col) if(dp[col][row] == INF) printf("X "); else printf("%d ",dp[col][row]);
			printf("\n");
		}
		*/


		int ret = INF;
		for(int i = 0; i < s; ++i) ret = min(ret, dp[q][i]);
		printf("Case #%d: %d\n",testCase, ret);
	}


}
