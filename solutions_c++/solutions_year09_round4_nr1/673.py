#include <cstdio>
#include <algorithm>
using namespace std;

char s[50];
int a[50];
int main()
{
	freopen("input2.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T, t, n, m, i, j;
	scanf("%d", &T);
	for (t = 1; t <= T; t++)
	{
		m = 0;
		scanf("%d", &n);
		for (i = 1; i <= n; i++)
		{
			scanf("%s", s+1);
			for (j = n; j && s[j] == '0'; j--);
			a[i] = j;
		}
		for (i = 1; i <= n; i++)
			if (a[i] > i)
			{
				for (j = i+1; j <= n; j++)
					if (a[j] <= i)
						break;
				while (i+1 <= j)
				{
					swap(a[j-1], a[j]);
					j--;
					m++;
				}
			}
		printf("Case #%d: %d\n", t, m);
	}
	return 0;
}
/*
1
4
1110
1100
1111
1000

3
2
10
11
3
001
100
010
4
1110
1100
1100
1000

*/
