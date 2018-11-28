#include <iostream>
#include <queue>

using std::cin;
using std::cout;
using std::endl;
using std::queue;

int main()
{
	int t = 0;
	cin >> t;

	int num = 1;
	while (num <= t) {
		// Number of runs; Capacity of the roller; Number of groups
		int r = 0, k = 0, n = 0;
		cin >> r >> k >> n;

		// Groups
		queue<int> q;
		long long total = 0;
		for (int i = 0; i < n; i++) {
			int gi = 0;
			cin >> gi;
			q.push(gi);
			total += gi;
		}

		long long int euros = 0;

		// Each run
		for (int i = 0; i < r; i++) {
			int space = k;
			// Until you can't put anymore group
			while ((space >= q.front()) && (k-space+q.front() <= total)) {
				space -= q.front();
				q.push( q.front() );
				q.pop();
			}
			euros += (k-space);
		}

		cout << "Case #" << num << ": " << euros << endl;

		num++;
	}

	return 0;
}
