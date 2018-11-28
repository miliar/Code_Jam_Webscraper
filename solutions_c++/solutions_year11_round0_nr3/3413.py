#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


long long solve(const vector <long long> &v) {
	long long r = 0;
	for (int i = 0; i < v.size(); i++)
		r ^= v[i];
	long long sum = 0;
	for (int i = 0; i < v.size(); i++)
		sum += v[i];
	if (r == 0)
		return sum - *min_element(v.begin(), v.end());
	else
		return 0;
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int t = 0;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		int n;
		cin >> n;
		vector<long long> v(n);
		for (int j = 0; j < n; j++)
			cin >> v[j];
		long long r = solve(v);
		printf("Case #%d: ", i + 1);
		if (r == 0)
			cout << "NO";
		else
			cout << r;
		printf("\n");
	}
}