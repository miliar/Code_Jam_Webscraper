#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int n, l, h;
long long a[100000];
long long f;

long long cmmdc(long long a, long long b)
{
	if (a % b == 0)
		return b;
	return cmmdc(b, a % b);
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;
	for (int TT=1;TT<=T;++TT) {
		cin >> n >> l >> h;
		for (int i=0;i<n;++i)
			cin >> a[i];
		/*sort(a, a + n);

		f = 1;

		while (f <= h) {
			bool ok = true;
			for (int i=0;i<n && ok;++i)
				if (f % a[i] != 0 && a[i] % f != 0)
					ok = false;

			if (ok && 
		}*/

		int f;

		for (f=l;f<=h;++f)
		{
			bool ok = true;
			for (int i=0;i<n && ok;++i)
				if (a[i] % f != 0 && f % a[i] != 0)
					ok = false;
			if (ok) break;
		}
		cout << "Case #" << TT << ": ";
		if (f <= h)
			cout << f << endl;
		else
			cout << "NO\n";
	}

	return 0;
}
