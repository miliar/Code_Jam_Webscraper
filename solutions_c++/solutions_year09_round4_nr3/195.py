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

int N, K, pr[200][30];
int ed[200][200], rr[200], bb[200];

bool above(int i, int j) {
	for(int k=0; k<K; ++k)
		if( pr[i][k]<=pr[j][k] ) return false;
	return true;
}

bool upd(int ver) {
	if( bb[ver] ) return false;
	bb[ver] = true;
	for(int i=0; i<N; ++i)
		if( ed[ver][i] && (rr[i]==-1 || upd(rr[i])) ) {
			rr[i] = ver;
			return true;
		}
	return false;
}

int main() {
	int T;
	scanf("%d", &T);
	for(int it=1; it<=T; ++it) {
		scanf("%d%d", &N, &K);
		for(int i=0; i<N; ++i) {
			for(int j=0; j<K; ++j)
				scanf("%d", &pr[i][j]);
			rr[i] = -1;
		}
		
		memset(ed, 0, sizeof(ed));
		for(int i=0; i<N; ++i)
			for(int j=0; j<N; ++j)
				if( above(i,j) )
					ed[i][j] = 1;
				else ed[i][j] = 0;
		
		int ans = N;
		for(int i=0; i<N; ++i) {
			memset(bb, 0, sizeof(bb));
			if( upd(i) ) ans--;
		}
		printf("Case #%d: %d\n", it, ans);
	}
	return 0;
}
