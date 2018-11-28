#include <map>
#include <vector>
#include <string>
#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;

#define ALL(x) x.begin(),x.end()
#define REP(i,n) for(int i=0,_n=(n);i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define PB push_back
#define ALLS(f,w) ({ bool _ok = true; f _ok = (_ok && (w)); _ok; })

typedef vector<int> VI; typedef pair<int,int > PII;
inline int getint() { int x; scanf("%d",&x); return x; }
inline void OPEN(string name) {
	string in = name+".in"; freopen(in.c_str(),"r",stdin);
	string out = name+".out"; freopen(out.c_str(),"w",stdout);
}

// Powered By TimoAI 2.2

int N,K;

vector< VI > data;
VI yes;
int ans;
int cache[17][17][1<<16];

int calc(int j,int last,int used) {
	int &ret=cache[j][last][used];
	if(ret>=0) return ret;
	if(used+1==1<<N) return ret = 0;
	if(j==N) {
		REP(i,N) if( (used & (1<<i))==0 ) {
			return ret = 1 + calc( i + 1, i, used | (1<<i) );
		}
	}else {
		VI curr = data[j];
		ret = calc( j + 1, last, used);
		// bisa merge
		if( (used & (1<<j))==0 && ALLS( REP(k,K), curr[k] > data[last][k] ) ) {
			int v = calc( j + 1, j, used | 1<<j );
			ret = min(ret, v);
		}
	}
	return ret;
}

int solve() {
	int ret = 0;
	int used[N];
	REP(i,N) used[i] = 0;
	REP(i,N) if(used[i]==0) {
		VI M = data[i];
		used[i] = 1;
		ret++;

		FOR(j,i+1,N) if(used[j]==0) {
			VI curr = data[j];
			if( ALLS( REP(k,K), curr[k] > M[k] ) ) {
				// bisa merge
				REP(k,K) M[k] >?= curr[k];
				used[j] = 1;
			}
		}
	}
	return ret;
}


int main() {
	OPEN("C");
	REP(ncase,getint()) {
		N = getint();
		K = getint();
		data.clear();
		REP(i,N) {
			VI nums;
			REP(j,K) nums.PB( getint() );
			data.PB( nums );
		}
		sort( ALL(data) );
		// ans = N;
		memset(cache,-1,sizeof(cache));
		ans = calc(1,0,1);
		printf("Case #%d: %d\n",ncase+1,ans+1);


		// printf("Case #%d: %d\n",ncase+1,solve() );
	}
	return 0;
}
