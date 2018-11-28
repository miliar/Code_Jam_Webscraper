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

template <class T> T sqr (T x) {return x * x;}

char ps[] = {'-', '|', '/' , '\\'};
const int px[] = {0, 1, -1, 1};
const int py[] = {1, 0, 1, 1};

const int nmax = 150;
const int64 mod = 1000003;

int n,m;
int a[nmax][nmax];
int num1[nmax][nmax], num2[nmax][nmax];
vector<int> g[nmax*nmax*2];
bool used[nmax*nmax*2];
int q = 0;

void go(int x){
	used[x] = 1;
	q ++;
	forn(i, g[x].size())
		if (!used[g[x][i]])
			go(g[x][i]);
}

int solve(){
	cin >> n >> m;
	forn(i, n * m * 2)
		g[i].clear();
	memset(used,0,sizeof used);
	forn(i, n)
		forn(j, m){
			char ch;
			cin >> ch;
			forn(k, 4)
				if (ps[k] == ch)
					a[i][j] = k;
		}
	forn(i, n)
		forn(j, m){
			num1[i][j] = i * m + j;
			num2[i][j] = n*m + num1[i][j];
		}
	forn(i, n)
		forn(j, m){
			{
				int nx = (i + px[a[i][j]] + n) % n;
				int ny = (j + py[a[i][j]] + m) % m;
				g[num1[i][j]].pb(num2[nx][ny]);
				g[num2[nx][ny]].pb(num1[i][j]);
			}
			{
				int nx = (i - px[a[i][j]] + n) % n;
				int ny = (j - py[a[i][j]] + m) % m;
				g[num1[i][j]].pb(num2[nx][ny]);
				g[num2[nx][ny]].pb(num1[i][j]);
			}
		}
//	cerr << endl;
//	forn(i, n*m*2)
//		cerr << g[i].size() << " ";
//	cerr << endl;
	int64 res = 1;
	forn(i, n*m*2)
		if (g[i].size() == 0)
			res = 0;
	memset(used, 0, sizeof used);
	forn(i, n * m * 2)
		if (!used[i]){
			q = 0;
			go(i);
			if (q % 2 != 0)
				res = 0;
			res = (res * 2ll) % mod;
		}
	cout << res << endl;
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
