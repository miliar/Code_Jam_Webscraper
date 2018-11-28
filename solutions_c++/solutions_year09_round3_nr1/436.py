#include <stdio.h>
#include <algorithm>

using namespace std;

int main()
{
	int n;
	scanf("%d", &n);
	for (int i=0; i<n; i++)
	{
		char s[100];
		int out[100];

		scanf("%s", s);

		int what[256];
		fill(what, what+256, -1);

		int last = -1;
		int base = 0;

		int len = strlen(s);
		for (int j=0; j<len; j++)
			if (what[s[j]] == -1)
			{
				switch (last)
				{
				case -1:
					last = 1;
					break;
				case 1:
					last = 0;
					break;
				case 0:
					last = 2;
					break;
				default:
					last++;
				}
				what[s[j]] = last;
				out[j] = last;
				base++;
			}
			else
				out[j] = what[s[j]];
		//printf("base = %d\n", base);
		if (base == 1) base = 2;
		long long ans = 0;
		for (int j=0; j<len; j++)
		{
			ans *= base;
			ans += out[j];
		}

		printf("Case #%d: %lld\n", i+1, ans);


	}
	return 0;
}

