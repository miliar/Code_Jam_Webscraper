#include <string>      
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <iostream>

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

const int nmax = 11;

int n;
int cc[nmax][1 << nmax];
long long t[nmax][1 << nmax][nmax];
int m[1 << nmax];


long long calc(int x, int y, int c){
	if (x < 0){
		if (c + m[y] >= n) return 0;
		return 1e11;
	}
	if (t[x][y][c] != -1) return t[x][y][c];
	t[x][y][c] = min(calc(x-1,y*2,c+1) + calc(x-1,y*2+1,c+1) + cc[x][y], calc(x-1,y*2,c) + calc(x-1,y*2+1,c));
	return t[x][y][c];
}


void solve(){
	cin >> n;
	forn(i,1 << n)
		cin >> m[i];
	forn(i,n)
		forn(j, 1 << (n-i-1))
			cin >> cc[i][j];
	memset(t, 255, sizeof t);
	long long res = calc(n-1, 0, 0);
	cout << res << endl;
}

int main(){
	freopen ("a.in", "rt", stdin);
	freopen ("a.out", "wt", stdout);

	int tst;
	cin >> tst;
	forn(i,tst){
		printf("Case #%d: ", i+1);
		solve();
	}

        return 0;
}
