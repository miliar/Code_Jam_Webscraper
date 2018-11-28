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

char c[110][110];

int main(void) {
	int T; scanf("%d", &T);
	FOR(t,1,T+1) {
		int n, m; scanf("%d%d", &n, &m);
		REP(i,n)
			scanf("%s", c[i]);
		int ok=1;
		REP(i,n) {
			REP(j,m) {
				if(c[i][j]=='#') {
					if(i==n-1 || j==m-1) {
						ok=0;
						continue;
					}
					if(c[i][j+1]!='#')
						ok=0;
					if(c[i+1][j]!='#')
						ok=0;
					if(c[i+1][j+1]!='#')
						ok=0;
					c[i][j]=c[i+1][j+1]='/';
					c[i+1][j]=c[i][j+1]='\\';
				}
			}
		}
		printf("Case #%d:\n", t);
		if(!ok)
			puts("Impossible");
		else {
			REP(i,n)
				puts(c[i]);
		}
	}
	return 0;
}
			
