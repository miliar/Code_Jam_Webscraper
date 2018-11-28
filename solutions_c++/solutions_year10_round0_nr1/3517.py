#include <fstream>

using namespace std;

int main() {
	ifstream in("A-large.in");
	ofstream out("A-large.out");

	int T;
	in >> T;
	for (int x = 0; x < T; x++) {
		int N, K;
		in >> N >> K;
		bool is = 1;
		for (int i = 0; i < N; i++) {
			if (((1 << i) & K) == 0) {
				is = 0;
				break;
			}
		}
		out << "Case #" << x + 1 << ": " << (is?"ON":"OFF") << endl;
	}
}
