#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long LL;

int gcd(int a, int b) {
	return b == 0 ? a : gcd(b, a%b);
}

LL calc(vector<int>& a) {
	int N = a.size();
	int d = 0;
	for (int i = 0; i < N; i++)
		for (int j = i+1; j < N; j++)
			d = gcd(a[j] - a[i], d);
	return (d - (a[0] % d)) % d;
}

int main() {
	int TC;
	cin >> TC;
	for (int tc = 1; tc <= TC; tc++) {
		int N;
		cin >> N;
		vector<int> a(N);
		for (int i = 0; i < N; i++) cin >> a[i];
		sort(a.begin(), a.end());
		cout << "Case #" << tc << ": " << calc(a) << endl;
	}
}

