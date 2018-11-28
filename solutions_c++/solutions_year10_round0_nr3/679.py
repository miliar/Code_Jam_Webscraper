#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	long long t, r, k, n;
	long long people[2000], money[2000], add[2000], total, result;
	ofstream fout("D:\\out");
	ifstream fin("D:\\in");
	fin >> t;
	for (int i = 0; i < t; ++i) {
		fin >> r >> k >> n;
		total = 0;
		for (int j = 0; j < n; ++j) {
			fin >> people[j];
			total += people[j];
		}
		if (total <= k) {
			result = total * r;
		} else {
			for (int j = 0; j < n; ++j) {
				money[j] = people[j];
				add[j] = 1;
				while (money[j] + people[(j + add[j]) % n] <= k) {
					money[j] += people[(j + add[j]) % n];
					++add[j];
				}
			}

			result = 0;
			int ptr = 0;
			for (int j = 0; j < r; ++j) {
				result += money[ptr];
				ptr = (ptr + add[ptr]) % n;
			}
		}
		fout << "Case #" << i + 1 << ": " << result << endl;
	}

	return 0;
}

