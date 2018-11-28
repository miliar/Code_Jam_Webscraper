#include <cstdio>
#include <cmath>
using namespace std;

int main()
{
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);

	int T, N, K;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%d%d", &N, &K);
		int x = (int)pow(2.0, (double)N);
		printf("Case #%d: %s\n", t, (K + 1) % x == 0 ? "ON" : "OFF");
	}
	return 0;
}