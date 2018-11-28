#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <sstream>

using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define si(c) ((int)(c).size())
#define forsn(i,s,n) for(int i = (int)(s); i<((int)n); i++)
#define all(c) (c).begin(), (c).end()
#define pb push_back
#define mp make_pair

typedef long long int tint;
typedef vector<int> vi;
typedef vector<bool> vb;
typedef vector<string> vs;
typedef pair<int,int> ii;
typedef vector<ii> vii;

const int maxn = 60;
const int OO = 1000000000;
int n;
int t[maxn][maxn];

bool isin(int u, int v, int x0, int y0){ return (u>=x0 && u<n+x0 && v>=y0 && v<n+y0); }

int check(int s, int x0, int y0){
	if(x0+n>s || y0+n>s) return OO;

//	cout << s <<  " " << x0 << " " << y0 << endl;

	bool pos = true;
	forn(i, n){
		forn(j, n){
			int u0 = x0+i, v0=y0+j;
//			cout << "a " << u0 << " " << v0 << endl;
			if(isin(v0, u0, x0, y0) && t[v0-x0][u0-y0] != t[i][j]){ pos = false; break; }

			u0 = x0+i; v0 = y0+j;
			int u = (s-1-v0), v = (s-1-u0);
//			cout << "b " << u0 << " " << v0 << ", " << u << " " << v << endl;
			if(isin(u, v, x0, y0) && t[i][j] != t[u-x0][v-y0]){ pos = false; break; }
		}
		if(!pos) break;
	}
//	if(pos) cout << s*s - n*n;
//	cout << endl;

	if(!pos) return OO;
	else return s*s - n*n;
}

int main(){
	freopen("diamondl.in","r",stdin);
//	freopen("diamondl.out","w",stdout);

	int NC; cin >> NC;
	forn(nc, NC){
		cin >> n;
		string s; getline(cin, s);
		forsn(i, 1, 2*n){
			string s;
			getline(cin, s);
			string s2;
			forn(j, si(s)) if(s[j] != ' ') s2 += s[j];

			int u=i-1, v = 0;
			if(u>=n){ v+=(u-n+1); u=n-1; }
//			cout << "fila " << i << " = " << u << ", " << v << endl;
			forn(j, si(s2)) { t[u][v] = int(s2[j]-'0'); u--; v++; }
		}

//		forn(i, n){ forn(j, n) cout << t[i][j] << " "; cout << endl; }
//		cout << endl;

		int res = OO;
		forsn(s, n, 4*n) forn(i, s) forn(j, s) res = min(check(s, i, j), res);

		cout << "Case #" << nc+1 << ": " << res << endl;
	}
	return 0;
}
