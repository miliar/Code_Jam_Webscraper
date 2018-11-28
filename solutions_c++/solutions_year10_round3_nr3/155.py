#include <stdio.h>
#include <string.h>

#define MAXN 40

int mp[MAXN][MAXN];
int dp[MAXN][MAXN];
int num[MAXN * MAXN];
char s[200];

int main(){
	freopen("D:\\C-small-attempt0.in", "r", stdin);
	freopen("D:\\out.txt", "w", stdout);
	int cases;
	scanf("%d", &cases);
	for(int case_t = 1; case_t <= cases; ++case_t){
		int n, m;
		scanf("%d%d", &n, &m);
		for(int i = 1; i <= n; ++i){
			scanf("%s", s + 1);
			for(int j = 1; j <= m / 4; ++j){
				char ch = s[j];
				int val;
				if(ch >= 'A' && ch <= 'F') val = ch - 'A' + 10;
				else val = ch - '0';
				for(int k = 1; k <= 4; ++k){
					mp[i][(j - 1) * 4 + 4 - k + 1] = val & 1;
					val >>= 1;
				}
			}
		}
		int currMax = 0, x = 1, y = 1;
		for(int i = n; i > 0; --i){
			for(int j = m; j > 0; --j){
				dp[i][j] = 1;
				if(i + 1 > n || j + 1 > m || mp[i][j] != mp[i + 1][j + 1]) continue;
				int mini = dp[i + 1][j] < dp[i][j + 1]? dp[i + 1][j]: dp[i][j + 1];
				if(mini == 1){
					if(mp[i + 1][j] == mp[i][j + 1] && mp[i + 1][j] != mp[i][j]) ++dp[i][j];
				}
				else dp[i][j] = mini + 1;
				if(mp[i][j] != mp[i + dp[i][j] - 1][j + dp[i][j] - 1]) --dp[i][j];
				if(dp[i][j] > currMax){currMax = dp[i][j]; x = i; y = j;}
				else if(dp[i][j] == currMax && (i < x || (i == x) && j < y)){x = i; y = j;}
			}
		}
		
		memset(num, 0, sizeof(num));
		int total = 0;
		int sum = 0;
		while(currMax >= 2){
			if(!num[currMax]) ++total;
			sum += currMax * currMax;
			++num[currMax];
			for(int i = x; i < x + currMax; ++i)
				for(int j = y; j < y + currMax; ++j)
					mp[i][j] = -1;
			currMax = 0;x = 1;y = 1;
			for(int i = n; i > 0; --i){
				for(int j = m; j > 0; --j){
					if(mp[i][j] == -1){
						dp[i][j] = 0;continue;
					}
					dp[i][j] = 1;
					if(i + 1 > n || j + 1 > m || mp[i + 1][j + 1] == -1 || mp[i + 1][j + 1] != mp[i][j]) continue;
					int mini = dp[i + 1][j] < dp[i][j + 1]? dp[i + 1][j]: dp[i][j + 1];
					if(mini == 0) continue;
					else if(mini == 1){
						if(mp[i + 1][j] == mp[i][j + 1] && mp[i + 1][j] != mp[i][j]) ++dp[i][j];
					}
					else dp[i][j] = mini + 1;
					if(mp[i][j] != mp[i + dp[i][j] - 1][j + dp[i][j] - 1]) --dp[i][j];
					if(dp[i][j] > currMax){currMax = dp[i][j]; x = i; y = j;}
					else if(dp[i][j] == currMax && (i < x || (i == x) && j < y)){x = i; y = j;}
				}
			}
		
		}
		if(sum != n * m) ++total;
		printf("Case #%d: %d\n", case_t, total);
		for(int i = n * m; i >= 2; --i)
			if(num[i]) printf("%d %d\n", i, num[i]);
		if(sum != n * m)
			printf("1 %d\n", n * m - sum);
	}
	return 0;
}