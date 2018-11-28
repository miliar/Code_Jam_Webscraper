#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
#include <cmath>
#include <map>
#include <set>
#include <cctype>
#include <iostream>
#include <sstream>
using namespace std;

char str[555];
int maze[555][555];
int X[555][555] , Y[555][555];
long long sumX[555][555] , sumY[555][555] , sum[555][555];
int n , m , d;


int main() {
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int cas = 1 ; cas <= T ; cas ++) {
		scanf("%d%d%d",&n,&m,&d);
		for (int i = 1 ; i <= n ; i ++) {
			scanf("%s",str);
			for (int j = 1 ; j <= m ; j ++) {
				maze[i][j] = d + str[j - 1] - '0';
				X[i][j] = i * maze[i][j];
				Y[i][j] = j * maze[i][j];
				sumX[i][j] = sumX[i][j-1] + sumX[i-1][j] - sumX[i-1][j-1] + X[i][j];
				sumY[i][j] = sumY[i][j-1] + sumY[i-1][j] - sumY[i-1][j-1] + Y[i][j];
				sum[i][j] = sum[i][j-1] + sum[i-1][j] - sum[i-1][j-1] + maze[i][j];
			}
		}

		int limitk = min(n , m);
		int ans = -1;
		for (int K = 3 ; K <= limitk ; K ++) {
			for (int x = K ; x <= n ; x ++) {
				for (int y = K ; y <= n ; y ++) {
					long long totx = sumX[x][y] - sumX[x-K][y] - sumX[x][y-K] + sumX[x-K][y-K];
					totx -= X[x][y] + X[x][y-K+1] + X[x-K+1][y] + X[x-K+1][y-K+1];
					
					long long toty = sumY[x][y] - sumY[x-K][y] - sumY[x][y-K] + sumY[x-K][y-K];
					toty -= Y[x][y] + Y[x][y-K+1] + Y[x-K+1][y] + Y[x-K+1][y-K+1];

					long long tot = sum[x][y] - sum[x-K][y] - sum[x][y-K] + sum[x-K][y-K];
					tot -= maze[x][y] + maze[x][y-K+1] + maze[x-K+1][y] + maze[x-K+1][y-K+1];

					if (totx * 2 == tot * (x + x - K + 1) && 
						toty * 2 == tot * (y + y - K + 1)) {
							ans = K;
							break;
					}
				}
				if (ans == K) break;
			}
		}
		printf("Case #%d: ",cas);
		if (ans == -1) puts("IMPOSSIBLE");
		else printf("%d\n",ans);
	}
	return 0;
}