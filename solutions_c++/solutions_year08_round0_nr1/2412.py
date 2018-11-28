/* Copyright (c) cnHawk */
#include <stdio.h>
#include <string>
#include <map>
using namespace std;

char s[128];
map <string, int> mp;
int dp[1024][128];

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("large", "w", stdout);
	int n, kase, S, Q;
	scanf("%d", &n);
	for(kase = 1; kase <= n; kase++){
		int i, j, k, t;
		mp.clear();
		scanf("%d\n", &S);
		for(i = 0; i < S; i++){
			gets(s);
			mp[(string)s] = i;
		}
		scanf("%d\n", &Q);
		for(i = 0; i < Q; i++){
			gets(s);
			k = mp[(string)s];
			if(i == 0) {
                memset(dp[0], 0, sizeof(dp[0]));
                dp[0][k] = 0x3fffffff;
            }
			else{
				for(j = 0; j < S; j++){
					if(j == k) {
                        dp[i][j] = 0x3fffffff;
                        continue;
                    }
					else dp[i][j] = dp[i-1][j];
					for(t = 0; t < S; t++) if(t != j) dp[i][j] <?= dp[i-1][t] + 1;
				}
			}
		}
		int ans = 0x3fffffff;
		if(Q <= 1){
			ans = 0;
		}
		else{
			for(j = 0; j < S; j++){
				if(ans > dp[Q-1][j]) ans = dp[Q-1][j];
			}
        }
		printf("Case #%d: ", kase);
		printf("%d\n", ans);

	}
	return 0;
}
