#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>

using namespace std;

#define FILENAME	"D-large-0"

int main() {
	ifstream in(FILENAME ".in");
	ofstream out(FILENAME ".out");

	int T;
	in >> T;
	for (int test = 1; test <= T; ++test) {
		int N, a, ans = 0;
		in >> N;
		for (int i = 1; i <= N; ++i) {
			in >> a;
			if (a != i) ++ans;
		}
		out << "Case #" << test << ": " << ans << endl;
	}

	return 0;
}