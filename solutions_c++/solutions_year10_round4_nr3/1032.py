#include <algorithm>
#include <cstdio>
#include <cstring>
using namespace std;
#define chkMax(x,y) if(x<y)x=y
#define chkMin(x,y) if(x>y)x=y
#define CLR(x) memset(x,0,sizeof(x))
#define FOR(i,s,e) for(int i=s;i<e;i++)
const int M = 105, inf = 10000000;
int main() {
	int z, rr;
	scanf("%d", &z);
	for (int zz=1;zz<=z;zz++) {
		scanf("%d", &rr);
		int ans = 0, cnt = 0;
		bool v[2][M][M] = {0};
		int last = 0, cur = 1;
		while (rr--) {
			int a,b,c,d;
			scanf("%d%d%d%d",&a,&b,&c,&d);
			FOR(i,a,c+1) FOR(j,b,d+1) v[0][i][j] = 1;
		}
		FOR(i,1,M) FOR(j,1,M) cnt += v[0][i][j];
		while (cnt) {
			FOR(i,1,M) FOR(j,1,M) {
				v[cur][i][j] = v[last][i][j];
				if (v[last][i][j]) {
					if (!v[last][i][j-1] && !v[last][i-1][j])
						v[cur][i][j] = 0, cnt --;
				} else {
					if (v[last][i][j-1] && v[last][i-1][j])
						v[cur][i][j] = 1, cnt ++;
				}
			}
			ans++;
			swap(cur, last);
		}
		printf("Case #%d: %d\n", zz, ans);
	}
	return 0;
}
