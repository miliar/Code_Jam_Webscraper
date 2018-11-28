#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long Long;

const Long M = 1000000007;

int main()
{
	int nCase;
	cin >> nCase;

	for(int iCase = 1; iCase <= nCase; iCase++) {
		Long n, m, x, y, z;
		cin >> n >> m >> x >> y >> z;

		vector<Long> a(n);

		for(int i = 0; i < m; i++)
			cin >> a[i];
		for(int i = m; i < n; i++)
			a[i] = (x * a[i - m] + y * (i - m + 1)) % z;

		vector<Long> b(n);
		Long sum = 0;

		for(int i = 0; i < n; i++) {
			b[i] = 1;

			for(int j = 0; j < i; j++) {
				if(a[i] > a[j]) { b[i] = (b[i] + b[j]) % M; }
			}

			sum = (sum + b[i]) % M;
		}

		cout << "Case #" << iCase << ": " << sum << endl;
	}

	return 0;
}
