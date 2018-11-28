#include <cstdio>
#include <map>
#include <algorithm>
#include <cmath>
using namespace std;

#define rep(i,a,b) for (int i=(a); i<(b); ++i)
#define trav(it, v) for(typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it)

int mass[510][510];
int ycen[510][510];
int xcen[510][510];
int d[510][510];

int main() {
	int T;
	scanf("%d", &T);
	memset(mass, 0, sizeof(mass));
	memset(ycen, 0, sizeof(ycen));
	memset(xcen, 0, sizeof(xcen));
	rep(t,0,T) {
		int R,C,D;
		char w;
		scanf("%d%d%d", &R,&C,&D);
		rep(r,0,R) {
			rep(c,0,C) {
				scanf(" %c", &w);
				d[r][c] = w-'0';
			}
		}
		// Prefix sums
		rep(r,1,R+1) {
			int colsum = 0;
			rep(c,1,C+1) {
				colsum += d[r-1][c-1];
				mass[r][c] = mass[r-1][c] + colsum;
			}
		}
		rep(r,1,R+1) {
			rep(c,1,C+1) {
				ycen[r][c] = ycen[r-1][c] + (mass[r][c]-mass[r-1][c])*(r);
				xcen[r][c] = xcen[r][c-1] + (mass[r][c]-mass[r][c-1])*(c);
			}
		}
/*		printf("MASS\n");
		rep(r, 0, R+1) {
			rep(c, 0, C+1)
				printf("%3d",mass[r][c]);
			printf("\n");
		}
		printf("XCEN\n");
		rep(r, 0, R+1) {
			rep(c, 0, C+1)
				printf("%3d",xcen[r][c]);
			printf("\n");
		}
		printf("YCEN\n");
		rep(r, 0, R+1) {
			rep(c, 0, C+1)
				printf("%3d",ycen[r][c]);
			printf("\n");
		}*/
		
		int K = min(R,C)+1;
		bool found = false;
		while(--K>2&& !found) {
			rep(r,0,R-K+1) {
				rep(c,0,C-K+1) {
					int ycentrum = ycen[r+K][c+K]+ycen[r][c]-ycen[r+K][c]-ycen[r][c+K] - d[r][c]*(r+1) - d[r][c+K-1]*(r+1) - d[r+K-1][c]*(r+K) - d[r+K-1][c+K-1]*(r+K);
					int xcentrum = xcen[r+K][c+K]+xcen[r][c]-xcen[r+K][c]-xcen[r][c+K] - d[r][c]*(c+1) - d[r][c+K-1]*(c+K) - d[r+K-1][c]*(c+1) - d[r+K-1][c+K-1]*(c+K);
					int massa = mass[r+K][c+K]+mass[r][c]-mass[r+K][c]-mass[r][c+K] - d[r][c] - d[r][c+K-1] - d[r+K-1][c] - d[r+K-1][c+K-1];
					if (ycentrum*2 == massa*(2*(r+1)+K-1) && xcentrum*2 == massa*(2*(c+1)+K-1))
						found = true;
//					printf("%d %d %d %d %d %d\n", K, c, r, ycentrum, xcentrum, massa);
				}
			}
		}
		
		if (!found)
			printf("Case #%d: IMPOSSIBLE\n",t+1);
		else
			printf("Case #%d: %d\n",t+1,K+1);
	}
	return 0;
}