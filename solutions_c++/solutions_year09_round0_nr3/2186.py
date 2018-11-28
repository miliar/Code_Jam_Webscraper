#include <stdio.h>
#include <algorithm>

int main()
{
	const char p[] = "welcome to code jam";
	static int C[sizeof(p)];
	static char s[501];
	int n, c = 0;
	scanf("%d\n", &n);
	C[0] = 1;
	for (int t = 1; t <= n; t++)
	{
		gets(s);
		std::fill(C + 1, C + sizeof(p), 0);
		for (int i = 0; s[i]; i++)
			for (int j = sizeof(p) - 1; j >= 1; j--)
				if (s[i] == p[j - 1])
					C[j] = (C[j] + C[j - 1]) % 10000;
		printf("Case #%d: %04d\n", t, C[sizeof(p) - 1]);
	}
}