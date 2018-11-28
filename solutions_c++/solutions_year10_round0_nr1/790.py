#include <cstdio>
#include <iostream>

using namespace std;

#define filename "A-large"

int main()
{
	freopen (filename ".in", "rt", stdin);
	freopen (filename ".out", "wt", stdout);

	int T, N, K, M;
	cin >> T;
	for (int test = 1; test <= T; ++test) {
		cin >> N >> K;
		M = (1 << N) - 1;
		cout << "Case #" << test << ": " << ((K & M) == M ? "ON" : "OFF") << endl;
	}

	return 0;
}