#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
using namespace std;
 
typedef long long LL;
typedef vector<int> vi;
typedef vector< pair<int, int> > vii;
#define MP(x,y) make_pair(x, y)
 
char a[555][555];
int w[555][555];
int xsum[555][555], ysum[555][555];
int xdp[555][555], ydp[555][555], dp[555][555];


inline int XDP(int ax, int ay, int bx, int by) {
	int ret = xdp[bx][by] - xdp[bx][ay-1] - (by-ay+1) * (dp[bx][ay-1]);
	
	//printf("XDP %d %d %d %d =%d %d\n", ax, ay, bx, by, ret, xdp[bx][by] - xdp[bx][ay-1]);
	ret -= xdp[ax-1][by] - xdp[ax-1][ay-1] - (by-ay+1) * (dp[ax-1][ay-1]);
	return ret;
}
inline int YDP(int ax, int ay, int bx, int by) {
	int ret = ydp[bx][by] - ydp[ax-1][by] - (bx-ax+1) * (dp[ax-1][by]);
	ret -= ydp[bx][ay-1] - ydp[ax-1][ay-1] - (bx-ax+1) * (dp[ax-1][ay-1]);
	return ret;
}
inline int DP(int ax, int ay, int bx, int by) {
	return dp[bx][by] + dp[ax-1][ay-1] - dp[ax-1][by] - dp[bx][ay-1];
}
int main(void) {
    int T, cs, m, n, D, i, j, k;
    scanf("%d", &T);
    for(cs=1;cs<=T;cs++) {
		scanf("%d%d%d", &m, &n, &D);
		//memset(xsum,0,sizeof(xsum));
		memset(xdp,0,sizeof(xdp));
		memset(ydp,0,sizeof(ydp));
		//memset(ysum,0,sizeof(ysum));
		memset(dp, 0, sizeof(dp));
		memset(a, 0, sizeof(a));
		for(i=1;i<=m;i++) {
			scanf("%s", a[i]+1);
			for(j=1;j<=n;j++) {
				w[i][j] = a[i][j]-'0';
				//ysum[i][j] = ysum[i][j-1] + a[i][j]-'0';
				//xsum[i][j] = xsum[i-1][j] + a[i][j]-'0';
				dp[i][j] = dp[i][j-1]+dp[i-1][j]-dp[i-1][j-1] + w[i][j];
				xdp[i][j] = dp[i][j] + xdp[i][j-1];
				ydp[i][j] = dp[i][j] + ydp[i-1][j];
				//printf("(%d,%d) %d %d %d\n", i, j, dp[i][j], xdp[i][j], ydp[i][j]);
			}
		}
		int sol = -1, sx, sy;
		for(k=min(m, n); k>=3;k--) {
			if(k%2) {
				for(i=1;i<=m-k+1;i++)
					for(j=1;j<=n-k+1;j++) {
						int xs = XDP(i, j, i+k-1, j+k/2-1);
						xs +=         XDP(i, j+k/2+1, i+k-1, j+k-1);
						xs += -(k/2+1)*DP(i, j+k/2+1, i+k-1, j+k-1);
						int ys = YDP(i, j, i+k/2-1, j+k-1);
						ys +=         YDP(i+k/2+1, j, i+k-1, j+k-1);
						ys += -(k/2+1)*DP(i+k/2+1, j, i+k-1, j+k-1);
						xs -= (w[i][j] + w[i+k-1][j] - w[i][j+k-1] - w[i+k-1][j+k-1]) * (k/2);
						ys -= (w[i][j] - w[i+k-1][j] + w[i][j+k-1] - w[i+k-1][j+k-1]) * (k/2);
						//printf("i=%d, j=%d, k=%d, xs=%d, ys=%d\n", i, j, k, xs, ys);
						if(xs==0 && ys==0 && sol==-1) {
							sol = k;
							sx = i;
							sy = j;
						}
					}
			} else {
				for(i=1;i<=m-k+1;i++)
					for(j=1;j<=n-k+1;j++) {
						int xs = XDP(i, j, i+k-1, j+k/2-1);
						xs += XDP(i, j+k/2, i+k-1, j+k-1);
						xs += -(k/2+1)*DP(i, j+k/2, i+k-1, j+k-1);
						int ys = YDP(i, j, i+k/2-1, j+k-1);
						ys += YDP(i+k/2, j, i+k-1, j+k-1);
						ys += -(k/2+1)*DP(i+k/2, j, i+k-1, j+k-1);
						xs *= 2;
						ys *= 2;
						xs -= DP(i, j, i+k-1, j+k/2-1) - DP(i, j+k/2, i+k-1, j+k-1);
						ys -= DP(i, j, i+k/2-1, j+k-1) - DP(i+k/2, j, i+k-1, j+k-1);
						xs -= (w[i][j] + w[i+k-1][j] - w[i][j+k-1] - w[i+k-1][j+k-1]) * (k-1);
						ys -= (w[i][j] - w[i+k-1][j] + w[i][j+k-1] - w[i+k-1][j+k-1]) * (k-1);
						if(xs==0 && ys==0 && sol==-1) {
							sol = k;
							sx = i;
							sy = j;
						}
					}
			}
		}
        printf("Case #%d: ", cs);
		if(sol==-1) printf("IMPOSSIBLE\n");
		else printf("%d\n", sol);

		fprintf(stderr, "Case #%d: ", cs);
		if(sol==-1) fprintf(stderr, "IMPOSSIBLE\n");
		else fprintf(stderr, "%d\n", sol);
    }
    return 0;
}

