#include <algorithm>
#include <numeric>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <complex>
#include <cassert>
#include <bitset>
using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define si(c) ((int)(c).size())
#define forsn(i,s,n) for(int i = (int)(s); i<((int)n); i++)
#define dforsn(i,s,n) for(int i = (int)(n)-1; i>=((int)s); i--)
#define decl(v, c) typeof(c) v = c
#define forall(i, c) for(decl(i, c.begin()); i!=c.end(); ++i)
#define all(c) (c).begin(), (c).end()
#define D(a) cout << #a << "=" << a << endl;
#define pb push_back
#define mp make_pair

typedef long long int tint;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int,int> pii;

map<string, map<string, int> > ids;
int id(string cat, string s) {
	map<string,int>& m = ids[cat];
	if (m.count(s) == 0) m[s] = si(m)-1;
	return m[s];
}

int cnt[3][3];

void init() {
	ids.clear();
	memset(cnt,0,sizeof cnt);
}



int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int _t; cin >> _t;
	forsn(cas,1,_t+1) {
		init();
		tint n,a,b,c,d,m,x,y; cin >> n >> a >> b >> c >> d >> x >> y >> m;
		forn(_,n) {
			cnt[x%3][y%3]++;
			x = (a * x + b) % m;
			y = (c * y + d) % m;
		}

		//forn(i,3) { forn(j,3) cout << cnt[i][j]<< ' '; cout << endl; }

		tint sum6 = 0, sum3 = 0, sum1 = 0;
		forn(i1,3) forn(j1,3)
		forn(i2,3) forn(j2,3)
		forn(i3,3) forn(j3,3) {
			if ((i1 + i2 + i3) % 3) continue;
			if ((j1 + j2 + j3) % 3) continue;
			vector<pii> p;
			p.pb(mp(i1,j1));
			p.pb(mp(i2,j2));
			p.pb(mp(i3,j3));
			sort(all(p));
			if (p[0] != p[1] && p[1] != p[2])
				sum6 += cnt[i1][j1] * cnt[i2][j2] * cnt[i3][j3];
			else if (p[0] == p[1] && p[1] == p[2]) {
				tint N = cnt[i1][j1];
				sum1 += (N * (N-1) * (N-2)) / 6;
			}
			else {
				if (p[1] == p[2]) swap(p[0],p[2]);
				tint N = cnt[p[0].first][p[0].second], M = cnt[p[2].first][p[2].second];
				sum3 += ((N * (N-1)) / 2) * M;
			}
		}


		cout << "Case #" << cas << ": " << sum1 + sum3 / 3 + sum6 / 6 << endl;
	}
	return 0;
}

