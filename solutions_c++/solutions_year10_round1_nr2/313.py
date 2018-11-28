#include <cstdio>
#include <algorithm>

using namespace std;

const int INF = (1<<28);
const int MAXN = 100+5;


int D, I, M, N;

int t[MAXN];
int memo[MAXN][256][261];

int f(int n, int last, int len) {
	int &result = memo[n][last][len];


	if(result != -1) return result;
	result = INF;

	if(len >= 260) result = INF;
	else if(n == 0) result = 0;
	else {

		result = min(result, D+f(n-1, last, 0));
		for(int i = max(0, last-M); i <= min(last+M, 255); i++) {
			result = min(result, I+f(n, i, len+1));
			result = min(result, abs(t[n]-last) + f(n-1, i, 0));
		}
	}
	return result;
}

int solve() {
	scanf("%d %d %d %d", &D, &I, &M, &N);
	for(int i = 1; i <= N; i++) scanf("%d", &t[i]);

	memset(memo, -1, sizeof(memo));

	int result = INF;
	for(int i = 0; i <= 255; i++) result = min(result, f(N, i, 0));
	return result;
}


int main() {
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++) printf("Case #%d: %d\n", i, solve()); 

}