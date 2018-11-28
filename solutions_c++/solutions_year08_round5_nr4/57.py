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
#define mod 10007

using namespace std;

int h, w, n;
int dp[101][101];
int badx[11], bady[11];
bool bad[101][101];

int get(int i, int j) {
	if (i < 0 || j < 0) return 0;
	return dp[i][j];
}

void solvecase() {
	scanf("%d%d%d", &h, &w, &n);
	CLR(bad, 0);
	FOR(i, n) {
		scanf("%d%d", &badx[i], &bady[i]);
		badx[i]--; bady[i]--;
		bad[badx[i]][bady[i]] = true;
	}
	dp[0][0] = 1;
	for (int i = 1; i < h; i++)
		for (int j = 1; j < w; j++) {
			if (bad[i][j]) {
				dp[i][j] = 0;
			} else {
				dp[i][j] = (get(i-1,j-2) + get(i-2, j-1)) % mod;
			}
		}
	printf("%d", dp[h-1][w-1]);
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
	freopen("x", "rt", stdin);
	//freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	solve();
	return 0;
}