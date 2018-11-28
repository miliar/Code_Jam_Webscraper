#include <iostream>
#include <sstream>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>

#include <vector>
#include <string>
#include <queue>
#include <map>
#include <set>

#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

typedef vector<int> vi; 
typedef vector<vi> vvi;
typedef vector<string> vs;
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define rep(i, n) for(int i = 0; i < n; ++i) 
#define foreach(it, c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it) 

#define TRACE(x...) x
#define watch(x) TRACE(cout << #x" = " << x << endl)
#define watcharr(i, x) TRACE(cout << #x" = "); rep(i, sz(x)) cout << x[i] << " "; cout << endl

#define INF 0x3f3f3f3f

int dx[] = {-1, 0, 0, 1};
int dy[] = {0, -1, 1, 0};

int T, H, W;

char lt;
int m[110][110];
char ret[110][110];
bool vis[110][110];

char dfs(int i, int j, char c) {
	if(vis[i][j]) return ret[i][j];
	vis[i][j] = true;
	int id = -1, v = m[i][j];
	rep(k, 4) {
		int ni = i + dx[k], nj = j + dy[k];
		if(ni < 0 || ni >= H || nj < 0 || nj >= W) continue;
		if(m[ni][nj] < v) {
			v = m[ni][nj];
			id = k;
		}
	}
	if(id == -1) ret[i][j] = c, lt++;
	else ret[i][j] = dfs(i + dx[id], j + dy[id], c);
	return ret[i][j];
}

int main() {
	
	scanf("%d", &T);
	
	rep(_case, T) 
	{
		scanf("%d %d", &H, &W);
		rep(i, H) rep(j, W) scanf("%d", &m[i][j]), vis[i][j] = false;
		
		lt = 'a';
		
		rep(i, H) rep(j, W) if(!vis[i][j]) dfs(i, j, lt);
		
		printf("Case #%d:\n", _case + 1);
		rep(i, H) {
			rep(j, W) printf("%c ", ret[i][j]);
			printf("\n");
		}
	}
	
	return 0;
	
}

