#pragma comment(linker, "/STACK:60000000")
#define _CRT_SECURE_NO_WARNINGS

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
#include <iomanip>
#include <complex>
#include <queue>
#include <functional>

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

int n, m;
multiset <int> vin[10000];
vector <int> vout[10000];
bool u[10000];

void dfs (int v) {
	if (u[v])
		return;
	u[v] = 1;
	forn (i, vout[v].size()) {
		int w = vout[v][i];
		for (multiset<int> :: iterator it = vin[w].begin(); it != vin[w].end(); it ++)
			dfs (*it);
	}
}

void calccalc () {
	cin >> n >> m;
	forn (i, n*m) {
		vin[i].clear ();
		vout[i].clear ();
	}
	forn (i, n)
		forn (j, m) {
			char c;
			scanf (" %c", &c);
			int dx, dy;
			dx = dy = 0;
			if (c == '|') {
				dx = 1; 
				dy = 0;
			}
			if (c == '-') {
				dx = 0; 
				dy = 1;
			}

			if (c == '\\') {
				dx = 1; 
				dy = 1;
			}
			if (c == '/') {
				dx = -1; 
				dy = 1;
			}
			for (int l = -1; l <= 1; l += 2) {
				int vx = i + dx * l;
				int vy = j + dy * l;
				vx = (vx + n) % n;
				vy = (vy + m) % m;
				vout[i*m+j].pb ((vx*m+vy));
				vin[vx*m+vy].insert ((i*m+j));
			}
		}
	vector <int> Q;
	forn (i, n*m) {
		if (vin[i].size() == 0) {
			cout << 0 << endl;
			return;
		} else
		if (vin[i].size() == 1) {
			Q.pb (i);
        	}		
	}
    int h = 0;
    while (h < I Q.size()) {
    	int v = Q[h];
    	h ++;
    	int w = (*vin[v].begin());
		forn (i, vout[w].size()) {
    		vin[vout[w][i]].erase (vin[vout[w][i]].find (w));
    		if (vin[vout[w][i]].size() == 0 && vout[w][i] != v) {
    			cout << 0 << endl;
    			return;
    		}
    		if (vin[vout[w][i]].size() == 1)
    			Q.pb (vout[w][i]);
    	}
		vout[w] = vout[v];
		if (v == w)
			continue;
		forn (i, vout[w].size()) {
			if (vin[vout[w][i]].count(v) == 0) {
				cout << "WA" << endl;
			}
			vin[vout[w][i]].erase (vin[vout[w][i]].find(v));
			vin[vout[w][i]].insert (w);
		}
    }
    seta (u, 0);
    forn (i, n*m)
    	if (vin[i].size() == 0)
    		u[i] = 1;
	int res = 0;
	forn (i, n*m)
		if (!u[i]) {
			dfs (i);
			res ++;
		}
	int ans = 1;
	forn (i, res)
		ans = (ans * 2) % 1000003;
	cout << ans << endl;
}

int main ()
{
//	freopen ("input.txt", "r", stdin);
//	freopen ("output.txt", "w", stdout);
	int tt;
	cin >> tt;
	forn (ii, tt) {
		printf ("Case #%d: ", ii+1);
		calccalc ();
	}
	
	return 0;
}
