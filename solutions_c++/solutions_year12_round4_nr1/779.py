#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 2000000000;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
    
	int T;
	cin >> T;
	for(int t = 1; t <= T; ++t) {
		int n, D;
		cin >> n;
		vector <int> d(n), l(n);
		vector <int> ans(n, INF);
		for(int i = 0; i < n; ++i)
			cin >> d[i] >> l[i];
		cin >> D;
		ans[0] = 0;
		bool found = false;
		if(D <= d[0] + min(d[0] - ans[0], l[0])) {
			cout << "Case #" << t << ": YES" << endl;
			found = true;
		}
		for(int i = 0; i < n - 1 && !found; ++i) {
			for(int j = i + 1; j < n && d[j] <= d[i] + min(d[i] - ans[i], l[i]) && !found; ++j)
				if(ans[j] == INF) {
					ans[j] = d[i];
					if(D <= d[j] + min(d[j] - ans[j], l[j])) {
						cout << "Case #" << t << ": YES" << endl;
						found = true;
					}
				}
		}
		if(!found)
			cout << "Case #" << t << ": NO" << endl;
	}
	
    return 0;
}