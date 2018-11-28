#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

char s[10000];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tt;
	scanf("%d\n", &tt);
	for (int ii = 1; ii <= tt; ++ii)
	{
		printf("Case #%d: ", ii);
		gets(s);
		int len = strlen(s);
		if (next_permutation(s, s + len))
			printf("%s\n", s);
		else
		{
			s[len++] = '0';
			s[len] = 0;
			sort(s, s + len);
			int i = 0;
			while (s[i] == '0')
				++i;
			swap(s[i], s[0]);
			printf("%s\n", s);
		}
	}

	return 0;
}