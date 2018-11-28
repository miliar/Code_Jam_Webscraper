#include<vector>
#include<string>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<set>
#include<map>
#include<sstream>
#include<queue>
#include<climits>
#include<cmath>
using namespace std;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef unsigned long long ull;
typedef long long ll;
typedef long double ld;

int N;

string data[64];
int len[64];

int check() {
	for(int i = 0; (i+1) < N; ++i) {
		if(len[i] > (i + 1)) {
			return 1;
		}
	}
	return 0;
}

int find() {
	for(int i = 0; (i+1) < N; ++i) {
		// not just bigger than diagonal..
		// the next element must be smaller too
		if(len[i] > (i + 1)) {
			return i;
		}
	}
	return -1;
}

void debug() {
	for(int i = 0; i < N; ++i) {
		cout << len[i] << endl;
	}
	cout << endl;
}

int main() {
	int T; cin >> T;
	for(int tt = 1; tt <= T; ++tt) {
		cin >> N;
		for(int i = 0; i < N; ++i) {
			cin >> data[i];
			len[i] = 0;
			for(int j = 0; j < N; ++j) {
				if(data[i][j] == '1') len[i] = j + 1;
			}
		}
		int ans = 0;
		while(check()) {
			int a = find();
			int b = a + 1;
			while(len[b] > (a + 1)) b++;
			swap(len[b - 1], len[b]);
			++ans;
		}
		cout << "Case #" << tt << ": " << ans << endl;
	}
	return 0;
}

