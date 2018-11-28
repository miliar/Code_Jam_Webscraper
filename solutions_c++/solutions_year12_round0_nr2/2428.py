#include <cstdio>
#include <cassert>
#include <iostream>
using namespace std;

const int N = 100 + 10;
const int INF = 1 << 29;

int n, s, p;
int a[N], dp[2][N];

void read () {
	cin >> n >> s >> p;
	for (int i = 0; i < n; ++i) {
		cin >> a[i];
	}
}

class calc {
public:
	int score, *prev_value, i;
	int scores[3], total_score, cost;
	
	calc (int score, int *prev_value, int i): score(score), prev_value(prev_value), i(i) {
	}
	
	int gen (int x) {
		// cerr << x << endl;
		
		if (x == 3) {
			
			if (total_score == score) {
				/* for (int j = 0; j < 3; ++j) {
					cerr << scores[j] << " ";
				}
				cerr << endl;
				*/
				assert(scores[2] - scores[0] <= 2);
				int cost = (scores[2] >= p ? 1 : 0);
				if (scores[2] - scores[0] < 2) {
					return prev_value[i] + cost;
				}
				else {
					if (i == 0) {
						return -INF;
					}
					else {
						return prev_value[i - 1] + cost;
					}
				}
			}
			else {
				return -INF;
			}
		}
		
		int res = -INF;
		
		int from, to;
		if (x == 0) {
			from = 0, to = 10;
		}
		else {
			from = scores[x - 1], to = min(10, scores[0] + 2);
		}
		
		for (int j = from; j <= to; ++j) {
			total_score += j;
			scores[x] = j;
			res = max(res, gen(x + 1));
			total_score -= j;
		}
		return res;
	}
	
	int get_value () {
		total_score = 0;
		return gen(0);
	}
};

void solve (int test_number) {
	dp[0][0] = 0;
	for (int i = 1; i <= s; ++i) {
		dp[0][i] = -INF;
	}
	
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j <= s; ++j) {
			dp[1][j] = calc(a[i], dp[0], j).get_value();
			// cerr << i << " " << j << " " << dp[1][j] << endl;
		}
		swap(dp[0], dp[1]);
	}
	assert (dp[0][s] >= 0);
	printf("Case #%d: %d\n", test_number, dp[0][s]);
}

int main () {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	
	int i, t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		read();
		solve(i + 1);
	}
	return 0;
}