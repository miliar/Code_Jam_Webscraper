#include<cstdio>
#include<cstring>
#include<vector>
#include<string>
#include<algorithm>
#include<queue>

using namespace std;

int main(){
	int T;
	scanf("%d", &T);
	for (int cc = 1; cc <= T; ++cc){
		printf("Case #%d: ", cc);
		int H, W, R;
		scanf("%d%d%d", &H, &W, &R);
		bool isob[H][W];
		memset(isob, 0, sizeof(isob));
		for (int i = 0 ; i < R; ++i){
			int x, y;
			scanf("%d%d", &x, &y);
			isob[--x][--y] = 1;
		}
		int DP[H][W];
		memset(DP, 0, sizeof(DP));
		DP[0][0] = 1;

		for (int i = 0 ; i < H; ++i){
			for (int j = 0 ; j < W; ++j){
				if (isob[i][j]){
					DP[i][j] = 0;
					continue;
				}
				int p, q;
				p = i-1, q = j-2;
				if (p >= 0 && q >= 0) DP[i][j] = (DP[i][j]+DP[p][q])%10007;
				p = i-2, q = j-1;
				if (p >= 0 && q >= 0) DP[i][j] = (DP[i][j]+DP[p][q])%10007;
			}
		}
		printf("%d\n", DP[H-1][W-1]);
	}
	return 0;
}
