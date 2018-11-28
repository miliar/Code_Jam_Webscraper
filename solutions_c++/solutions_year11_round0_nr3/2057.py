#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <functional>
#include <iostream>
#include <set>
#include <string>
#include <vector>
using namespace std;

int main()
{
	long long int inps, i, nums, buf, aba, ok, j, res, min;
	vector <long long int> ones;

	cin >> inps;
	
	for (i = 0; i < inps; i++) {
		cin >> nums;

		res = 0;
		min = 1000000000;
		ones.clear();

		for (j = 0; j < nums; j++) {
			cin >> buf;
			res += buf;
			if (buf < min)
				min = buf;

			aba = 0;

			while (buf > 0) {
				if (aba + 1 > ones.size())
					ones.push_back(0);
				if (buf % 2) {
					ones[aba]++;
				}
				buf /= 2;
				aba++;
			}
		}

		ok = 1;

		for (j = 0; j < ones.size(); j++) {
			if (ones[j] % 2) {
				ok = 0;
				break;
			}
		}

		cout << "Case #" << i + 1 << ": ";
		if (ok)
			cout << res - min << endl;
		else
			cout << "NO" << endl;
	}

	return 0;
}
