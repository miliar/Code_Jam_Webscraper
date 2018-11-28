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

int c[110][110], d[110][110];

int main(void) {
	int t, T, n, m, i, j, k, x1, y1, x2, y2, res, ok;
	scanf("%d", &T);
	FOR(t,1,T+1) {
		scanf("%d", &n);
		memset(c, 0, sizeof c);
		REP(i,n) {
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			--x1; --y1;
			FOR(j,y1,y2) {
				FOR(k,x1,x2)
					c[j][k]=1;
			}
		}
		res=0; ok=1;
		while(ok) {
			REP(i,100) {
				REP(j,100) {
					d[i][j]=0;
					if(c[i][j]) {
						if(i>0 && j>0 && (c[i-1][j]==1 || c[i][j-1]==1))
							d[i][j]=1;
					}
					else {
						if(i>0 && j>0 && c[i-1][j]==1 && c[i][j-1]==1)
							d[i][j]=1;
					}
				}
			}
			ok=0;
			REP(i,100) {
				REP(j,100) {
					c[i][j]=d[i][j];
					if(c[i][j])
						ok=1;
				}
			}
			++res;
		}
		printf("Case #%d: %d\n", t, res);
	}
	return 0;
}
