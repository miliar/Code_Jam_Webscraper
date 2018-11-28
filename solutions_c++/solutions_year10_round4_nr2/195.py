#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define PB push_back
#define MP make_pair

#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;
const int maxn = 5000;
/*int M[2000];
int sum[100];
int pp[10][1054];*/
int M[maxn],pp[maxn];
int dp[maxn][15],p;
int sum[100];
int b = 1;
void dfs(int low,int high,int now)
{
	if(low + 1== high) {
		dp[now][M[now%sum[p]]]=0;
		return ;
	}
	int mid = (low + high )/2;
	dfs(low, mid, now*2);
	dfs(mid, high, now*2+1);
	for(int i = 0;i <= p; ++i) {
		for(int j = 0;j <= p; ++j) {
			dp[now][max(i,j)]=min(dp[now][max(i,j)],dp[2*now][i]+dp[2*now+1][j]);
		}
	}
	for(int i=0;i < p;i++) {
		dp[now][i]=min(dp[now][i],dp[now][i+1] + pp[now]);
	}
}

inline void solve() {
	scanf("%d", &p);
	fill(&dp[0][0], &dp[maxn][0], 20000000);
	for (int i = 0; i < sum[p]; ++i) {
		scanf("%d", M + i);
	}
	for(int i = sum[p]-1;i > 0; --i) {
		scanf("%d", pp + i);
	}
	dfs(0,sum[p], 1);
	printf("Case #%d: ", b);
	++b;
	printf("%d\n", dp[1][0]);
};

int main()
{
	int T;
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	sum[0] = 1;
	for (int i = 1; i < 32; ++i) {
		sum[i] = sum[i-1] * 2;
	}
	scanf("%d",&T);
	while (T--) {
		solve();
	}
}