#include <cstdio>
#include <cstring>

int N, M, D;
int ans;
char g[1000][1000];
int shaX[1000][1000], shaY[1000][1000], sum[1000][1000];

void init() {
	scanf("%d%d%d", &N, &M, &D);
	for (int i=0;i<N;i++)
		scanf("%s", &g[i]);
		
	memset(shaX, 0, sizeof(shaX));
	memset(shaY, 0, sizeof(shaY));
	memset(sum, 0, sizeof(sum));
	for (int i=1;i<=N;i++)
		for (int j=1;j<=M;j++) {
			int w = g[i-1][j-1] - '0';
			shaX[i][j] = shaX[i-1][j] + shaX[i][j-1] - shaX[i-1][j-1] + w * ((i - 1) * 2 + 1);
			shaY[i][j] = shaY[i-1][j] + shaY[i][j-1] - shaY[i-1][j-1] + w * ((j - 1) * 2 + 1);
			sum[i][j] =  sum[i-1][j]  + sum[i][j-1]  - sum[i-1][j-1]  + w;
		}
}

void work() {
	ans = -1;
	for (int k=N-1;k>=2;k--)
		for (int x1=1;x1+k<=N;x1++)
			for (int y1=1;y1+k<=M;y1++) {
				int x2 = x1 + k, y2 = y1 + k;
				int w;
				
				int xs  = shaX[x2][y2] + shaX[x1-1][y1-1] - shaX[x2][y1-1] - shaX[x1-1][y2];
				int ys  = shaY[x2][y2] + shaY[x1-1][y1-1] - shaY[x2][y1-1] - shaY[x1-1][y2];
				int s   = sum [x2][y2] + sum [x1-1][y1-1] - sum [x2][y1-1] - sum [x1-1][y2];
				
				w = g[x1-1][y1-1] - '0';
				xs -= w * ((x1 - 1) * 2 + 1);
				ys -= w * ((y1 - 1) * 2 + 1);
				s  -= w;
				w = g[x1-1][y2-1] - '0';
				xs -= w * ((x1 - 1) * 2 + 1);
				ys -= w * ((y2 - 1) * 2 + 1);
				s  -= w;
				w = g[x2-1][y1-1] - '0';
				xs -= w * ((x2 - 1) * 2 + 1);
				ys -= w * ((y1 - 1) * 2 + 1);
				s  -= w;
				w = g[x2-1][y2-1] - '0';
				xs -= w * ((x2 - 1) * 2 + 1);
				ys -= w * ((y2 - 1) * 2 + 1);
				s  -= w;
				
				//if (N == 3 && M == 3) printf("%d\n", s);
				
				xs -= s * 2 * (x1 - 1);
				ys -= s * 2 * (y1 - 1);
				
				if (xs == s * (k + 1) &&
					ys == s * (k + 1)) {
					ans = k;
					return;
				}
			}		
}

int main() {
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T;
	scanf("%d", &T);
	for (int ti=1;ti<=T;ti++) {
		init();
		printf("Case #%d: ", ti);
		work();
		if (ans != -1)
		printf("%d\n", ans+1);
		else
			printf("IMPOSSIBLE\n");
	}
	return 0;
}

