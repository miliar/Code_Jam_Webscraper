#include <stdio.h>
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <bitset>
#include <cmath>
#include <algorithm>
#include <sstream>
#include <cstring>
#include <iomanip>
using namespace std;
#define REP(i,n) for (int i=0; i<(n); ++i)
#define FOR(i,a,b) for (int i=(a); i<=(b); ++i)
#define FORD(i,a,b) for (int i=(a); i>=(b); --i)
#define FORE(it, X) for(__typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define debug(x) cerr << #x << " = " << x << "\n";
#define debugv(x) cerr << #x << " = "; FORE(it,(x)) cerr<< *it <<","; cerr<<"\n";
#define PB push_back
#define ALL(x) (x).begin(),(x).end()
#define CLR(x) memset(x,0,sizeof x)
#define xx first
#define yy second
typedef long long int lli;
typedef pair<int, int> P;
typedef vector<int> vi;
#define MAXN 17
#define INF 100000007
template <class Ty, class Tx>
Ty cast(const Tx &x) {
	 Ty y; stringstream ss(""); ss<<x; ss.seekg(0); ss>>y; return y;
}


int T;
int R,C;
char pl[MAXN][MAXN];

map<vi, int> M;
set<vi> vis;
map<vi, bool> ST;
int dx[]={-1,1,0,0};
int dy[]={0,0,1,-1};


bool jest[MAXN];
vi ak;

void go(int x){
	REP(i,ak.size())
		if(ak[i] == x && !jest[i]){
			jest[i]=true;
			go(x+1);
			go(x-1);
			go(x+MAXN);
			go(x-MAXN);
		}
}

bool stab(vi v){
	ak=v;
	if(!ST.count(v)){
		CLR(jest);
		go(ak[0]);
		bool res=true;
		REP(i,ak.size()) if(!jest[i]) res=false;
		ST[v]=res;
	}
	return ST[v];
}

int main(){
	cin >> T;
	FOR(cas,1,T){
		//in
		M.clear();
		vis.clear();
		ST.clear();
		cin >> R >> C;
		FOR(i,1,R) scanf("%s",&pl[i][1]);
		REP(i,R+1) pl[i][0]=pl[i][C+1]='#';
		REP(i,C+1) pl[0][i]=pl[R+1][i]='#';
		vi pocz, kon;
		FOR(x,1,R) FOR(y,1,C) if(pl[x][y] == 'o' || pl[x][y] == 'w') pocz.PB(x*MAXN+y);
		FOR(x,1,R) FOR(y,1,C) if(pl[x][y] == 'x' || pl[x][y] == 'w') kon.PB(x*MAXN+y);
		sort(ALL(pocz));
		sort(ALL(kon));
		queue<vi> Q;
		Q.push(pocz);
		M[pocz]=1;
		int res=INF;
		//rozw
		while(!Q.empty()){
			vi v=Q.front(); Q.pop();
			if(vis.count(v)) continue;
			vis.insert(v);
//		if(cas == 6) {FORE(i,v) cout << *i << " "; cout << " = " << M[v] << " " << stab(v) << endl;}
			if(v == kon){
				res=M[kon];
				break;
			}
			int ko=M[v];
			REP(i,v.size()){
				int x=v[i]/MAXN;
				int y=v[i]%MAXN;
				REP(k,4){
					int nx=x-dx[k];
					int ny=y-dy[k];
					bool ok=true;
					FORE(q,v) if(*q == nx*MAXN+ny) ok=false;
					if(pl[nx][ny] == '#') continue;
					nx=x+dx[k];
					ny=y+dy[k];
					if(pl[nx][ny] == '#') continue;
					FORE(q,v) if(*q == nx*MAXN+ny) ok=false;
					if(!ok) continue;
					vi w=v;
					w[i]=nx*MAXN+ny;
					sort(ALL(w));
					if(!stab(v) && !stab(w)) continue;
					if(M[w]==0 || M[w]>ko+1){
						M[w]=ko+1;
//					if(cas==6)	cout << "-->" << k << " " << w[0] << " " << w[1] << endl;
						Q.push(w);
					}
				}
			}
		}
		///out
		if(res == INF) res=-1;
		else res--;
		cout << "Case #" << cas << ": " << res << endl;
	}
	return 0;
}
