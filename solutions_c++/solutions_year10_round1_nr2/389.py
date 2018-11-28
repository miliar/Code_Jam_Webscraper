#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;
int T, CT = 1;
int D, I, M, N, arr[101];
int ac[101][257];
int main() {
	freopen("small.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &T);
	while(T--) {
		scanf("%d %d %d %d", &D, &I, &M, &N);
		for(int i = 0; i < N; ++i) scanf("%d", &arr[i]);
		ac[0][256] = D;
		for(int i = 0; i < 256; ++i) {
			ac[0][i] = abs(i - arr[0]);
		}
		for(int i = 1; i < N; ++i) {
			for(int j = 0; j < 257; ++j) {
				ac[i][j] = ac[i - 1][j] + D;
			}
			for(int j = 0; j < 256; ++j) {
				//变为这个值是相差
				int sub = abs(arr[i] - j);
				for(int k = 0; k < 256; ++k) {
					//插入一群值
					if(M != 0) {
						int tmp = abs(k - j);
						int t2 = tmp / M;
						if(tmp % M == 0 && tmp > 0)
							--t2;
						int insert = t2 * I;

						ac[i][j] = min(ac[i][j], ac[i-1][k] + sub + insert);
					} else {
						ac[i][j] = min(ac[i][j], ac[i - 1][j] + abs(k - j) + sub);
					}
				}
			}

		}
		int ans = 1000000000;
		for(int i = 0; i < 257; ++i) {
			ans = min(ans, ac[N - 1][i]);
		}
		printf("Case #%d: %d\n", CT++, ans);
		
	}
	return 0;
}