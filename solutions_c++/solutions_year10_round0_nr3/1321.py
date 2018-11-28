#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>

#define REP(AA,BB) for(AA=0; AA<(BB); ++AA)
#define FOR(AA,BB,CC) for(AA=(BB); AA<(CC); ++AA)
#define FC(AA,BB) for(typeof(AA.begin()) BB=AA.begin(); BB!=AA.end(); ++BB)
#define SZ(AA) ((int)(AA.size()))
#define ALL(AA) (AA).begin(), (AA).end()
#define PB push_back
#define MP(AA,BB) make_pair((AA), (BB))

using namespace std;

typedef vector<int> VI;
typedef pair<int, int> PII;

int next[1010], x[1010], c[2010];

int main(void) {
	int t, T, n, m, i, j, k, R, K; long long res;
	scanf("%d", &T);
	FOR(t,1,T+1) {
		scanf("%d%d%d", &R, &K, &n);
		REP(i,n)
			scanf("%d", &c[i]);
		FOR(i,n,2*n)
			c[i]=c[i-n];
		REP(i,n) {
			for(j=i, k=0; j<i+n; ++j) {
				if(k+c[j]>K)
					break;
				k+=c[j];
			}
			if(j>=n)
				next[i]=j-n;
			else
				next[i]=j;
			x[i]=k;
		}
		res=0LL; j=0;
		REP(i,R) {
			res+=x[j];
			j=next[j];
		}
		printf("Case #%d: %lld\n", t, res);
	}
	return 0;
}
