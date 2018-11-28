#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

bool sort_comp_dec (size_t i, size_t j) { return (i>j); }

int main(int argc, char** argv)
{
	string str;
	size_t T;
	cin >> T;
	getline(cin, str);

	for (size_t i = 0; i < T; ++i) {
		size_t N, S, p, y = 0;
		cin >> N >> S >> p;
		vector<size_t> t(N);
		for (size_t j = 0; j < N; ++j) {
			cin >> t[j];
		}
		getline(cin, str);

		sort(t.begin(), t.end(), sort_comp_dec);

		for (size_t j = 0; j < N; ++j) {
			size_t k = t[j]/3;
			if (k+2 < p) break;
			size_t r = t[j]%3;
			size_t max;
			switch (r) {
			case 0:
				if (k >= p) ++y;
				else if (S > 0 && k != 0) {
					if (k+1 >= p) {
						--S;
						++y;
					}
				}
				break;
			case 1:
				if (k+1 >= p) ++y;
				break;
			case 2:
				if (k+1 >= p) ++y;
				else if (S > 0) {
					if (k+2 >= p) {
						--S;
						++y;
					}
				}
				break;
			default: cerr << "ERROR" << endl; return 1;
			}
		}

		cout << "Case #" << (i + 1) << ": " << y << endl;
	}
}


