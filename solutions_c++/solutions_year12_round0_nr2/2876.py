#include <stdio.h>

int N, S, P, t;

void go ()
{
	int result = 0;

	scanf ("%d%d%d", &N, &S, &P);
	for (int i = 0; i < N; ++i)
	{
		scanf ("%d", &t);
		if (t % 3 == 1)
		{
			result += (t / 3 + 1 >= P);
			continue;
		}

		if (t / 3 + (t % 3 > 0) >= P)
		{
			result ++;
			continue;
		}
	
		if (t / 3 + (t % 3 > 0) + 1 >= P && t > 0)
		{
			result ++;
			S --;
		}
	}

	if (S < 0)
		result += S;

	printf ("%d\n", result);
}

int main(int argc, char *argv[])
{
	freopen ("B-large.in", "r", stdin);
	freopen ("B-large.out", "w", stdout);


	int T;
	scanf ("%d", &T);
	for (int i = 1; i <= T; ++i)
	{
		printf ("Case #%d: ", i);
		go ();
	}

	return 0;
}
