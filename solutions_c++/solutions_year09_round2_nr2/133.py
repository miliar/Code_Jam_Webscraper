#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
using namespace std;

const int maxn = 100;

int TEST;

char a[maxn];

int main()
{
	freopen(".in","r",stdin);
	freopen(".out","w",stdout);
	scanf("%d\n", &TEST);
	for (int test = 0; test < TEST; test++)
	{
		printf("Case #%d: ", test + 1);
		gets(a);
		int n = strlen(a);
		if (next_permutation(a, a + n))	puts(a); else
		{
			for (int i = 0; i < n; i++)
				if ('0' < a[i] && (a[i] < a[0] || a[0] == '0')) swap(a[i], a[0]);

			printf("%c", a[0]);
			a[0] = '0';
			sort(a, a + n);
			puts(a);
		}

	}
	return 0;
}
