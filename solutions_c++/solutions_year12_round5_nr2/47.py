#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cctype>
#include <cmath>
#include <queue>
#include <stack>
#include <set>
#include <utility>
#include <vector>
#include <bitset>
#include <deque>
#include <iomanip>
#include <complex>
#include <fstream>
#include <sstream>
#include <map>
//#include <climits>
//#include <list>

using namespace std;

#if ( _WIN32 || __WIN32__ )
    #define LLD "%I64d"
#else
    #define LLD "%lld"
#endif

#define show(x) cerr<<((#x))<<" = "<<((x))<<" "<<endl
#define bit(a,b) (((a)>>(b))&1)
#define gcd __gcd
#define endl '\n'
#define bcnt(x) ((__builtin_popcount(x)))
#define sz(x) ((int((x).size())))
#define sqr(x) ((((x))*((x))))
#define fx(x) fixed<<setprecision(x)
#define FOR(i, a, n) for (register int i = (a); i < (int)(n); ++i)
#define pb push_back

template<class T> inline void smn(T &a,const T &b){if(b<a) a=b;}
template<class T> inline void smx(T &a,const T &b){if(b>a) a=b;}
//template<class T> inline T rev(const T & a){T _=a; reverse(_.begin(),_.end()); return _;}

typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;

const double eps=1e-9;
const ld leps=1e-14;

const int MAXN = 100000;

bool mark[MAXN], isborder[MAXN];
int par[MAXN];
map<pii, int> vert;

int find(int x) {
	if (par[x] == x) return x;
	return par[x] = find(par[x]);
}

void un(int a, int b) {
	par[find(a)] = par[find(b)];
}

int S, M;

void add(int x, int y) {
	pii nei[6] = {pii(x+1, y), pii(x, y+1), pii(x-1, y), pii(x, y-1), pii(x+1, y+1), pii(x-1, y-1)};
	mark[vert[pii(x, y)]] = true;
	FOR(i, 0, 6) if (vert.count(nei[i]) && mark[vert[nei[i]]]) un(vert[nei[i]], vert[pii(x, y)]);
}

bool bridge() {
	pii cor[6] = {pii(1, 1), pii(S, 1), pii(1, S), pii(2*S-1, S), pii(S, 2*S-1), pii(2*S-1, 2*S-1)};
	FOR(i, 0, 6) FOR(j, i+1, 6) if (find(vert[cor[i]]) == find(vert[cor[j]])) return true;
	return false;
}

vector<pii> border, side[6];
int dsu[MAXN];

int dsu_find(int x) {
	if (dsu[x] == x) return x;
	return dsu[x] = dsu_find(dsu[x]);
}

void dsu_un(int a, int b) {
	if (dsu_find(a) == dsu_find(b)) return;
	dsu[dsu_find(a)] = dsu_find(b);
}

bool ring() {
	FOR(i, 0, MAXN) dsu[i] = i;
	map<pii, int>::iterator it;
	for (it = vert.begin(); it != vert.end(); it++) {
		if (mark[it->second]) continue;
		int x = it->first.first, y = it->first.second;
		pii nei[6] = {pii(x+1, y), pii(x, y+1), pii(x-1, y), pii(x, y-1), pii(x+1, y+1), pii(x-1, y-1)};
		FOR(i, 0, 6) {
			if (vert.count(nei[i]) == 0) continue;
			if (mark[vert[nei[i]]]) continue;
			dsu_un(vert[nei[i]], it->second);
		}
	}
	set<int> st;
	FOR(i, 0, sz(border)) st.insert(dsu_find(vert[border[i]]));
	for (it = vert.begin(); it != vert.end(); it++)
		if (!mark[it->second] && !isborder[it->second] && st.find(dsu_find(it->second)) == st.end()) return true;
	return false;
}

bool ffork() {
	map<int, int> mp;
	FOR(i, 0, 6) FOR(j, 0, sz(side[i])) mp[find(vert[side[i][j]])] |= 1<<i;
	map<int, int>::iterator it;
	for (it = mp.begin(); it != mp.end(); ++it) if (__builtin_popcount(it->second) >= 3) return true;
	return false;
}

void init() {
	memset(isborder, 0, sizeof isborder);
	border.clear();
	FOR(i, 0, 6) side[i].clear();
	FOR(i, 2, S) {
		side[0].pb(pii(i, 1));
		side[1].pb(pii(1, i));
		side[2].pb(pii(S+i-1, i));
		side[3].pb(pii(i, S+i-1));
		side[4].pb(pii(2*S-1, S+i-1));
		side[5].pb(pii(S+i-1, 2*S-1));
	}
	FOR(i, 0, 6) FOR(j, 0, sz(side[i])) border.pb(side[i][j]);
	pii cor[6] = {pii(1, 1), pii(S, 1), pii(1, S), pii(2*S-1, S), pii(S, 2*S-1), pii(2*S-1, 2*S-1)};
	FOR(i, 0, 6) border.pb(cor[i]);
	FOR(i, 0, sz(border)) isborder[vert[border[i]]] = true;
}

int main()
{
	ios_base::sync_with_stdio(false);
	int t, tc = 1;
	cin >> t;
	while (t--) {
		cin >> S >> M;
		vector<pii> Q(M);
		bool done = false;
		memset(mark, 0, sizeof mark);
		FOR(i, 0, MAXN) par[i] = i;
		vert.clear();
		int cnt = 0;
		FOR(sum, 2, 4*S-1) {
			//cout << "sum " << sum << endl;
			int lim = min(min(sum-1, 4*S-1-sum), S);
			int lo = sum/2, hi = sum-sum/2;
			int tmp = 0;
			if (sum%2 == 0) {
				//cout << lo << " " << hi << endl;
				vert[pii(lo, hi)] = cnt++, lo--, hi++, tmp++;
			}
			while (tmp+2 <= lim && lo >= 1) {
				vert[pii(lo, hi)] = cnt++;
				vert[pii(hi, lo)] = cnt++;
				//cout << lo << " " << hi << endl;
				//cout << hi << " " << lo << endl;
				tmp += 2;
				lo--; hi++;
			}
		}
		//cout << "cnt " << cnt << endl;
		FOR(i, 0, M) cin >> Q[i].first >> Q[i].second;
		init();
		//cout << "sz " << sz(border) << endl;
		//FOR(i, 0, sz(border)) cout << border[i].first << "," << border[i].second << endl;
		FOR(cur, 0, M) {
			add(Q[cur].first, Q[cur].second);
			map<pii, int>::iterator it;
			//for (it = vert.begin(); it != vert.end(); it++)
			//	cout << it->first.first << "," << it->first.second << " " << find(it->second) << " " << mark[it->second] << endl;
			vector<string> res;
			if (bridge()) res.pb("bridge");
			if (ffork()) res.pb("fork");
			if (ring()) res.pb("ring");
			if (res.empty()) continue;
			cout << "Case #" << tc++ << ": ";
			FOR(i, 0, sz(res)) {
				if (i) cout << "-";
				cout << res[i];
			}
			cout << " in move " << cur+1 << endl;
			done = true;
			break;
		}
		if (!done) cout << "Case #" << tc++ << ": none" << endl;
	}
	return 0;
}
