#pragma comment (linker, "/STACK:64000000")
#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <sstream>
#include <iostream>
#include <queue>
#include <set>
#include <map>

#define ABS(x) ((x)<0?-(x):(x))
#define SQR(x) ((x)*(x))
#define PB push_back
#define MP make_pair
#define SS stringstream
#define LL long long
#define LD long double
#define SZ(x) int(x.size())
#define ALL(x) x.begin(),x.end()
#define FOR(a,b) for(int a=0;a<b;a++)
#define DFOR(a,b) for(int a=b-1;a>=0;a--)
#define CLR(a,b) memset(a,b,sizeof(a))

using namespace std;

#define maxn 505
#define mod 10000

char s[maxn];
char *t = "welcome to code jam";
int n, m;
int dp[maxn][50];

void solvecase() {
	gets(s);
	n = strlen(s);
	m = strlen(t);
	for (int i = 0; i <= n; i++) dp[i][0] = 1;
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= m; j++)
		{
			if (s[i-1] == t[j-1])
				dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % mod;
			else
				dp[i][j] = dp[i-1][j];
		}
	printf("%04d", dp[n][m]);
}

void solve() {
	int n;
	scanf("%d\n", &n);
	FOR(i, n) {
		printf("Case #%d: ", i+1);
		solvecase();
		printf("\n");
	}
}

int main() {
	freopen("y", "rt", stdin);
	//freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	solve();
	return 0;
}