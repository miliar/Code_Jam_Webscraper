#include <algorithm>
#include <iostream>
#include <utility>
#include <vector>
using namespace std;

int main()
{
	ios::sync_with_stdio(false);

	int testCases, n, val, result;
	vector<pair<int, int> > num;
	cin >> testCases;
	for (int t = 1; t <= testCases; ++ t) {
		cin >> n;
		num.clear();
		for (int i = 0; i < n; ++ i) {
			cin >> val;
			num.push_back(make_pair(val, i));
		}
		sort(num.begin(), num.end());
		result = n;
		for (int i = 0; i < n; ++ i)
			result -= num[i].second == i;
		cout << "Case #" << t << ": " << result << endl;
	}
	return 0;
}
