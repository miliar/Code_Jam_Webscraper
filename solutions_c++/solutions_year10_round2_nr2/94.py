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

int x[110], v[110];

int main(void) {
	int t, T, n, m, i, j, k, res, ile, B, C;
	scanf("%d", &T);
	FOR(t,1,T+1) {
		scanf("%d%d%d%d", &n, &k, &B, &C);
		REP(i,n) {
			scanf("%d", &x[i]);
			x[i]=B-x[i];
		}
		REP(i,n)
			scanf("%d", &v[i]);
		res=0;
		for(i=n-1, j=0, ile=0; i>=0 && j<k; --i) {
			if(x[i]>v[i]*C)
				++ile;
			else {
				++j;
				res+=ile;
			}
		}
		if(j==k)
			printf("Case #%d: %d\n", t, res);
		else
			printf("Case #%d: IMPOSSIBLE\n", t);
	}
	return 0;
}
