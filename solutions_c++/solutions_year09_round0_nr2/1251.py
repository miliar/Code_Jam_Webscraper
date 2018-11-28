#include <iostream>
#include <cassert>
#include <cstring>
#include <vector>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

const int inf = (int)1E+9;

typedef long long int64;
typedef pair<int,int> pii;

#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define all(a) a.begin(), a.end()
#define last(a) (int)a.size() - 1
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define norm(a) sort(all(a)); a.erase(unique(all(a)), a.end());
#define num(a, v) (int)(lower_bound(all(a), v) - a.begin())

const int nmax = 150;

const int px[4] = {-1,0,0,1};
const int py[4] = {0,-1,1,0};

int a[nmax][nmax];
int res[nmax][nmax];
int n,m;




bool check(int x, int y){
	if (min(x,y) < 0) return 0;
	if (x >= n || y >= m) return 0;
	return 1;
}

int go(int x, int y, int &now){
	if (res[x][y] != -1) return res[x][y];
	int nx, ny;
	nx = x; ny = y;
	forn(i,4)
		if (check(x + px[i], y+py[i]) && a[x+px[i]][y+py[i]] < a[nx][ny]){
			nx = x + px[i];
			ny = y + py[i];
		}
	if (nx == x && ny == y){
		now++;
		return res[x][y] = now;
	}
	return res[x][y] = go(nx,ny,now);
}

void solve(){
	cin >> n >> m;
	forn(i,n)
		forn(j,m)
			cin >> a[i][j];
	forn(i,n)
		forn(j,m)
			res[i][j] = -1;
	int now = -1;
	forn(i,n)
		forn(j,m)
			if (res[i][j] == -1)
				go(i,j,now);
	forn(i,n){
		forn(j,m){
			printf("%c ", res[i][j] + 'a');
		}
		puts("");
	}						
}

int main(){
	freopen ("b.in", "rt", stdin);
	freopen ("b.out", "wt", stdout);

	int tst;
	cin >> tst;
	forn(i,tst){
		printf("Case #%d:\n",i+1);
		solve();
		}

	return 0;
}
