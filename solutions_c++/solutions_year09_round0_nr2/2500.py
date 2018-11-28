#include <iostream>
#include <queue>
using namespace std;
const int MAXN = 101;
int n, m, cnt, mp[MAXN][MAXN], DX[] = {1, 0, 0, -1}, DY[] = {0, 1, -1, 0}, res[MAXN][MAXN];
char flag[MAXN][MAXN];
bool used[MAXN][MAXN];

bool f(int i, int j){
	bool flag = true;
	for(int k = 0; k < 4; ++k){
		int x = i + DX[k], y = j + DY[k];
		if(x > 0 && x <= n && y > 0 && y <= m && mp[i][j] > mp[x][y]) return false;
	}
	return true;
}
void solve(int i, int j){
	if(used[i][j]) return;
	int temp = 10001;
	for(int k = 0; k < 4; ++k){
		int x = i + DX[k], y = j + DY[k];
		if(x > 0 && x <= n && y > 0 && y <= m && mp[x][y] < mp[i][j] && mp[x][y] <= temp){
			temp = mp[x][y];
			solve(x, y);
			flag[i][j] = flag[x][y];
		}
	}
	return;
}
void dfs(int i, int j){
	if(used[i][j]) return;
	used[i][j] = true;
	res[i][j] = cnt;
	for(int k = 0; k < 4; ++k){
		int x = i + DX[k], y = j + DY[k];
		if(x > 0 && x <= n && y > 0 && y <= m && !used[x][y] && flag[i][j] == flag[x][y]) dfs(x, y);
	}
	return;
}

int main(){
	freopen("D:\\B-small-attempt0.in", "r", stdin);
	freopen("D:\\problem.out", "w", stdout);
	int cases, caseNum = 1;
	scanf("%d", &cases);
	while(cases--){
		scanf("%d%d", &n, &m);
		for(int i = 1; i <= n; ++i)
			for(int j = 1; j <= m; ++j)
				scanf("%d", &mp[i][j]);
		memset(used, false, sizeof(used));
		char ch = 'a';
		for(int i = 1; i <= n; ++i)
			for(int j = 1; j <= m; ++j)
				if(f(i, j)){
					flag[i][j] = ch++;
					used[i][j] = true;
				}
		for(int i = 1; i <= n; ++i)
			for(int j = 1; j <= m; ++j)
				if(!used[i][j]) solve(i, j);
		memset(used, false, sizeof(used));
		cnt = 0;
		for(int i = 1; i <= n; ++i)
			for(int j = 1; j <= m; ++j)
				if(!used[i][j]){
					dfs(i, j);
					++cnt;
				}
		printf("Case #%d:\n", caseNum++);
		for(int i = 1; i <= n; ++i)
		{
			printf("%c", res[i][1] + 'a');
			for(int j = 2; j <= m; ++j) printf(" %c", res[i][j] + 'a');
			putchar('\n');
		}
	}
	return 0;
}