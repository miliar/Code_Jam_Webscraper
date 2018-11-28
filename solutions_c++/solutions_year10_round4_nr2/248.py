#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>
#include <sstream>
#include <algorithm>
#include <stack>

#define INF 1000000000
#define EPS 1E-8
#define PI 3.14159265358979

using namespace std;

typedef long long ll;

int m[1050];
int tic[1050];
int dp[1050][1050];
int used[1050][1050];

ll go(int pos, int num, int t, int p) {
	if(pos >= (1 << p)) {
		if(num < m[pos - (1 << p)]) return INF;
		return 0;
	}
	if(used[pos][num] == t + 1) return dp[pos][num];
	int res = INF;
	for(int i = 0; i < 2; ++i) {
		res = min((ll)res, go(pos * 2, num + i, t, p) + go(pos * 2 + 1, num + i, t, p) + tic[pos] * i);
	}
	used[pos][num] = t + 1;
	return dp[pos][num] = res;
}

int main() {
	int N;
	cin >> N;
	for(int t = 0; t < N; ++t) {
		printf("Case #%d: ", t + 1);
		int p;
		cin >> p;
		for(int i = 0; i < (1 << p); ++i) {
			cin >> m[(1 << p) - i - 1];
			m[(1 << p) - i - 1] = p - m[(1 << p) - i - 1];
		}
		for(int i = 0; i < (1 << p) - 1; ++i) {
			cin >> tic[(1 << p) - 1 - i];
		}
		cout << go(1, 0, t, p) << endl;
	}
	return 0;
}
