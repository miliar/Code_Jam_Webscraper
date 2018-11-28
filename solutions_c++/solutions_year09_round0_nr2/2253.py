#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <sstream>
#include <cmath>
#include <queue>

#define FOR(i, n) for(int i=0; i<(n); i++)
#define DFOR(i, n) for(int i=(n)-1; i>=0; i--)
#define CLR(a, b) memset(a, sizeof(a), b)
#define MIN(a, b) ((a)<(b) ? (a):(b))
#define MAX(a, b) ((a)>(b) ? (a):(b))
#define SQR(x) ((x)*(x))
#define ABS(x) ((x)>0 ? (x) : -(x))
#define LL long long
#define VI vector<int>
#define PII pair<int, int>
#define FI first
#define SE second
#define PB push_back
#define MP make_pair
#define ALL(x) x.begin(), x.end()

using namespace std;

void init(){
    freopen(".in", "r", stdin);
    freopen(".out", "w", stdout);
}

#define maxn 110

int dx[4] = {-1, 0, 0, 1};
int dy[4] = {0, -1, 1, 0};

int w, h;
int a[maxn][maxn];
char ans[maxn][maxn];
bool used[maxn][maxn];
bool Used[26];
char what[26];

bool inboard(int x, int y){
	return (x>=0&&x<w&&y>=0&&y<h);
}

void dfs(int x, int y){
	used[x][y] = true;
	int mini = (int)1e9;
	FOR(q, 4) if(inboard(x+dx[q], y+dy[q])) mini = min(mini, a[x+dx[q]][y+dy[q]]);
	FOR(q, 4) if(inboard(x+dx[q], y+dy[q]) && a[x+dx[q]][y+dy[q]]==mini){
		if(!used[x+dx[q]][y+dy[q]]) dfs(x+dx[q], y+dy[q]);
		ans[x][y] = ans[x+dx[q]][y+dy[q]];
		return;
	}
}

void solvecase(){
	cin >> w >> h;
	FOR(i, w) FOR(j, h) cin >> a[i][j];
	FOR(i, w) FOR(j, h) used[i][j] = false;
	char cur = 'a';
	FOR(x, w) FOR(y, h) {
		bool f = true;
		FOR(q, 4) if(inboard(x+dx[q], y+dy[q]) && a[x+dx[q]][y+dy[q]]<a[x][y]) f = false;
		if(f){ ans[x][y] = cur++; used[x][y] = true;}
	}
	FOR(x, w) FOR(y, h) if(!used[x][y]) dfs(x, y);

	cur = 'a';
	FOR(i, 26) Used[i] = false;
	FOR(x, w) FOR(y, h)if(!Used[ans[x][y]-'a']){
		Used[ans[x][y]-'a'] = true;
		what[ans[x][y]-'a'] = cur++;
	}	

	FOR(x, w){
		FOR(y, h) cout << what[ans[x][y]-'a'] << " ";
		cout << endl;
	}
}

void solve(){
	int t;
	cin >> t;
	FOR(qq, t){
		printf("Case #%d:\n", qq+1);
		solvecase();
	}
}

int main(){
    init();
    solve();
    return 0;
}