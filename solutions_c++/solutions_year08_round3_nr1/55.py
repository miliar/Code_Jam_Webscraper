#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

typedef long long Long;

int main()
{
	int nCase;
	cin >> nCase;

	for(int iCase = 1; iCase <= nCase; iCase++) {
		int p, k, l;
		cin >> p >> k >> l;
		assert(p * k >= l); // always possible provided this condition

		vector<Long> v(l);

		for(int i = 0; i < l; i++)
			cin >> v[i];

		sort(v.rbegin(), v.rend());

		Long sum = 0;

		for(int i = 0; i < l; i++)
			sum += v[i] * (i / k + 1);

		cout << "Case #" << iCase << ": " << sum << endl;
	}

	return 0;
}
