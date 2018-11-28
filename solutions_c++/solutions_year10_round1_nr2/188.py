#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <list>
#include <set>
#include <map>
using namespace std;

#define PB push_back
#define MP make_pair
#define FI first
#define SE second
#define CLEAR(a,v) memset((a), (v), sizeof(a))

const double eps = 1e-9;
const int INF = 1000000000;
const long long LLINF = (long long)INF * INF;
const double PI = 2 * acos(.0);

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int,int> PII;

#define ABS(x) ((x)>0?(x):(-(x)))

int a[128];
int dp[128][260];

int main() {
	freopen("b-large.in","r",stdin);
	freopen("b-large.out","w",stdout);
	int T, ca, D, I, M, N;
	scanf("%d",&T);
	for (ca = 1 ; ca <= T ; ++ca) {
		int i;
		scanf("%d%d%d%d",&D,&I,&M,&N);
		for (i = 0 ; i < N ; i++)
			scanf("%d",&a[i]);
		CLEAR(dp, 0x3f);
		for (i = 0 ; i <= 255 ; i++)
			dp[0][i] = ABS(a[0] - i);
		int j, tj, ins, cost;
		for (i = 0 ; i < N - 1 ; i++)
			for (j = 0 ; j <= 255 ; j++) {
				dp[i+1][j] <?= ABS(a[i+1] - j) + D * (i+1);
				//if (dp[i][j] >= INF) continue;
				dp[i+1][j] <?= dp[i][j] + D;
				for (tj = 0 ; tj <= 255 ; tj++) {
					if (tj == j) ins = 0;
					else if (M != 0) ins = (ABS(tj - j) - 1) / M * I;
					else continue;
					cost = ins + ABS(tj - a[i+1]);
					dp[i+1][tj] <?= dp[i][j] + cost;

					cost = ins + D + I;
					dp[i+1][tj] <?= dp[i][j] + cost;
				}
			}
		/*
		for (i = 0 ; i < N ; i++)
			for (j = 0 ; j <= 255 ; j++)
				if (dp[i][j] <= 5) printf("dp[%d][%d]:%d\n",i,j,dp[i][j]);
		*/
		int best = D * N;
		for (j = 0 ; j <= 255 ; j++)
			best <?= dp[N-1][j];
		printf("Case #%d: %d\n",ca,best);
	}
	return 0;
}
