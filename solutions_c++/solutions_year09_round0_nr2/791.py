#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(i=0;i<n;i++)
#define F1(i,n) for(i=1;i<=n;i++)
const int inf = 1000000009;
const double eps = 1e-8;
const double pi = acos(-1.0);

int i, j, k, m, n, l, o;
int dx[]={-1, 0, 0, 1};
int dy[]={0, -1, 1, 0};
vector<pii> adj[100][100];
int h[100][100], v[100][100];

int ok(int x, int y) { return 0 <= x && x < m && 0 <= y && y < n; }

void dfs(int x, int y) {
	v[x][y] = k;
	int sz = SZ(adj[x][y]), j;
	F0(j,sz) {
		int xx = adj[x][y][j].first;
		int yy = adj[x][y][j].second;
		if (v[xx][yy] == -1) dfs(xx, yy);
	}
}

int main() {
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int tt, tn;
	cin >> tn;
	F1(tt,tn) {
		cin >> m >> n;
		F0(i,m) F0(j,n) { cin >> h[i][j]; v[i][j] = -1; adj[i][j].clear(); }
		F0(i,m) F0(j,n) {
			int lowest = h[i][j], xx = -1, yy = -1;
			F0(k,4) {
				int x = i + dx[k];
				int y = j + dy[k];
				if (ok(x, y) && h[x][y] < lowest) {
					lowest = h[x][y];
					xx = x;
					yy = y;
				}
			}
			if (xx != -1) {
				adj[xx][yy].push_back(pii(i, j));
				adj[i][j].push_back(pii(xx, yy));
			}
		}
		k = 0;
		F0(i,m) F0(j,n) if (v[i][j] == -1) {
			dfs(i, j);
			k++;
		}
		printf("Case #%d:\n", tt);
		F0(i,m) {
			F0(j,n) cout << (char)(v[i][j] + 'a') << " ";
			cout << endl;
		}
	}

	return 0;
}
