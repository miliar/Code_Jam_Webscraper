/**
 * Qualification Round 2009
 * g++ 3.4.5
 */
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> II;
typedef vector<II> VII;

template<typename T> inline int sz(const T& x) { return (int)x.size(); }

int dr[] = {-1,0,0,1};
int dc[] = {0,-1,1,0};

int alt[128][128];
VII adj[128][128];
int vis[128][128];


void dfs(int i, int j, int c) {
	if( vis[i][j] )
		return;
	vis[i][j] = c;

	VII& a = adj[i][j];
	for(int k = 0; k < sz(a); ++k)
		dfs( a[k].first, a[k].second, c );
}

void solve() {
	int N, M;
	cin >> N >> M;

	memset(alt, 1, sizeof alt);

	for(int i = 1; i <= N; ++i)
		for(int j = 1; j <= M; ++j) {
			cin >> alt[i][j];
			adj[i][j].clear();
		}

	VII sinks;

	for(int i = 1; i <= N; ++i)
		for(int j = 1; j <= M; ++j) {

			int bi = i, bj = j;

			for(int d = 0; d < 4; ++d) {
				if( alt[i+dr[d]][j+dc[d]] < alt[bi][bj] ) {
					bi = i+dr[d];
					bj = j+dc[d];
				}
			}

			if(bi == i && bj == j)
				sinks.push_back( II(i,j) );
			else
				adj[bi][bj].push_back( II(i,j) );
		}


	memset(vis, 0, sizeof vis);

	for(int i = 0; i < sz(sinks); ++i) {
		II& sink = sinks[i];
		dfs( sink.first, sink.second, i+1 );
	}

	char comp[32];
	memset(comp, 0, sizeof comp);
	char letter = 'a'-1;

	for(int i = 1; i <= N; ++i) {
		for(int j = 1; j <= M; ++j) {
			int c = vis[i][j];

			if(!comp[c])
				comp[c] = ++letter;

			cout << comp[c];
			if(j<M) cout << ' ';
		}
		cout << '\n';
	}
}

int main() {
	cin.sync_with_stdio(false);
	cout.sync_with_stdio(false);

	int T;
	cin >> T;

	for(int t = 1; t <= T; ++t) {
		cout << "Case #" << t << ":\n";
		solve();
	}

	return 0;
}
