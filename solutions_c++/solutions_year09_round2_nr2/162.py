#include <stdio.h>
#include <algorithm>

int main()
{
	char s[22];
	int t, n;
	scanf("%d\n", &t);
	for (int tc = 1; tc <= t; tc++)
	{
		gets(s);
		//printf("in: %s\n", s);
		n = strlen(s);
		if (!std::next_permutation(s, s + n))
		{
			std::copy(s, s + n, s + 1);
			s[++n] = 0;
			s[0] = '0';
			int i = 0;
			while (s[i] == '0') i++;
			std::swap(s[0], s[i]);
		}
		printf("Case #%d: %s\n", tc, s);
	}
	return 0;
}