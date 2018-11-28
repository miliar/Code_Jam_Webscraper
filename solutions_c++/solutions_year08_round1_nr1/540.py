#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n;
vector<long long> xs, ys;

long long calc(void)
{
	sort(xs.begin(), xs.end());
	sort(ys.begin(), ys.end());
	long long ans = 0;
	for (int i=0; i<n; ++i) {
		ans += xs[i]*ys[n-1-i];
	}
	return ans;
}

int main(void)
{
	int i, j;
	int T;
	cin >> T;
	for (i=1; i<=T; ++i) {
		cin >> n;
		xs.resize(n);
		ys.resize(n);
		for (j=0; j<n; ++j) cin >> xs[j];
		for (j=0; j<n; ++j) cin >> ys[j];

		cout << "Case #" << i << ": " << calc() << endl;
	}

	return 0;
}

