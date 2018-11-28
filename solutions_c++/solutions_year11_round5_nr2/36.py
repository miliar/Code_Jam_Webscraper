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

int p[10100];

int main(void) {
	int T; scanf("%d", &T);
	FOR(t,1,T+1) {
		int n; scanf("%d", &n);
		memset(p, 0, sizeof p);
		REP(i,n) {
			int a; scanf("%d", &a);
			++p[a];
		}
		int mn=1000000;
		VI cur;
		REP(i,10002) {
			VI tmp; int j;
			while(p[i]>SZ(cur)) {
				tmp.PB(1);
				--p[i];
			}
			for(j=0; j<SZ(cur) && p[i]>0; ++j) {
				tmp.PB(cur[j]+1);
				--p[i];
			}
			if(j<SZ(cur))
				mn=min(mn, cur[j]);
			cur=tmp;
		}
		if(mn==1000000)
			mn=0;
		printf("Case #%d: %d\n", t, mn);
	}
	return 0;
}
				
