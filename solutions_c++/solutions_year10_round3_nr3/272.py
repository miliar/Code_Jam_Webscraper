#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <cassert>
#include <ctime>
#include <map>
#include <set>
#define forn(i, n) for(int i = 0; i < int(n); i++)
#define X first
#define Y second
#define sz(s) (int)(s).size()
#define mp make_pair

using namespace std;

typedef long long li;
typedef pair<int, int> pt;
int n, m, t;
int a[600][600];
int d[2][600][600];
int solve(int x, int y, int c){
	if(c == -1)
		return -2;
	if(x >= m || y >= n)
		return -2;
	if(c != a[x][y])
		return -2;
	if(d[c][x][y] == -1){
		d[c][x][y] = 0;
		if(solve(x + 1, y + 1, c) != -2 && solve(x + 1, y, !c) != -2 && solve(x, y + 1, !c) != -2){
			d[c][x][y] = min(d[c][x + 1][y + 1], min(d[!c][x][y + 1], d[!c][x + 1][y]));	
		}
		d[c][x][y]++;
	}
	return d[c][x][y];
}

int find(int sz){
	int res = 0;
	forn(i, m)
		forn(j, n)
			if(a[i][j] > -1 && d[a[i][j]][i][j] == sz){
				res++;
				memset(d, -1, sizeof(d));
				for(int i1 = i; i1 < i + sz; i1++)
					for(int j1 = j; j1 < j + sz; j1++){
						
						a[i1][j1] = -1;
					}
				forn(i1, m)
					forn(j1, n)
						solve(i1, j1, a[i1][j1]);
						
			}
	return res;
}
int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	
	cin >> t;
	forn(q, t){
		cin >> m >> n;
		forn(i, m){
			forn(j, n/4){
				char c;
				cin >> c;
				int k = 0;
				if(isdigit(c))
					k = c - '0';
				else
					k = c - 'A' + 10;
				for(int i1 = j * 4; i1 <(j + 1) * 4; i1++)
					a[i][i1] = (bool)(k & (1 << (3 - (i1 - j * 4))));
			}
		}
		memset(d, -1, sizeof(d));
		
		forn(i, m)
			forn(j, n){
				solve(i, j, a[i][j]);
		}
		vector<pt> v;
		for(int sz = n; sz >= 1; sz--){
			int x = find(sz);
			if(x > 0)
				v.push_back(pt(sz, x));
		}
		cout << "Case #" << q + 1 << ": " << sz(v) << endl;
		forn(i, sz(v))
			cout << v[i].X << " " << v[i].Y << endl;
	}
	return 0;
}