#include <stdio.h>
#include <memory.h>
#include <algorithm>
using namespace std;

#define CL(x)		memset(x, 0, sizeof(x))
#define CLX(x, v)	memset(x, v, sizeof(x))

const int K = 30;
const int N = 100 + 5;

int c, d, n, q;
int cc[K][K];
int dd[K][K];
int nn[N];
int qq[N];

int a2i(char c)
{
	return c - 'A';
}

char i2a(int i)
{
	return 'A' + i;
}

void Solve()
{
	q = 0;
	for (int k = 0; k < n; k++)
	{
		qq[q++] = nn[k];
		while (q > 1)
		{
			int z = cc[ qq[q - 1] ][ qq[q - 2] ];
			if (z != -1)
			{
				q -= 2;
				qq[q++] = z;
				continue;
			}
			break;
		}
		for (int i = 0; i < q; i++)
			for (int j = 0; j < i; j++)
				if (dd[ qq[i] ][ qq[j] ])
					q = 0;
	}
	printf("[");
	for (int i = 0; i < q; i++)
	{
		if (i) printf(", ");
		printf("%c", i2a(qq[i]));
	}
	printf("]\n");
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int tt;
	scanf("%d", &tt);
	for (int t = 1; t <= tt; t++)
	{
		CL(dd);
		CLX(cc, -1);
		printf("Case #%d: ", t);
		scanf("%d", &c);
		for (int i = 0; i < c; i++)
		{
			char buf[4];
			scanf("%s", buf);
			cc[ a2i(buf[0]) ][ a2i(buf[1]) ] = a2i(buf[2]);
			cc[ a2i(buf[1]) ][ a2i(buf[0]) ] = a2i(buf[2]);
		}
		scanf("%d", &d);
		for (int i = 0; i < d; i++)
		{
			char buf[3];
			scanf("%s", buf);
			dd[ a2i(buf[0]) ][ a2i(buf[1]) ] = 1;
			dd[ a2i(buf[1]) ][ a2i(buf[0]) ] = 1;
		}
		scanf("%d", &n);
		char buf[N];
		scanf("%s", buf);
		for (int i = 0 ; i < n; i++) nn[i] = a2i(buf[i]);
		Solve();
	}
	
	return 0;
}