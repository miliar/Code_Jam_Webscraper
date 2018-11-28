#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int T, N;
	int t, i, v, max, sum, s1, s2;
	vector<int> values;
	ifstream in("H:\\temp\\C-large.in");
	in >> T;
	ofstream out("H:\\temp\\C-large.out");
	for (t = 1; t <= T; t++) {
		values.clear();
		s1 = s2 = 0;
		sum = 0;
		max = 0;
		in >> N;
		for (i = 0; i < N; i++) {
			in >> v;
			s1 ^= v;
			values.push_back(v);
		}
		sort(values.begin(), values.end());
		for (i = N - 1; i >= 1; i--) {
			sum += values[i];
			s2 ^= values[i];
			s1 ^= values[i];
			if (s1 == s2)
				max = sum;
		}
		out << "Case #" << t << ": ";
		if (max)
			out << max << endl;
		else
			out << "NO\n";
	}
	in.close();
	out.close();
	return 0;
}