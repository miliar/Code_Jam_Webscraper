#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <queue>
using namespace std;

int main() {
	freopen("inputC.txt", "r", stdin);
	freopen("C-small.out", "w", stdout);

	int t;
	cin >> t;
	for (int e=1; e<=t; e++) {
		int r,n,k;
		cin >> r >> k >> n;

		cout << "Case #" << e << ": ";
		long long ans = 0;

		queue<int> q;
		for (int i=0; i<n; i++) {
			int x;
			cin >> x;
			q.push(x);
		}

		for (int i=0; i<r; i++) {
			int cur = 0;
			queue<int> q2;
			while (!q.empty() && cur + q.front() <= k) {
				int person = q.front();
				cur += person;
				q.pop();
				q2.push(person);
			}
			ans += cur;
			cur = 0;
			while (!q2.empty()) {
				q.push(q2.front());
				q2.pop();
			}
		}

		cout << ans << endl;


	}




	return 0;
}