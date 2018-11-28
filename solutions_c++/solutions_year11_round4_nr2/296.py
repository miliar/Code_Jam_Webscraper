#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<vector>
#include<string>
#include<algorithm>
#include<queue>
using namespace std;

#define min(a,b) (((a)<(b))?(a):(b))
#define max(a,b) (((a)>(b))?(a):(b))
#define rep(i,n) for(i=0;i<(n);i++)
#define MAXN 120
#define EPS 1e-8

int g[MAXN][MAXN];
int R,C,D;

int main() {
	int T,kase=1;
	char s[1000];
	int i,j,k,a,b;
	int r1,r2,c1,c2;
	double sx,sy,s2,cx,cy;
	int res;
	scanf(" %d",&T);
	while(T--) {
		printf("Case #%d: ",kase++);
		scanf(" %d %d %d",&R,&C,&D);
		rep(i,R) {
			scanf(" %s",s);
			rep(j,C) g[i][j] = s[j]-'0';
		}

		//odd size
		res = -1;
		rep(i,R) rep(j,C) {
			//if(i < 1 || j < 1 || i >= R-1 || j >= C-1) continue;
			for(k=1;;k++) {
				r1 = i - k;
				r2 = i + k;
				c1 = j - k;
				c2 = j + k;
				if(r1 < 0 || r2 > R-1 || c1 < 0 || c2 > C-1) break;

				sx = sy = s2 = 0;
				for(a=r1;a<=r2;a++) {
					for(b=c1;b<=c2;b++) {
						if(a == r1 && b == c1) continue;
						if(a == r1 && b == c2) continue;
						if(a == r2 && b == c1) continue;
						if(a == r2 && b == c2) continue;
						sx += (D + g[a][b]) * (a + .5);
						sy += (D + g[a][b]) * (b + .5);
						s2 += (D + g[a][b]);
					}
				}
				cx = sx / s2;
				cy = sy / s2;
				if(fabs(cx - i - .5) < EPS && fabs(cy - j - .5) < EPS) {
					res = max(res, 2*k+1);
				//	printf("%d %d %d %d %d\n",2*k+1, r1, c1, r2, c2);
				}
			}
		}

		//even size
		rep(i,R) rep(j,C) {
			//if(i < 1 || j < 1 || i >= R-1 || j >= C-1) continue;
			for(k=2;;k++) {
				r1 = i - k + 1;
				r2 = i + k;
				c1 = j - k + 1;
				c2 = j + k;
				if(r1 < 0 || r2 > R-1 || c1 < 0 || c2 > C-1) break;

				sx = sy = s2 = 0;
				for(a=r1;a<=r2;a++) {
					for(b=c1;b<=c2;b++) {
						if(a == r1 && b == c1) continue;
						if(a == r1 && b == c2) continue;
						if(a == r2 && b == c1) continue;
						if(a == r2 && b == c2) continue;
						sx += (D + g[a][b]) * (a + .5);
						sy += (D + g[a][b]) * (b + .5);
						s2 += (D + g[a][b]);
					}
				}
				cx = sx / s2;
				cy = sy / s2;
				if(fabs(cx - i - 1) < EPS && fabs(cy - j - 1) < EPS) {
					res = max(res, 2*k);
					//printf("%d %d %d %d %d\n",2*k, r1, c1, r2, c2);
				}
			}
		}

		if(res < 3) printf("IMPOSSIBLE\n");
		else printf("%d\n",res);
	}
	return 0;
}