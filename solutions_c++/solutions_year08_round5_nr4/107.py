#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define beg 10000000
#define pb push_back
#define mp make_pair
#define sz size()
#define iss istringstream
#define oss ostringstream
#define pf pop_front()
#define nd second
#define st first
#define fr(i, n) for(int i = 0; i < (int)n; i++)
#define LL long long
#define vi vector<int>
#define pii pair<int, int>
#define vs vector<string>

using namespace std;

int dp[110][110];
int dx[] = {2, 1};
int dy[] = {1, 2};
int mod = 10007;
bool M[110][110];

void solveCase(int Case) {
	memset(dp, 0, sizeof(dp));
	memset(M, true, sizeof(M));
	dp[1][1] = 1;
	int H, W;
	cin >> H >> W;
	int R;
	cin >> R;
	fr(i, R) {
		int x, y;
		cin >> x >> y;
		M[x][y] = false;
	}
	for(int sum = 2; sum <= H + W; sum++) {
		for(int x = 1; x <= H; x++) {
			int y = sum - x;
			if(y >= 1 && y <= W) if(M[x][y]) {
				fr(k, 2) {
					int xn = x + dx[k], yn = y + dy[k];
					if(xn >= 1 && xn <= H && yn >= 1 && yn <= W) if(M[xn][yn]) {
						dp[xn][yn] += dp[x][y];
						dp[xn][yn] %= mod;
					}
				}
			}
		}
	}
	cout << "Case #" << Case << ": " << dp[H][W] << endl;	
}

int main() {
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int tests;
	cin >> tests;
	for(int test = 1; test <= tests; test++) solveCase(test);	
	return 0;
}
