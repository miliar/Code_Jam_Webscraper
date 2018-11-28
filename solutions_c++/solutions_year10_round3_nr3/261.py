//be name oo
#include <cstdio>
#include <iostream>
#include <set>

#define FOR(i, n) for(int i = 0; i < (n); i++)

using namespace std;

const int MAX_N = 512 + 10;

struct sq{
	int r, c, sz;
	sq(int rr = 0, int cc = 0, int szz = 0){
		r = rr;
		c = cc;
		sz = szz;
	}
	friend bool operator < (const sq& a, const sq& b){
		if(a.sz != b.sz)
			return a.sz > b.sz;
		if(a.r != b.r)
			return a.r < b.r;
		return a.c < b.c;
	}
};

int n, m;
int tab[MAX_N][MAX_N];
int dp[MAX_N][MAX_N];
set<sq> chess;
char str[MAX_N];
int ans[MAX_N];

int main(){
	int t;
	scanf("%d", &t);
	for(int test = 1; test <= t; test++){
		scanf("%d %d", &n, &m);
		FOR(i, n){
			scanf(" %s", str);
			FOR(j, m / 4){
				int num = 0;
				if('0' <= str[j] && str[j] <= '9')
					num = str[j] - '0';
				else	num = str[j] - 'A' + 10;
				FOR(k, 4)
					tab[i][4 * j + 3 - k] = (bool)(num & (1 << k));
			}
		}
		chess.clear();
		for(int i = n - 1; i >= 0; i--)
			for(int j = m - 1; j >= 0; j--){
				if(i + 1 == n || j + 1 == m)
					dp[i][j] = 1;
				else if(tab[i][j] != tab[i + 1][j + 1] || tab[i + 1][j] != tab[i][j + 1] || tab[i][j] == tab[i + 1][j])
					dp[i][j] = 1;
				else	dp[i][j] = min(dp[i + 1][j + 1], min(dp[i + 1][j], dp[i][j + 1])) + 1;
				chess.insert(sq(i, j, dp[i][j]));
			}
		memset(ans, 0, sizeof ans);
		while(chess.size()){
			sq cur = *chess.begin();
			ans[cur.sz]++;
			for(int i = cur.r; i < cur.r + cur.sz; i++)
				for(int j = cur.c; j < cur.c + cur.sz; j++){
					chess.erase(sq(i, j, dp[i][j]));
					tab[i][j] = 2;
				}
			for(int i = cur.r + cur.sz - 1; i >= 0; i--)
				for(int j = cur.c + cur.sz - 1; j >= 0; j--){
					if(tab[i][j] == 2)
						continue;
					int dr = i + dp[i][j] - cur.r;
					int dc = j + dp[i][j] - cur.c;
					dr = min(dr, dc);
					dr = max(dr, 0);
					chess.erase(sq(i, j, dp[i][j]));
					dp[i][j] -= dr;
					chess.insert(sq(i, j, dp[i][j]));
				}
		}
		int ans1 = 0;
		for(int i = 0; i < MAX_N; i++)
			if(ans[i])
				ans1++;
		printf("Case #%d: %d\n", test, ans1);
		for(int i = MAX_N - 1; i >= 0; i--)
			if(ans[i])
				printf("%d %d\n", i, ans[i]);
	}
	return 0;
}
