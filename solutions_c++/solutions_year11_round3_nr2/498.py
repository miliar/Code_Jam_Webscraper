#include <iostream>
#include <cmath>
#include <string>
#include <algorithm>
#include <fstream>
#include <climits>
using namespace std;

int city[1000000];

int main() {
	ifstream cin("B-small.in");
	ofstream cout("B-small.out");
	int T;
	cin >> T;
	for (int cc = 1; cc <= T; cc++) {
		int L, N, C;
		long long t;
		cin >> L >> t >> N >> C;
		for (int i = 0; i < C; i++) {
			int a;
			cin >> a;
			for (int k = 0; k*C+i < N; k++)
				city[k*C+i] = 2*a;
		}
		cout << "Case #" << cc << ": ";
		if (L == 0) {
			int res = 0;
			for (int i = 0; i < N; i++)
				res += city[i];
			cout << res << endl;
		} else {
			double bst = INT_MAX;
			int reach = 0;
			for (int i = 0; i < N; i++) {
				double nxt = reach + city[i];
				if (nxt > t) {
					nxt -= min((nxt-t), 1.0*city[i])/2;
				}
				double mx = 0;
				for (int j = i+1; j < N; j++) {
					nxt += city[j];
					if (nxt > t) {
						mx = max(mx, min(nxt-t, 1.0*city[j]));
					}
				}
				if (L == 2)
					nxt -= mx/2;
				bst = min(bst, nxt);
				reach += city[i];
			}
			int res = bst*10;
			if (res%10 >= 5)
				res += 10;
			res /= 10;
			cout << res << endl;
		}
	}

	return 0;
}