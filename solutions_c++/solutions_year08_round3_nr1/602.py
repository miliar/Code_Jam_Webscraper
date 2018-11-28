#include <cstdio>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;

typedef long long ll;
int main (int argc, char* argv[])
{
	if (argc >= 2)
		freopen (argv[1], "r", stdin);
	if (argc >= 3)
		freopen (argv[2], "w", stdout);

	int N;
	scanf ("%d", &N);

	for (int t = 0; t < N; ++t)
	{
		int P, K, L;
		scanf ("%d %d %d", &P, &K, &L);

		vector<int> freq (L);
		for (int i = 0; i < L; ++i)
			scanf ("%d", &freq[i]);

		sort (freq.begin(), freq.end(), greater<int>() );

		ll req = 0;
		for (int i = 0; i < L; ++i)
			req += ((long long)(freq[i]))*((i/K) + 1);
		
		printf ("Case #%d: %d\n", t+1, req);
	}

	return 0;
}