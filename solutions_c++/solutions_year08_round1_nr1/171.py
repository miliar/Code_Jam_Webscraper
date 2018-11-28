#include <algorithm>
#include <iostream>
using namespace std;

const int MaxN = 800 + 10;

int caseNum, totCase;
int n;
long long a[MaxN], b[MaxN];

int main() {
	cin >> totCase;
	for (caseNum = 1; caseNum <= totCase; ++caseNum) {
		cin >> n;
		for (int i = 0; i < n; ++i)
			cin >> a[i];
		for (int i = 0; i < n; ++i)
			cin >> b[i];
		sort(a, a + n);
		sort(b, b + n);
		long long res = 0;
		for (int i = 0; i < n; ++i)
			res += a[i] * b[n - i - 1];
		cout << "Case #" << caseNum << ": " << res << endl;
	}
	return 0;
}
