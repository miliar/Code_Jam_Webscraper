#include <cstdio>
#include <iostream>
using namespace std;

bool on(const unsigned int N, const unsigned int K)
{
	for (unsigned int i = 1; i <= (1 << (N - 1)); i *= 2)
		if ((K / i) % 2 == 0)
			return false;
	return true;
}

int main()
{
	int T; cin >> T;
	for (int x = 1; x <= T; ++x) {
		unsigned int N, K; cin >> N >> K;
		printf("Case #%d: %s\n", x, on(N, K) ? "ON" : "OFF");
	}
}
