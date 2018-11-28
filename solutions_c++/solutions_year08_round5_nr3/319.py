#include <iostream>
#include <vector>
using namespace std;
const int MAXN = 10;
bool data[MAXN][MAXN];
vector<int> state, num;
int m, n, f[1 << MAXN], g[1 << MAXN];
int grid[MAXN + 1];
void dfs(int pos, int x, int nn){
	if (pos == n){
		state.push_back(x);
		num.push_back(nn);
		return;
	}
	
	if ((x & 1) == 0) dfs(pos + 1, (x << 1) + 1, nn+ 1);
	dfs(pos + 1, x << 1, nn);
}
void Compress(){
	for (int i = 0; i != m; ++i){
		int x = 0;
		for (int j = 0; j != n; ++j) x = x * 2 + (data[i][j] ? 1 : 0);
		grid[i + 1] = x;
	}
}
bool match1(int x, int y){
	return (((x << 1) | (x >> 1)) & y) == 0;
}
bool match2(int x, int y){
	if ((x | grid[y]) != grid[y]) return false; else return true;
}
int main(){
	int cases;
	scanf("%d", &cases);
	for (int t = 0; t != cases; ++t){
		scanf("%d%d", &m, &n);
		getchar();
		memset(data, 0, sizeof(data));
		state.clear(); num.clear();
		for (int i = 0; i != m; ++i){
			for (int j = 0; j != n; ++j) data[i][j] = ((getchar() == '.') ? true : false);
			getchar();
		}
		Compress();
		dfs(0, 0, 0);
		memset(f, 0, sizeof(f));
		memset(g, 0, sizeof(g));
		//start state!!
	//	for (int i = 0; i != state.size(); ++i) cout << grid[i] << endl;
	//	for (int i = 0; i != state.size(); ++i) cout << state[i] << " " << num[i] << endl;
		for (int i = 1; i <= m; ++i){
			memset(g, 0, sizeof(g));
			for (int j = 0; j != state.size(); ++j){
				for (int k = 0; k != state.size(); ++k){
					if (!match1(state[j], state[k])) continue;
		//			cout << state[j] << " " << state[k] << endl;
					if (match2(state[k], i)) g[k] = max(g[k], f[j] + num[k]);
				}
			}
			memcpy(f, g, sizeof(f));
		}
		int ans = -1;
		for (int i = 0; i != (1 << n); ++i) ans = max(ans, f[i]);
		printf("Case #%d: %d\n", t + 1, ans);
	}
	return 0;
}
