#include <iostream>
#include <algorithm>
#include <string>
#include <sstream>
#include <vector>
#include <queue>
#include <cmath>
#include <utility>
#include <cassert>

using namespace std;

vector<int> eval;
int sz;
int memo[51];

int func(int node) {
	//if (memo[node] != -1) return memo[node];
	if (node > (sz-1)/2) {
		return eval[node-1];
	}
	if (eval[node-1] == 0) {
		return func(node*2) | func(node*2+1);
	}
	return func(node*2) & func(node*2+1);
}

int main() {
	int N;
	cin >> N;
	for (int i = 0; i < N; i++) {
		int M, V;
		cin >> M >> V;
		vector<int> vec;
		vector<int> changable;
		for (int j = 0; j < (M-1)/2; j++) {
			int G, C; cin >> G >> C;
			vec.push_back(G);
			if (C) {
				changable.push_back(j);
			}
		}
		for (int j = 0; j < (M+1)/2; j++) {
			int I; cin >> I;
			vec.push_back(I);
		}
		int numChange = changable.size();
		vector<int> orig = vec;
		sz = M;
		int cnt = 99999;
		for (int j = 0; j < (1 << numChange); j++) {
			vec = orig;
			memset(memo,-1,sizeof(memo));
			for (int m = 0; m < numChange; m++) {
				if ((1 << m) & j) {
					// change it
					//cout << "Change!\n";
					vec[changable[m]] = 1 - vec[changable[m]];
				}
			}
			//cout << "PRINT\n";
			//for (int m = 0; m < vec.size(); m++) cout << vec[m] << " ";
			//cout << "\n";
			// evaluate
			eval = vec;
			//cout << "Case: " << j << "\n";
			int ans = func(1);
			//cout << "Ans: " << ans << "\n";
			if (ans == V) {
				int c = 0;
				int m = j; while (m > 0) { c += (m % 2); m /= 2; }
				cnt = min(cnt, c);
			}
		}
		if (cnt >= 99999) {
			cout << "Case #" << i+1 << ": IMPOSSIBLE\n";
		} else {
			cout << "Case #" << i+1 << ": " << cnt << "\n";
		}
	}
	return 0;
}