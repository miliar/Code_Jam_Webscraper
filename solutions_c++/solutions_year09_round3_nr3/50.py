#include <iostream>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <string>
#include <vector>

#define forn(i, n) for(int i = 0; i < int(n); i++)
#define for1(i, n) for(int i = 1; i < int(n); i++)
#define mp(a, b) make_pair(a, b);
#define X first
#define Y second
#define pb(a) push_back(a)
#define sz(a) a.size()

using namespace std;

typedef long long li;
typedef pair<int, int> pt;

int p, q;
li d[200][200];
int a[200];
int solve(int l, int r){
	if (r - l == 1)
		return d[l][r] = 0; 
	if (d[l][r] == -1){
		int res = -1;
		for(int i = l + 1; i <= r - 1; i++){
			int k = solve(l, i) + solve(i, r);
			if (solve(l, i) + solve(i, r) < res || res == -1)
				res = solve(l, i) + solve(i, r);
		}
		
		d[l][r] = res + (a[r] - a[l] - 2);
	}
	return d[l][r];
}
int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t;
	cin >> t;
	forn(x, t){
		cin >> p >> q;
		memset(d, -1, sizeof(d));
		forn(i, q){
			cin >> a[i + 1];
		}
		a[0] = 0;
		a[q + 1] = p + 1;
		q++;
		sort(a, a+ q);
		cout << "Case #" << x + 1 << ": " << solve(0, q)<< endl;
	}
	return 0;
}