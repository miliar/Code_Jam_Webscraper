#include <iostream>
using namespace std;

struct Entry {
	long long value;
	int size;
	int next;
};
Entry groups[1000];

int main(int argc, char* argv[])
{
	int T;
	cin >> T;
	for (int test = 1; test <= T; test++) {
		int R, k, N;
		cin >> R >> k >> N;

		for (int i = 0; i < N; i++) cin >> groups[i].size;
		for (int i = 0; i < N; i++) {
			int ofs = i;
			long long value = 0;
			for (int j = 0; j < N && groups[ofs].size + value <= k; j++) {
				value += groups[ofs].size;
				ofs = (ofs+1) % N;
			}
			groups[i].value = value;
			groups[i].next = ofs;
		}
		int ofs = 0;
		long long earned = 0;
		for (int ride = 0; ride < R; ride++) {
			earned += groups[ofs].value;
			ofs = groups[ofs].next;
		}
		cout << "Case #" << test << ": " << earned << "\n";
	}
	return 0;
}

