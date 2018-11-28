#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;
const char inf = 100;

char c[1024][1024];
int l, p, C;

char rezolva(int, int);

int main()
{
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);

	int t, test;

	scanf("%d", &t);

	for(test = 1; test <= t; ++test)
	{
		scanf("%d %d %d", &l, &p, &C);
//		printf("%d %d %d\n", l, p, C);
		rezolva(l, p);
		printf("Case #%d: %d\n", test, c[l][p]);
		memset(c, 0, sizeof(c));
	}

	return 0;
}

char rezolva(int a, int b)
{
	//printf("%d %d\n", a, b);

	char temp;
	if((double)b / a <= (double)C)
	{
//		printf("din prima");
		return 0;
	}
	else
	{
		if(c[a][b] != 0)
		{
			return c[a][b];
		}
		c[a][b] = inf;
		for(int i = a * C; i <= b; ++i)
		{
			temp = max(rezolva(a, i), rezolva(i, b)) + 1;
			if(c[a][b] > temp)
				c[a][b] = temp;
		}
		return c[a][b];
	}
}
