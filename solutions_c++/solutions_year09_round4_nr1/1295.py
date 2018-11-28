#include <cstdio>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#define FOR(i,a,b)	for(int i=(a); i<(b); ++i)
#define FORD(i,a,b)	for(int i=(a)-1; i>=b; --i)
#define FORE(i,q)	for(__typeof((q).begin()) i=(q).begin(); i!=(q).end(); ++i)
using namespace std;

typedef unsigned long long LG;

int T, N;

struct ttt {
	LG tab[40];
	int val;
} sss;

bool operator<(const ttt &s1, const ttt &s2) {
	FOR(i,0,N) {
		if(s1.tab[i] < s2.tab[i]) return true;
		if(s1.tab[i] > s2.tab[i]) return false;
	}
	return false;
}

void write(const ttt &s) {
	printf("!!! ");
	FOR(i,0,N) printf("%lld ", s.tab[i]);
	printf("(%d)\n", s.val);
}

int main() {
	scanf("%d", &T);
	FOR(z,0,T) {
		LG K = -1;
		sss.val = 0;
		scanf("%d", &N);
		FOR(i,0,N) {
			LG aa = 0;
			char str[44];
			scanf("%s", str);
			FOR(j,0,N) {
				aa += (str[j] == '1' ? 1LL << j : 0);
			}
			sss.tab[i] = aa;
			if(aa < (2LL << i) ) ++sss.val;
			//printf("%lld %d\n", aa, sss.val);
		}
		map<ttt, LG> S;
		S.clear();
		queue<ttt> Q;
		S[sss] = 1;
		Q.push(sss);
		while(!Q.empty()) {
			ttt v = Q.front(); Q.pop();
			//write(v);
			//printf("$$ %d\n", v.val);
			if(v.val == N) {
				//printf("$$ %d(%d)\n", v.val, N);
				K = S[v] - 1;
				break;
			}
			LG g = S[v];
			FOR(i,1,N) {
				int nj = 0;
				if( v.tab[i] < (2LL << i) && v.tab[i] >= (2LL << (i-1)) ) --nj;
				if(v.tab[i-1] >= (2LL << (i-1)) && v.tab[i-1] < (2LL << (i)) ) ++nj;
				LG xxx = v.tab[i]; v.tab[i] = v.tab[i-1]; v.tab[i-1] = xxx;
				v.val += nj;
				//write(v);
				if(S.find(v) == S.end()) Q.push(v), S[v] = g + 1;//, printf("* %lld (%d)\n", S[v], i);
				//else printf("---- %lld (%d)\n", S[v], i);
				v.val -= nj;
				xxx = v.tab[i]; v.tab[i] = v.tab[i-1]; v.tab[i-1] = xxx;
			}
		}
		printf("Case #%d: %lld\n", z + 1, K);
	}
	return 0;
}
