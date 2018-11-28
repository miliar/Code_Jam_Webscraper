//be name oo
#include <cstdio>
#include <iostream>

using namespace std;

const int MAX_N = 1000 + 10, C = 10;

int c, l, p;
int dp[C + 1][MAX_N][MAX_N];
//int par[C + 1][MAX_N][MAX_N];

void cal_dp(int dp[MAX_N][MAX_N]){
	for(int len = 1; len <= (p - l); len++)
		for(int s = l; s + len <= p; s++){
			if(s + len <= s * c){
				dp[s][len] = 0;
				continue;
			}
			dp[s][len] = MAX_N;
			for(int j = 1; j < len; j++)
				if(dp[s][len] > 1 + max(dp[s][j], dp[s + j][len - j])){
					dp[s][len] = 1 + max(dp[s][j], dp[s + j][len - j]);
					//par[s][len] = s + j;
				}
			/*if(dp[s][len] < 1 + max(dp[s][s * (c - 1)], dp[s * c][len - s * (c - 1)])){
				printf("bad! %d %d\n", s, len);
				return;
			}*/
		}
}

int main(){
	l = 1;
	p = 1000;
	for(c = 2; c <= C; c++){
		cerr<<"salam!\n";
		cal_dp(dp[c]);
	}
	/*for(int s = l; s < p; s++){
		printf("%2d:  ", s);
		for(int len = 1; s + len <= p; len++)
			printf(" %2d", dp[s][len]);
		printf("\n");
	}
	for(int s = l; s < p; s++){
		printf("%2d:  ", s);
		for(int len = 1; s + len <= p; len++)
			printf(" %2d", par[s][len]);
		printf("\n");
	}*/
	//cerr<<"salam!\n";
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++){
		int nl, np, nc;
		scanf("%d %d %d", &nl, &np, &nc);
		printf("Case #%d: %d\n", i, dp[nc][nl][np - nl]);
	}
	return 0;
}
