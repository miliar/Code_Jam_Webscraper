#include<iostream> 
#include<sstream> 
#include<cstdlib> 
#include<cmath> 
#include<vector> 
#include<string> 
#include<algorithm> 
using namespace std; 
typedef vector<int>VI;typedef vector<VI>VVI; 
typedef vector<string>VS; 
typedef pair<int,int>PII; 
#define FOR(i,n) for((i)=0;(i)<(n);(i)++) 
#define FORN(i,n) for((i)=(n)-1;(i)>=0;(i)--) 
#define BE(a) ((a).begin()),((a).end()) 
#define SI(a) ((a).size()) 
#define PB push_back 
#define MP make_pair 
#define FORIT(i,a) for((i)=(a).begin();(i)!=(a).end();(i)++) 
#define CLR(a,v) memset((a),(v),sizeof(a)) 

#define MD 1000000009

VVI g;
int n, k;
int C[505][505], F[505];
bool seen[505];
int memo[505];
bool seen_same[505][505];
bool memo_same[505][505];

inline int getF(int b, int a) {
	int ret = 1;
	int i;
	FOR (i,a) ret = (ret * (long long)(b - i)) % MD;
	return ret;
}

/*bool same(int u, int pu, int v, int pv) {
	bool & ret = memo_same[u][v];
	if (seen_same[u][v]) return ret;
	seen_same[u][v] = true;
	vector<bool> b;
	b = vector<bool>(SI(g[v]), true);
	int i, j, t, tj;
	FOR (t,SI(g[u])) if (g[u][t] != pu) {
		i = g[u][t];
		FOR (tj,SI(g[v])) if (g[v][tj] != pv && b[tj]) {
			j = g[v][tj];
			if (same(i, u, j, v)) {
				b[tj] = false;
				break;
			}
		}
		if (tj >= SI(g[v])) break;
	}
	ret = (t >= SI(g[u]));
	return ret;
}*/

int doit(int u, int p, int z) {
	int & ret = memo[u];
	if (seen[u]) return ret;
	seen[u] = true;
	//VI a, cnt;
	int i, j, t, zz;
	/*a.clear();
	cnt.clear();
	a.reserve(SI(g[u]));
	cnt.reserve(SI(g[u]));
	FOR (t,SI(g[u])) if (g[u][t] != p) {
		i = g[u][t];
		FOR (j,SI(a)) if (same(a[j], u, i, u)) break;
		if (j >= SI(a)) {
			a.PB(i);
			cnt.PB(1);
		} else cnt[j]++;
	}*/
	ret = 1;
	FOR (t,SI(g[u])) if (g[u][t] != p) {
		i = g[u][t];
		ret = (ret * (long long)doit(i, u, SI(g[u]))) % MD;
	}
	ret = (ret * (long long)getF(k - z, (int)SI(g[u]) - (u != p))) % MD;
	/*zz = k - z;
	FOR (i,SI(a)) {
		ret = (ret * (long long)getF(zz, cnt[i])) % MD; // C[zz][cnt[i]] * (long long)F[cnt[i]]
		zz -= cnt[i];
	}*/
	return ret;
}

int main() {
	int cases, casen, i, j, z;
	/*C[0][0] = 1;
	for (i = 1; i < 504; i++) {
		C[i][0] = C[i][i] = 1;
		for (j = 1; j < i; j++) C[i][j] = (C[i - 1][j - 1] + (long long)C[i - 1][j]) % MD;
	}
	F[0] = 1;
	for (i = 1; i < 505; i++) F[i] = (F[i - 1] * (long long)i) % MD;*/
	//cout << C[10][3] << endl;
	cin >> cases;
	for (casen = 1; casen <= cases; casen++) {
		cin >> n >> k;
		g = VVI(n, VI(0));
		FOR (z,n-1) {
			cin >> i >> j;
			i--; j--;
			g[i].PB(j);
			g[j].PB(i);
		}
		CLR(seen,0);
		//cout << same(1, 0, 2, 0) << endl;
		cout << "Case #" << casen << ": " << doit(0, 0, 0) << endl;
	}
	return 0;
}
