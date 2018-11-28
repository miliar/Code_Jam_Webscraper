#include <iostream>
#include <vector>
#include <string>

using namespace std;


const int oo = 10000000, MAX_N = 70000;
int dp[MAX_N][2];

struct Node {
	int internal;
	int gate;
	int change;
	int val;
} node[MAX_N];


inline int min(int a, int b) {
	if (a <= b) return a;
	return b;
}


int best(int pos, int req) {
	if (!node[pos].internal) {
		if (req == node[pos].val) return 0;
		else					  return oo;
	}

	int &rf = dp[pos][req];
	if (rf != -1) return rf;

	rf = oo;

	for (int lt = 0; lt < 2; lt++) {
		for (int rt = 0; rt < 2; rt++) {
			int cur = node[pos].gate;
			
			if (cur == 1 && (lt & rt) == req)
				rf = min(rf, best(2 * pos + 1, lt) + best(2 * pos + 2, rt));
			if (cur == 0 && (lt | rt) == req)
				rf = min(rf, best(2 * pos + 1, lt) + best(2 * pos + 2, rt));
		}
	}

	if (node[pos].change) {
		for (int lt = 0; lt < 2; lt++) {
			for (int rt = 0; rt < 2; rt++) {
				int cur = 1 - node[pos].gate;
			
				if (cur == 1 && (lt & rt) == req)
					rf = min(rf, 1 + best(2 * pos + 1, lt) + best(2 * pos + 2, rt));
				if (cur == 0 && (lt | rt) == req)
					rf = min(rf, 1 + best(2 * pos + 1, lt) + best(2 * pos + 2, rt));
			}
		}
	}

	return rf;
}


int main() {
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		int M, V;
		cin >> M >> V;

		int lmt = (M - 1) / 2;
		for (int i = 0; i < lmt; i++) {
			int a, b;
			cin >> a >> b;
			node[i].internal = 1;
			node[i].gate = a;
			node[i].change = b;
		}

		int lmt2 = (M + 1) / 2;
		for (int i = lmt, c = 0; c < lmt2; i++, c++) {
			int value;
			cin >> value;
			node[i].internal = 0;
			node[i].val = value;
		}

		memset(dp, -1, sizeof(dp));

		int ret = best(0, V);

		cout << "Case #" << t << ": ";
		if (ret == oo) cout << "IMPOSSIBLE" << endl;
		else			cout << ret << endl;
	}
}




