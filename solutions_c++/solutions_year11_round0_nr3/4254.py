#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {

	ifstream in("C-large.in");
	ofstream out("out.txt");

	int t, n;
	in >> t;
	for (int tc = 1; tc <= t; ++tc) {
		in >> n;
		vector<int> v(n, 0);
		for (int i = 0; i < n; ++i) {
			in >> v[i];
		}
		

		bool isGood = true;
		for(int k = 0; k < 30; ++k) {
			int num = 0;
			for (int i = 0; i < n; ++i) {
				if (v[i] & (1<<k)) 
					++num;
			}
			if (num % 2 == 1) {
				isGood = false;
				break;
			}
		}

		if (isGood) {
			sort(v.begin(), v.end());
			int sum = 0;
			for (int i = 1; i < n; ++i) {
				sum += v[i];
			}

			out << "Case #" << tc << ": " << sum << endl;
		}
		else {
			out << "Case #" << tc << ": " << "NO" << endl;
		}
	}

	return 0;
}