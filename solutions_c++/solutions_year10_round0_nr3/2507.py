#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <utility>
#include <queue>

using namespace std;

int tab[1001];

int main() {
	int T;
	cin >> T;
	long long R, k, N;
	for (int t = 0; t < T; t++) {
		cin >> R >> k >> N;
		vector<int> pass;
		long long tot = 0;
		for (int m = 0; m < N; m++) {
			long long val; cin >> val;
			pass.push_back(val);
			tot += val;
		}
		memset(tab,0,sizeof(tab));
		int cur = 0;
		int remain = R;
	//	cout << "number: " << number << "\n";
	//	cout << "rides: " << rides << "\n";
		//long long allow = R / rides;
		//long long remain = R % rides;
	//	cout << "allow: " << allow << "\n";
	//	cout << "remain: " << remain << "\n";
		//long long total = (allow * number);
		// last cycle = cycleEnd
		//cur = allow ? cycleEnd : 0;
		// again
		long long total = 0;
		while (remain > 0) {
			int rem = k;
		//	cout << "New ride\n";
			int c = 0;
			while (rem > 0 && c < N) {
				if (rem - pass[cur] < 0) break;
				rem -= pass[cur];
				total += pass[cur];
				//cout << "using: " << cur << "\n";
				cur = (cur+1)%pass.size();
				c++;
			}
			remain--;
		}
		cout << "Case #" << (t+1) << ": " << total << "\n";
	}
	return 0;
}