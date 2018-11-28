#include <cstdio>
#include <cstring>
#include <utility>

using namespace std;

const int N = 109;

int n, m;
int h[N][N];
char ans[N][N];
char curr;
pair < int, int > memo[N][N];

bool val(int i, int j){
	return i >= 0 && j >= 0 && i < n && j < m;
}

int s;

pair < int, int > mm(int i, int j){
	pair < int, int > ans;
	int m = 1000000;
	
	for (int di = -1; di <= 1; di++){
		for (int dj = -1; dj <= 1; dj++) if (di * di + dj * dj == 1){
			int ii = i + di, jj = j + dj;

			if (val(ii, jj) && h[ii][jj] < m){
				m = h[ii][jj];
				ans = make_pair(ii, jj);
			}
		}
	}

	return ans;

}

void dfs(int i, int j){
	ans[i][j] = curr;

	//for (int k = 0; k < s; k++) printf("  ");
	//printf("dfs(%d, %d)\n", i, j);

	//s++;

	for (int di = -1; di <= 1; di++){
		for (int dj = -1; dj <= 1; dj++) if (di * di + dj * dj == 1){
			int ii = i + di, jj = j + dj;

			if (val(ii, jj) && h[ii][jj] > h[i][j] && !ans[ii][jj] && mm(ii, jj) == make_pair(i, j)){
				dfs(ii, jj);
			}
		}
	}

	//s--;
}

pair < int, int > gmin(int i, int j){
	if (memo[i][j] != make_pair(-1, -1)) return memo[i][j];

	pair < int, int > ans;
	int m = 1000000;

	for (int di = -1; di <= 1; di++){
		for (int dj = -1; dj <= 1; dj++) if (di * di + dj * dj == 1){
			int ii = i + di, jj = j + dj;

			if (val(ii, jj) && h[ii][jj] < m){
				//if (i == 0 && j == 0 && ii == 1 && jj == 0) printf("%d menor que %d\n", h[ii][jj], h[i][j]);
				m = h[ii][jj];
				ans = make_pair(ii, jj);
			}
		}
	}

	if (m < h[i][j]) return memo[i][j] = gmin(ans.first, ans.second);
	else return memo[i][j] = make_pair(i, j);
}

void find(){
	curr = 'a';

	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			memo[i][j] = make_pair(-1, -1);

	for (int i = 0; i < n; i++){
		for (int j = 0; j < m; j++){
			if (ans[i][j]) continue;

			pair < int, int > p = gmin(i, j);

			//printf("gmin(%d, %d) = (%d, %d)\n", i, j, p.first, p.second);

			dfs(p.first, p.second);
			curr++;
		}
	}
}

int main(){
	int tests;
	scanf("%d", &tests);

	for (int t = 0; t < tests; t++){
		scanf("%d %d", &n, &m);

		for (int i = 0; i < n; i++){
			for (int j = 0; j < m; j++){
				scanf("%d", &h[i][j]);
			}
		}

		memset(ans, 0, sizeof(ans));
		find();

		printf("Case #%d:\n", t + 1);

		for (int i = 0; i < n; i++){
			for (int j = 0; j < m; j++)
				printf("%c ", ans[i][j]);
			printf("\n");
		}
	}

	return 0;
}
