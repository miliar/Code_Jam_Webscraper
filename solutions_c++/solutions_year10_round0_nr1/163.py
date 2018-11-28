#include <stdio.h>

int main(int argc, char *argv[])
{
	freopen ("A-large.in", "r", stdin);
	freopen ("ou.txt", "w", stdout);

	int T;
	scanf ("%d", &T);
	for (int i = 1; i <= T; ++i)
	{
		printf ("Case #%d: ", i);
		int flag = 0, N, K;
		scanf ("%d%d", &N, &K);
		if (K % (1 << N) == (1 << N) - 1)
			printf ("ON\n");
		else
			printf ("OFF\n");
	}
	
	return 0;
}
