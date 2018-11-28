#include <iostream>
#include <vector>
using namespace std;

int main()
{
	int t, m = 0;
	cin >> t;

	while (t--) {
		m++;
		int r, k, n;
		cin >> r >> k >> n;
		vector<int> v(n);
		for (int i = 0; i < n; i++) cin >> v[i];
		
		int z = 0;
		for (int i = 0; i < v.size(); i++) {
			z += v[i];
		}
		if (z <= k) {
			cout << "Case #" << m << ": " << z*r << endl;
			continue;
		}

		int i = 0, p = 0, sum = 0, q = 0;
		while (p != r) {
			p++;
			q = 0;
			while (q+v[i] <= k) {
				q += v[i];
				sum += v[i];
				if (i+1 < v.size()) i++;
				else i = 0;
			}
		}
		
		cout << "Case #"<< m << ": " << sum << endl;
	}

	return 0;
}		
