#include<cstdio>
#include<cstring>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include <list>
#include<queue>
#include <deque>
#include <stack>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
int main() {
	int N,H,W,R,a,b,dp[105][105];
	char chess[105][105];
	scanf("%d\n",&N);
	for(int ii = 1;ii <=N;++ii) {
		scanf("%d %d %d\n",&H,&W,&R);
		memset(chess,1,sizeof(chess));
		for(int i = 0;i <R ; ++i) {
			scanf("%d %d\n",&a,&b);
			chess[a][b] = 0;
		}
		memset(dp,0,sizeof(dp));
		dp[1][1] = 1;
		for(int i = 1;i <= H;++i) for(int j =1;j<=W;++j) {
			if(i == 1 || j == 1) continue;
			if(chess[i][j] != 0) dp[i][j] = (dp[i-1][j-2] + dp[i-2][j-1]) % 10007;
		}
		printf("Case #%d: %d\n",ii,dp[H][W]);
	}
	return 0;
}
