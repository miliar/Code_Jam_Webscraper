
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <stack>
#include <queue>
#include <map>

using namespace std;

int memo[111][111];

vector<int> data;
int leftMost, rightMost;

int func(int leftIdx, int rightIdx) {
	if (rightIdx - leftIdx < 2) {
		return 0;
	}
	if (memo[leftIdx][rightIdx] != -1) return memo[leftIdx][rightIdx];
	int res = 1<<30;
	for (int i = leftIdx+1; i < rightIdx; i++) {
		// split on index i
		int calc = (data[i] - data[leftIdx] - 1) + (data[rightIdx] - data[i] - 1);
		calc = calc + func(leftIdx, i) + func(i, rightIdx);
		res = min(res,calc);
	}
	return memo[leftIdx][rightIdx] = res;
}

int main() {
	int N;
	cin >> N;
	for (int t = 0; t < N; t++) {
		int P, Q; cin >> P >> Q;
		vector<int> pris;
		for (int i = 0; i < Q; i++) {
			int val; cin >> val; pris.push_back(val);
		}
		pris.push_back(0);
		pris.push_back(P+1);
		sort(pris.begin(),pris.end());
		data = pris;
		memset(memo,-1,sizeof(memo));
		leftMost = 0;
		rightMost = data.size()-1;
		int best = func(0, data.size()-1);
		cout << "Case #" << t+1 << ": " << best << "\n";
	}
	return 0;
}
