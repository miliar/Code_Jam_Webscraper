#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <utility>
#include <queue>
#include <set>
#include <sstream>
#include <map>

using namespace std;

int avail[26];
int next[26];
int best[26];

int main() {
	
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		int n;
	//for (int n = 2; n <= 25; n++) {
		cin >> n;
		vector<int> vec;
		for (int i = 2; i <= n; i++) vec.push_back(i);
		int tot = 0;
		for (int i = 1; i < (1 << vec.size()); i++) {
			//map<int,int> data;
			memset(avail,-1,sizeof(avail));
			int pos = 1;
			for (int j = 0; j < vec.size(); j++) {
				if (i & (1 << j)) { avail[vec[j]] = pos++; } //data[vec[j]] = pos++; }
			}
			//int idx = data[n];
			int idx = avail[n];
			bool ok = true;
			//for (int i = 0; i < 26; i++) if (avail[i]) cout << i << ",";
				//cout << "\n";
			if (idx <= 0) ok = false;
			while (idx > 1) {
				//cout << "idx: " << idx << "\n";
				idx = avail[idx];
				if (idx <= 0) { ok = false; break; }
			}
			//if (idx == 1) cout << "idx: " << idx << "\n";
			if (ok && idx == 1) {
				//for (int i = 0; i < 26; i++) if (avail[i]) cout << i << ",";
				//cout << "\n";
				tot++;
			}
		}
		best[n] = tot;
		cout << "Case #" << (t+1) << ": " << best[n]%100003 << "\n";
	}
	/*
	cout << "{";
	for (int i = 2; i <= 25; i++) cout << best[i] << ",";
	cout << "}";
	*/
	/*
	best[0] = 1; best[1] = 2;
	for (int n = 2; n < 26; n++) best[n] = best[n-1] + best[n-2];
	for (int t = 0; t < T; t++) {
		int n; cin >> n;
		cout << "Case #" << (t+1) << ": " << best[n-2] << "\n";
	}
	*/
	return 0;
}
