#include <iostream>
#include <cstdlib>
#include <string>

using namespace std;


const int MAX_S = (1 << 10) + 7, MAX_N = 12;
string row[MAX_N];
int M, N;
int memoOk[MAX_S][MAX_S];
int memoGood[MAX_S][MAX_S];
int memoCount[MAX_S];
int dp[MAX_N][MAX_S];


inline int ok(int down, int up) {
	//int &rf = memoOk[down][up];
	//if (rf != -1) return rf;

	for (int i = 0; i < N; i++) if (down & (1 << i)) {
		if (i < N - 1 && (up & (1 << (i + 1)))) return 0;
		if (i > 0 && (up & (1 << (i - 1)))) return 0;
	}

	return 1;
}		


inline int good(int r, int state) {
	//int &rf = memoGood[r][state];
	//if (rf != -1) return rf;
	
	for (int i = 0; i < N; i++) if (state & (1 << i)) {
		if (row[r][i] == 'x') return 0;
		if (i > 0 && (state & (1 << (i - 1)))) return 0;
		if (i < N - 1 && (state & (1 << (i + 1)))) return 0;
	}

	return 1;
}
		


inline int countBits(int num) {
	//int &rf = memoCount[num];
	//if (rf != -1) return rf;

	int ret = 0;
	while (num > 0) {
		if (num & 1) ret++;
		num >>= 1;
	}
	//return rf = ret;
	return ret;
}


inline int max(int a, int b) {
	return (a > b)? a: b;
}


int memo(int cur, int up) {
	if (cur == M) return 0;

	int &rf = dp[cur][up];
	if (rf != -1) return rf;

	rf = 0;

	for (int state = 0; state < (1 << N); state++) {
		if (good(cur, state) && ok(state, up)) {
			int bits = countBits(state);
			rf = max(rf, bits + memo(cur + 1, state));
		}
	}

	return rf;
}


int main() {
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		cin >> M >> N;

		for (int i = 0; i < M; i++) {
			cin >> row[i];
		}

		//for (int i = 0; i < M; i++) 
		//	cout << row[i] << endl;
		//}

		memset(dp, -1, sizeof(dp));
		memset(memoOk, -1, sizeof(dp));
		memset(memoGood, -1, sizeof(dp));
		memset(memoCount, -1, sizeof(memoCount));
		int ret = memo(0, 0);

		cout << "Case #" << t << ": " << ret << endl;
	}

	return 0;
}




