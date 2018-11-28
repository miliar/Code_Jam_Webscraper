#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;

int T, N;
long long K;

inline bool on ()
{
	K = K % (1 << N);
	return __builtin_popcountll (K) == N;
}

int main ()
{
	scanf ("%d", &T);

	for (int i = 0; i < T; i++)
	{
		scanf ("%d %lld", &N, &K);
		printf ("Case #%d: %s\n", i+1, (on () && K) ? "ON" : "OFF");
	}

	return 0;
}
