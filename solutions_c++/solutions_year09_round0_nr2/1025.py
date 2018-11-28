#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <cstring>
#include <set>
#include <vector>
#include <map>
#include <queue>
#include <cmath>
#include <sstream>
#include <numeric>
#include <bitset>

#define mp make_pair
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define sz(x) ((int)((x).size()))
#define fi first
#define se second
#define re return
#define For(i,a,b) for(int i = a; i < b; i++)
#define rep(i,n) for(int i = 0; i < n; i++)
#define sqr(x) ((x) * (x))

using namespace std;

template<class T> T abs(T x) {re x > 0 ? x : -x;}

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<string> vs;

int n;
int m;

int matr[100][100];

vii v;

int ans[100][100];
ii last[100][100];

int dx[4] = {-1, 0, 0, 1};
int dy[4] = {0, -1, 1, 0};

bool l1(ii a, ii b) {
	re matr[a.fi][a.se] < matr[b.fi][b.se];
}	

int good(int x, int y) {
	re x >= 0 && x < n && y >= 0 && y < m;
}	

void parse(int x, int y) {
	int ind = -1, low = matr[x][y];
	rep(i, 4) {
		int nx = x + dx[i];
		int ny = y + dy[i];

		if (good(nx, ny))
		if (matr[nx][ny] < low) {
			ind = i;
			low = matr[nx][ny];
		}
	}       

	if (ind != -1) {
		int nx = x + dx[ind];
		int ny = y + dy[ind];
		last[x][y] = last[nx][ny];			
	}
	else
		last[x][y] = mp(x, y);
}

int main() {
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);

	int t;
	cin >> t;
	rep(u, t) {
		v.clear();
		cin >> n >> m;
		rep(i, n)
		rep(j, m) {
			cin >> matr[i][j];		
			v.pb(mp(i, j));
		}	
		sort(all(v), l1);
		rep(i, n * m)
			parse(v[i].fi, v[i].se);
		memset(ans, 0, sizeof(ans));
		char c = 'a';
		cout << "Case #" << u + 1 << ":" << endl;
		rep(i, n) {
			rep(j, m) {
				if (ans[last[i][j].fi][last[i][j].se] == 0)
					ans[last[i][j].fi][last[i][j].se] = c++;
				cout << (char)ans[last[i][j].fi][last[i][j].se] << ' ';	
			}
			cout << endl;
		}	
	}

	return 0;	
}