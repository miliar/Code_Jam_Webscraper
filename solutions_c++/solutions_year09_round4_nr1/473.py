#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <list>
#include <map>
#include <string>
#include <vector>

using namespace std;

void Solve() {
	int N;
	cin >> N;
	string s;
	vector<int> M;
	for(int i = 0; i < N; ++i) {
		cin >> s;
		int l = 0;
		for(int j = 0; j < N; ++j) {
			if (s[j] == '1') {
				l = j;
			}
		}
		M.push_back(l);
	}
	int Answer = 0;
	for(int i = 0; i < N; ++i) {
		int j = i;
		while (M[j] > i) {
			++j;
		}
		for(int k = j; k > i; --k) {
			swap(M[k], M[k - 1]);
			++Answer;
		}
	}
	cout << Answer << endl;
}

void Init() {
	int T;
	cin >> T;
	for(int i = 0; i < T; ++i) {
		cout << "Case #" << i + 1 << ": ";
		Solve();
	}
}

int main() {
	Init();
	return 0;
}
