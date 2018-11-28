#include <iostream>
#include <cmath>
#include <string>
#include <algorithm>
using namespace std;
int main() {
	freopen("B-large.in", "r", stdin);
	freopen("bsmall.out", "w", stdout);
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		string N;
		cin >> N;
		bool done = false;
		for (int j = N.size() - 2; j >= 0; j--) {
			int minimax = 1000000000;
			int minimaxi = 0;
			for (int k = j + 1; k < N.size(); k++)
				if (N[k] - '0' > N[j] - '0' && N[k] - '0' < minimax)
					minimax = N[k] - '0', minimaxi = k;
			if (minimax == 1000000000)
				continue;
			char c = N[j];
			N[j] = N[minimaxi];
			N[minimaxi] = c;
			string s = N.substr(j + 1);
			string t = N.substr(0, j + 1);
			sort(s.begin(), s.end());
			N = t + s;
			done = true;
			break;
		}
		if (!done) {
			sort(N.begin(), N.end());
			N.insert(1, "0");
			if (N[0] == '0') {
				int j = 1;
				for (; j < N.size() - 1; j++)
					if (N[j] != '0')
						break;
				char c = N[j];
				N[j] = N[0];
				N[0] = c;
			}
		}
		cout << "Case #" << i + 1 << ": " << N << endl;
	}
}