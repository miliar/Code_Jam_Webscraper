// Adrian Kügel
#include <stdio.h>
#include <vector>
#include <set>
#include <queue>
#include <math.h>
#include <stdlib.h>
#include <map>
#include <assert.h>
#include <limits.h>
#include <complex>
#include <algorithm>
#include <ctype.h>
#include <string>
using namespace std;

typedef set<int> SI;
typedef vector<int> VI;
typedef vector<string> VS;
typedef complex<double> tComp;

int dp[100][100];
const int mod = 10007;

void update(int &a, int b) {
	if (a < 0)
		return;
	a = (a+b)%mod;
}

int main() {
	int tc;
	scanf("%d", &tc);
	for (int scen=1; scen<=tc; ++scen) {
		printf("Case #%d: ", scen);
		int h, w, r;
		scanf("%d %d %d",&h,&w,&r);
		memset(dp, 0, sizeof(dp));
		for (int i=0; i<r; ++i) {
			int x, y;
			scanf("%d %d", &x, &y);
			dp[x-1][y-1] = -1;
		}
		dp[0][0] = 1;
		for (int i=0; i<h; ++i)
			for (int j=0; j<w; ++j) {
				if (dp[i][j] <= 0)
					continue;
				if (i+1<h && j+2<w)
					update(dp[i+1][j+2], dp[i][j]);
				if (i+2<h && j+1<w)
					update(dp[i+2][j+1], dp[i][j]);
			}
		printf("%d\n", dp[h-1][w-1]);
	}
	return 0;
}
