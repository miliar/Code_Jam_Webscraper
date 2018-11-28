#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>


using namespace std;
const int N = 110;
const int INF = 0x7fffffff;

int dp[N][N][N]; // the second means Orange, and third means Blue.

struct	node {
	int index;
	char type[2];
}seq[N];

void scaf(int &n) {
	scanf("%d", &n);

	for (int i = 0; i < n; i ++) {
		scanf("%s%d", seq[i].type, &seq[i].index);
	}
}

void initDp(int n) {

	for (int i = 0; i <= n; i ++) {
		for (int j = 0; j <= 100; j ++) {
			for (int k = 0; k <= 100; k ++) {
				dp[i][j][k] = INF;
			}
		}
	}

	dp[0][1][1] = 0;
}

int getMinTime(int n) {
	//initDp(n);

	int totalTime = 0;
	int BTime = 0;
	int OTime = 0;
	int BIndex = 1;
	int OIndex = 1;
	int diff;

	for (int i = 0; i < n; i ++) {
		if (seq[i].type[0] == 'O') {
			diff = OTime - abs(seq[i].index - OIndex);
			if (diff >= 0) {
				totalTime ++;
				BTime ++; 
			}
			else {
				diff = abs(diff);
				totalTime += diff + 1;
				BTime += diff + 1;
			}
			OTime = 0;
			OIndex = seq[i].index;
		}
		else {
			diff = BTime - abs(seq[i].index - BIndex);
			if (diff >= 0) {
				totalTime ++;
				OTime ++;
			}
			else {
				diff = abs(diff);
				totalTime += diff + 1;
				OTime += diff + 1;
			}
			BTime = 0;
			BIndex = seq[i].index;
		}
	}

	return totalTime;
	/*
	for (int i = 0; i < n; i ++) {
		for (int j = 0; j <= 100; j ++) {
			for (int k = 0; k <= 100; k ++) {
				if (dp[i][j][k] == INF) 
					continue;

				next = i + 1;
				if (seq[i].type[0] == 'O') {
					time = abs(seq[i].index - j) + 1;
					totalTime = time + dp[i][j][k];
					start = max(1, k - time);
					end = min(100, k + time);

					for (int l = start; l <= end; l ++) 
						dp[next][seq[i].index][l] = min(dp[next][seq[i].index][l], 
				}
				else {
				
				}
			}
		}
	}
	*/
}
int main() {
	//freopen("Lin.txt", "r", stdin);
	//freopen("Lout.txt", "w", stdout);
	int t, n;
	scanf("%d%*c", &t);

	for (int cas = 1; cas <= t; cas ++) {
		scaf(n);

		printf("Case #%d: %d\n", cas, getMinTime(n));
	}
	return 0;
}