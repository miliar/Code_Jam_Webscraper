#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <list>
#include <map>
#include <string>
#include <vector>

#define INFINITY 100000

using namespace std;

int G[16][16];

bool Check(int i) {
	for(int j = 0; j <= 16; ++j) {
		if (((1 << j) & i) == 0) {
			continue;
		}
		for(int k = j + 1; k <= 16; ++k) {
			if (((1 << k) & i) == 0) {
				continue;
			}
			if (!G[j][k]) {
				//cout << j << " " << k << endl;
				return false;
			}
		}
	}
	return true;
}

void Solve() {
	int N, K;
	vector< vector <int> > price;
	cin >> N >> K;
	for(int i = 0; i < N; ++i) {
		vector<int> p;
		for(int j = 0; j < K; ++j) {
			int a;
			cin >> a;
			p.push_back(a);
		}
		price.push_back(p);
	}
	for(int i = 0; i < N; ++i) {
		G[i][i] = 1;
		for(int j = i + 1; j < N; ++j) {
			int ok = 1;
			if (price[i][0] == price[j][0]) {
				ok = 0;
			}
			for(int k = 1; k < K; ++k) {
				if (price[i][k] == price[j][k] ||
						(price[i][k - 1] <= price[j][k - 1] && price[i][k] >= price[j][k]) ||
						(price[i][k - 1] >= price[j][k - 1] && price[i][k] <= price[j][k])) {
						ok = 0;
						break;
					}
			}
			G[j][i] = G[i][j] = ok;
		}
	}
	vector<int> Answer(1 << N);
	vector<bool> Ok(1 << N);
	Answer[0] = 0;
	for(int i = 1; i < (1 << N); ++i) {
		Answer[i] = INFINITY;
		Ok[i] = Check(i);
		for(int j = 0; j < i; ++j) {
			if ((j | i) > i) {
				continue;
			}
			if (Ok[i ^ j]) {
				//cout << i << " " << j << endl << Answer[j] + 1;
				Answer[i] = min(Answer[i], Answer[j] + 1);
			}
		}
		//cout << i << " " << Answer[i] << " " << Ok[i] << endl;
	}
	cout << Answer[(1 << N) - 1] << endl;
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
