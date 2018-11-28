#include<cstdio>
#include<cmath>
#include<cstring>
#include<map>
#define x first
#define y second

using namespace std;

int main(){
	int T;
	scanf("%d", &T);
	for (int cc = 1; cc <= T; ++cc){
		printf("Case #%d: ", cc);
		int n, A, B, C, D, x0, y0, M;
		scanf("%d%d%d%d%d%d%d%d", &n, &A, &B, &C, &D, &x0, &y0, &M);
		long long P[n][2];
		P[0][0] = x0, P[0][1] = y0;
		for (int i = 1; i < n ; ++i){
			long long nx, ny;
			nx = (long long)A;
			nx = (nx*P[i-1][0]+B)%M;
			ny = (long long)C;
			ny = (ny*P[i-1][1]+D)%M;
			P[i][0] = nx;
			P[i][1] = ny;
		}
		long long ans = 0;
		long long cnt[3][3];
		memset(cnt, 0, sizeof(cnt));
		for (int i = 0 ; i < n; ++i)
			cnt[P[i][0]%3][P[i][1]%3]++;
		/*for (int i = 0 ; i < 3; ++i)
			for (int j = 0 ; j < 3; ++j)
				printf("%d %d: %d\n", i, j, cnt[i][j]);*/
		pair<int, int> TL[9];
		int ptr = 0;
		for (int i = 0 ; i < 3; ++i)
			for (int j = 0 ; j < 3; ++j)
				TL[ptr++] = pair<int, int>(i, j);
		for (int i = 0 ; i < 9; ++i)
			for (int j = i ; j < 9 ; ++j)
				for (int k = j; k < 9 ; ++k){
					pair<int, int> W = TL[i], X=TL[j], Y=TL[k];
					//printf("%d %d %d\n", i, j, k);
					if ((W.x+X.x+Y.x)%3 == 0 && (W.y+X.y+Y.y)%3 == 0){
						long long wc = cnt[W.x][W.y];
						long long xc = cnt[X.x][X.y];
						long long yc = cnt[Y.x][Y.y];
						if (i!=j && j!=k && k != i) ans += wc*xc*yc;
						if (i==j && j!=k){
							if (wc>1) ans += wc*(wc-1)/2*yc;
						}
						if (j==k && i!=k){
							xc--;
							if (xc>1) ans += wc*xc*(xc-1)/2;
						}
						if (i==k && j!=i){
							if (wc>1){
								ans += xc*wc*(wc-1)/2;
							}
						}
						if (i==j && j==k){
							if (wc>2){
								long long cu = wc;
								cu = cu*(wc-1)*(wc-2)/6;
								ans += cu;
							}
						}
					}
				}
		printf("%lld\n", ans);
	}
	return 0;
}
