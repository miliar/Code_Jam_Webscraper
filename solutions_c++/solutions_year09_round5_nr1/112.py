#include<iostream>
#include<cstdio>
#include<string>
#include<vector>
#include<map>
#include<cmath>
#include<algorithm>
#include<set>
using namespace std;

#define sz(q) ((int)(q).size())
#define _fill(mem,v) memset(mem,v,sizeof(mem))
#define FOR(i,q1,q2) for(int i=(q1); i<=(q2); ++i)
#define FORD(i,q1,q2) for(int i=(q1); i>=(q2); --i)
#define FOREACH(it,mp) for(typeof((mp).begin()) it=(mp).begin(); it!=(mp).end(); ++it)

#define isdig(c) ('0'<=(c) && (c)<='9')

#define inbit(i,n) ((n & (1<<i))>0?1:0)
#define bit(i) (1<<i)

#define mp make_pair
#define xx first
#define yy second

typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;

#define MAXGG 10100100

int T, N, M, K;
char lv[20][20], ww[20][20];
int ss[20][20], bb[20];

const int dx[4] = {0, 1, 0, -1}, dy[4] = {1, 0, -1, 0};

struct POS {
	pii a[5];
	
	void fromId(ll code) {
		for(int i=K-1; i>=0; --i) {
			a[i].xx = code%12;
			a[i].yy = (code/12)%12;
			code /= 144;
		}
	}
	
	ll getId() {
		sort(a, a+K);
		ll res = 0;
		for(int i=0; i<K; ++i) {
			res = res*144 + a[i].xx + a[i].yy*12;
			if( res<0 )
				cerr << "res overloaded" << endl;
		}
		return res;
	}
	
	bool operator<(const POS &p1) const {
		for(int i=0; i<K; ++i)
			if( a[i]!=p1.a[i] )
				return a[i]<p1.a[i];
		return false;
	}
	
	void dfs(int ind) {
		bb[ind] = 1;
		for(int i=0; i<K; ++i)
			if( ss[ind][i] && !bb[i] )
				dfs(i);
	}
	
	bool isDanger() {
		for(int i=0; i<K; ++i)
			for(int j=i+1; j<K; ++j)
				if( abs(a[i].xx - a[j].xx) + abs(a[i].yy - a[j].yy) <= 1 )
					ss[j][i] = ss[i][j] = 1;
				else ss[j][i] = ss[i][j] = 0;
		memset(bb, 0, sizeof(bb));
		dfs(0);
		//cout << "@" << bb[0] << bb[1] << endl;
		for(int i=0; i<K; ++i)
			if( !bb[i] ) return true;
		return false;
	}
	
	bool canMove(int ind, int dir, bool isdan) {
		pii q = pii(a[ind].xx+dx[dir], a[ind].yy+dy[dir]), qq = pii(a[ind].xx-dx[dir], a[ind].yy-dy[dir]);
		
		if( q.xx<0 || q.xx>=N || q.yy<0 || q.yy>=M || lv[q.xx][q.yy]=='#' )
			return false;
		if( qq.xx<0 || qq.xx>=N || qq.yy<0 || qq.yy>=M || lv[qq.xx][qq.yy]=='#' )
			return false;
		
		for(int i=0; i<K; ++i)
			if( a[i]==q || a[i]==qq )
				return false;
		
		a[ind] = q;
		bool isdan2 = isDanger();
		a[ind].xx -= dx[dir];
		a[ind].yy -= dy[dir];
		if( isdan2 && isdan )
			return false;
		return true;
	}
	
	void moveFrom(POS &pos, int ind, int dir) {
		for(int i=0; i<K; ++i)
			a[i] = pos.a[i];
		a[ind].xx += dx[dir];
		a[ind].yy += dy[dir];
	}
	
	void print() {
//		for(int i=0; i<K; ++i) printf("(%d, %d)\n", a[i].xx, a[i].yy);
		for(int i=0; i<N; ++i) {
			for(int j=0; j<M; ++j)
				if( lv[i][j]=='#' )
					ww[i][j] = '#';
				else ww[i][j] = '.';
			ww[i][M] = 0;
		}
		for(int i=0; i<K; ++i)
			ww[a[i].xx][a[i].yy] = 'x';
		for(int i=0; i<N; ++i)
			printf("%s\n", ww[i]);
		printf("------------\n");
	}
};

map<ll, int> dd;
ll gg[MAXGG], ngg;

int main() {
	scanf("%d", &T);
	for(int it=1; it<=T; ++it) {
		int ans = -1;
		scanf("%d%d", &N, &M);
		for(int i=0; i<N; ++i)
			scanf("%s", lv[i]);

		POS st, fi, pos;
		int k1=0, k2=0;
		for(int i=0; i<N; ++i)
			for(int j=0; j<M; ++j) {
				if( lv[i][j]=='x' || lv[i][j]=='w' )
					fi.a[k2++] = pii(i,j);
				if( lv[i][j]=='o' || lv[i][j]=='w' )
					st.a[k1++] = pii(i,j);
			}
		K = k1;
		if( k1!=k2 ) cerr << "k1!=k2" << endl;
		
		ngg = 0;
		dd.clear();
		ll code = st.getId(), finCode = fi.getId();
		if( code==finCode )
			ans = 0;
		dd[code] = 0;
		gg[ngg++] = code;
		for(int igg=0; igg<ngg && ans==-1; ++igg) {
			pos.fromId(gg[igg]);
			int dist = dd[gg[igg]];
			//pos.print();
			
			bool isDanger = pos.isDanger();
			//cout << isDanger << endl;
			for(int i=0; i<K; ++i)
				for(int dir=0; dir<4; ++dir)
					if( pos.canMove(i, dir, isDanger) ) {
						st.moveFrom(pos, i, dir);
						code = st.getId();
						//st.print();
						if( dd.find(code)==dd.end() ) {
							gg[ngg++] = code;
							dd[code] = dist+1;
							if( code==finCode ) {
								ans = dist+1;
								break;
							}
						}
					}
		}
		//cout << ngg << endl;
		
		printf("Case #%d: %d\n", it, ans);
	}
	
	return 0;
}
