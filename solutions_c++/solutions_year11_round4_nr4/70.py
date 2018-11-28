#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <ctime>
#include <cstring>
#include <cassert>
#include <sstream>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) int(a.size() - 1)
#define all(a) a.begin(), a.end()
#define seta(a,x) memset (a, x, sizeof (a))
#define I (int)

typedef long long int64;
typedef pair <int, int> pii;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const int64 inf64 = ((int64)1 << 62) - 1;
const long double pi = 3.1415926535897932384626433832795;
const string task = "";

template <class T> T sqr (T x) {return x * x;}

const int nmax = 410;

vector<int> lev[nmax], g[nmax];
int dep[nmax], us[nmax];
int n,m;
vector<int> e;
int t[nmax][nmax];

void bfs(){
	lev[0].pb(0);
	dep[0] = 0;
	int now = 0;
	memset(us, 0, sizeof us);
	us[0] = 1;
	e.clear();
	e.pb(0);
	while (lev[now].size() > 0){
		for (int i = 0; i < lev[now].size(); i++)
			for (int j = 0; j < g[lev[now][i]].size(); j++)
				if (!us[g[lev[now][i]][j]]){
					e.pb(g[lev[now][i]][j]);
				
					us[g[lev[now][i]][j]] = 1;
					lev[now+1].pb(g[lev[now][i]][j]);
					dep[g[lev[now][i]][j]] = now + 1;
				}
		now ++;
	}
}

int s[nmax][nmax][nmax];

int solve(){
	cin >> n >> m;
	forn(i, nmax){
		lev[i].clear();
		g[i].clear();
	}
	forn(i, m){
		string s;
		cin >> s;
		int v,u;
		sscanf(s.data(),"%d,%d", &v,&u);
		g[v].pb(u);
		g[u].pb(v);
	}
	bfs();
	memset(us, 0, sizeof us);

	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++){
				forn(w, g[i].size())
					us[g[i][w]] = 1;
				forn(w, g[j].size())
					us[g[j][w]] = 1;
				us[i] = us[j] = 1;
			for (int k = 0; k < n; k ++){
				s[i][j][k] = 0;
				forn(w, g[k].size())
					if (!us[g[k][w]])
						s[i][j][k] ++;
			}
				forn(w, g[i].size())
					us[g[i][w]] = 0;
				forn(w, g[j].size())
					us[g[j][w]] = 0;
				us[i] = us[j] = 0;
		}
	memset(t, 255, sizeof t);
	t[0][0] = g[0].size()+1;
	int res = -1;
	forn(i, e.size())
		forn(j, e.size())
			if (t[e[i]][e[j]] >= 0){
//				if (e[j] == 1)
//					res = max(res, t[e[i]][e[j]]);
				for (int q = 0; q < g[e[j]].size(); q++){
					int k = g[e[j]][q];
					if (dep[k] == dep[e[j]] + 1){
						if (k == 1){
							res = max(res, t[e[i]][e[j]]);
							//cerr << res<< " "<< e[i] << " " << e[j] << endl;
						}
						t[e[j]][k] = max(t[e[j]][k], t[e[i]][e[j]] + s[e[i]][e[j]][k]);
					}
				}
			} 

	cout << dep[1] - 1 <<" " << res-dep[1] << endl;
	return 0;
	

}	        

int main ()
{
	int tst;
	cin >> tst;
	forn(i, tst){
		printf("Case #%d: ", i + 1);
		solve();
	}

	
	return 0;
}
