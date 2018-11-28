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

int a[110];

int main(void) {
	int T; scanf("%d", &T);
	FOR(t,1,T+1) {
		int n; int L, R; scanf("%d%d%d", &n, &L, &R);
		REP(i,n)
			scanf("%d", &a[i]);
		int res=-1;
		FOR(i,L,R+1) {
			int ok=1;
			REP(j,n) {
				if(i%a[j]!=0 && a[j]%i!=0) {
					ok=0;
					break;
				}
			}
			if(ok) {
				res=i;
				break;
			}
		}
		if(res==-1)
			printf("Case #%d: NO\n", t);
		else
			printf("Case #%d: %d\n", t, res);
	}
	return 0;
}
