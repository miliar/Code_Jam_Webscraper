#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <string>
#include <cstring>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <ctime>
#include <cmath>
#include <cassert>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define all(a) a.begin(), a.end()
#define fs first
#define sc second
#define mp make_pair
#define pb push_back

typedef pair<int,int> pii;
typedef long long int64;

const int inf = 2 * 1e9 + 2;
const double eps = 1e-6;

const int nmax = 200;

vector<int> g[nmax], l[nmax];
double wp[nmax], owp[nmax], oowp[nmax], res[nmax];
int a[nmax][nmax];

void solve(){


	int n;
	cin >> n;
	forn(i, n){
		g[i].clear();
		l[i].clear();
	}
	forn(i,n){
		forn(j,n){
			char ch;
			cin >> ch;
			a[i][j] = ch - '0';
			if (ch == '1'){
				g[i].pb(j);}
			if (ch == '0')
			{l[i].pb(j);}
		}
	}
	forn(i, n)
		res[i] = wp[i] = owp[i]= oowp[i] = 0;
	forn(i, n){
		wp[i] = (g[i].size()) * 1.0 / (g[i].size() + l[i].size());
		forn(j, g[i].size())
			l[i].pb(g[i][j]);
		cerr << g[i].size() << " " << l[i].size() << " " << wp[i] << endl;
	}
	forn(i, n){
		forn(j,l[i].size())
			owp[i] += (wp[l[i][j]] * l[l[i][j]].size() - a[l[i][j]][i]) / (l[l[i][j]].size()-1);
		if (l[i].size() > 0)
			owp[i] /= l[i].size() + .0;
	}
	forn(i, n){
		forn(j,l[i].size())
			oowp[i] += owp[l[i][j]];
		if (l[i].size() > 0)
			oowp[i] /= l[i].size() + .0;
		cerr << wp[i] << " " << owp[i] << " " << oowp[i] << endl;
	}
	forn(i, n)
		res[i] = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
	puts("");
	forn(i, n)
		printf("%0.9lf\n", res[i]);




}

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tst;
	scanf("%d", &tst);
	for (int i = 0; i < tst; i++){
		printf("Case #%d: ", i + 1);
		solve();
	}

	return 0;
}