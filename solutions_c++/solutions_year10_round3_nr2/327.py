#include <iostream>

using namespace std;

long long a,b,c;

long long Solve() {
	long long res = 0;
	long long n = 0;
	long long tmp = a * c;
	while (tmp < b) {
		++n;
		tmp *= c;
	}
	++n;
	while (n > 1) {
		n = (n + 1)/2;
		++res;
	}
	return res;
}

int main() {
	//freopen("in.txt","r",stdin);
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int ncase;
	cin >> ncase;
	for (int i = 0; i < ncase; ++i) {
		cin >> a >> b >> c;
		long long ans = Solve();
		// long long ans = Easy();
		cout << "Case #" << i + 1 << ": " << ans << endl;
	}
	return 0;
}