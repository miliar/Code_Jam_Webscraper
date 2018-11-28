#include <stdio.h>
#include <math.h>

void main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

	int T;
	scanf("%d", &T);

	for (int t = 1; t <= T; t++)
	{
		int N, K;
		scanf("%d %d", &N, &K);
		int C = pow(2.0, N);
		printf("Case #%d: %s\n", t, K % C + 1 == C ? "ON" : "OFF");
	}
}
