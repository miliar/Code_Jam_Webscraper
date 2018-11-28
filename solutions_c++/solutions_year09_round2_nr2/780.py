#include <cstdio>
#include <algorithm>
using namespace std;
int main()
{
	freopen("E:/other contests/code jam/2009/1B/1.txt", "w", stdout);
	int t;
	char n[24];
	scanf("%d", &t);
	getchar();
	for (int k = 1; k <= t; ++k)
	{
		gets(n);
		int l = strlen(n);
		printf("Case #%d: ", k);
		if (!next_permutation(n, n+l))
		{
			sort(n, n+l);
			int i;
			for (i = 0; i < l; ++i)
				if (n[i] != '0') break;
			putchar(n[i]);
			for (int j = 0; j <= i; ++j)
				putchar('0');
			puts(n+i+1);
		}
		else
			puts(n);
	}
	return 0;
}