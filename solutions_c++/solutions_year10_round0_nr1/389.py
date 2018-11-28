#include <cstdio>

using namespace std;

int N, K;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t)
	{
		printf("Case #%d: ", t);
		scanf("%d%d", &N, &K);
		printf((K % (1<<N) == (1<<N)-1) ? "ON\n" : "OFF\n");
	}

	return 0;
}
