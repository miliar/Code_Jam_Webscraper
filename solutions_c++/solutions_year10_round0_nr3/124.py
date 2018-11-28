#include <cstdio>
#include <cmath>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <numeric>

using namespace std;

long long ThemePark(int R, int K, vector <int> g)
{
	vector <int> head;
	vector <long long> num;
	int index = 0;
	int loop = -1;
	while (1) {
		if (find(head.begin(), head.end(), index) != head.end()) {
			loop = distance(head.begin(), find(head.begin(), head.end(), index));
			break;
		}
		int start = index;
		long long count = 0;
		if (count + g[index] <= K) do {
			count += g[index];
			index = (index + 1) % g.size();
		} while (count + g[index] <= K && start != index);
		head.push_back(start);
		num.push_back(count);
	}

	long long ret = 0;
	int t = (R - loop) / (num.size() - loop);
	if (t > 0) {
		// printf("%d %d %d %I64d\n", head.size(), loop, t, accumulate(num.begin() + loop, num.end(), 0LL));
		ret += t * accumulate(num.begin() + loop, num.end(), 0LL);
		R -= t * (num.size() - loop);
	}
	for (int i = 0; i < R; i++) {
		ret += num[i % num.size()];
	}
	return ret;
}


int main()
{
	string line;

	int cases;
	cin >> cases;
	getline(cin, line);

	for (int caseno = 1; caseno <= cases; caseno++) {
		int R, k, n;
		cin >> R >> k >> n;
		vector <int> g(n);
		for (int i = 0; i < n; i++) {
			cin >> g[i];
		}

		long long ret = ThemePark(R, k, g);

		cout << "Case #" << caseno << ": " << ret << endl;
	}

	return 0;
}
