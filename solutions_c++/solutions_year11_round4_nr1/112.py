#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>

#define REP(AA,BB) for(int AA=0; AA<(BB); ++AA)
#define FOR(AA,BB,CC) for(int AA=(BB); AA<(CC); ++AA)
#define FC(AA,BB) for(__typeof((AA).begin()) BB=(AA).begin(); BB!=(AA).end(); ++BB)
#define SZ(AA) ((int)((AA).size()))
#define ALL(AA) (AA).begin(), (AA).end()
#define PB push_back
#define MP make_pair

using namespace std;

typedef vector<int> VI;
typedef pair<int, int> PII;
typedef long long LL;
typedef long double LD;

int R;

struct st {
	int v, len;
	st(int _v=0, int _len=0) : v(_v), len(_len) {}
	int operator<(const st &a) const {
		return v<a.v;
	}
};

int main(void) {
	int T; scanf("%d", &T);
	FOR(t,1,T+1) {
		int X, S, time, N; scanf("%d%d%d%d%d", &X, &S, &R, &time, &N); 
		vector<st> p; R-=S;
		REP(i,N) {
			int a, b, w; scanf("%d%d%d", &a, &b, &w);
			p.PB(st(S+w, b-a));
			X-=(b-a);
		}
		//printf("%d\n", X);
		if(X>0)
			p.PB(st(S,X));
		sort(ALL(p)); LD res=0.0; LD TT=time;
		REP(i,SZ(p)) {
			int ve=p[i].v+R;
			if(p[i].len<=TT*ve) {
				res+=(0.0+p[i].len)/(0.0+ve);
				TT-=(0.0+p[i].len)/(0.0+ve);
			}
			else if(TT>1e-12) {
				LD s=0.0+p[i].len-TT*ve;
				res+=TT;
				TT=0.0;
				res+=s/p[i].v;
			}
			else if(TT<=1e-12)
				res+=(0.0+p[i].len)/p[i].v;
		}
		printf("Case #%d: %.10Lf\n", t, res);
	}
	return 0;
}
			
