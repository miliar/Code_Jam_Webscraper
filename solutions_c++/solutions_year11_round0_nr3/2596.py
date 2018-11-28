#include <iostream>
#include <cstring>
using namespace std;

void solve()
{
	unsigned bits[32];
	memset(bits, 0, sizeof(bits));
	unsigned sum = 0, smallest = -1;

	unsigned N; cin >> N;
	for (unsigned i = 0; i < N; i++) {
		unsigned num; cin >> num;

		sum += num;
		if (num < smallest)
			smallest = num;

		for (unsigned j = 0; j < 32; j++) {
			bits[j] += num & 1;
			num >>= 1;
		}
	}

	for (unsigned j = 0; j < 32; j++) {
		if ((bits[j] % 2) != 0) {
			cout << "NO" << endl;
			return;
		}
	}

	cout << sum - smallest << endl;
}

int main()
{
	int T; cin >> T;
	for (int i = 0; i < T; ++i) {
		cout << "Case #" << i+1 << ": ";
		solve();
	}
}
