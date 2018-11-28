#include <iostream>
#include <string.h>
#define MAXP 10
using namespace std;

int sat[1<<MAXP];
int match[MAXP][1<<(MAXP - 1)];
int Check (int start, int len);
void Minus (int start, int len);


int main()
{
	int t, i, j, f, p, tmp, res;
	freopen ("B-small.in", "r", stdin);
	freopen ("B-small.out", "w", stdout);
	scanf("%d", &t);
	for (f = 1; f <= t; f++)
	{
		res = 0;
		memset (sat, 0, sizeof sat);
		memset (match, 0, sizeof match);
		scanf("%d", &p);
		for (i = 0; i < (1<<p); i++)
		{
			scanf("%d", &tmp);
			sat[i] = p - tmp;
		}
		for (i = 0; i < p; i++)
		{
			for (j = 0; j < (1<<(p - i - 1)); j++)
			{
				scanf("%d", &match[i][j]);
			}
		}
		for (i = p - 1; i >= 0; i--)
		{
			for (j = 0; j < (1<<(p - i - 1)); j++)
			{
				if (Check (j * (1<<(i + 1)), 1<<(i + 1)) == -1)
				{
					Minus (j * (1<<(i + 1)), 1<<(i + 1));
					res++;
				}
			}
		}
		printf("Case #%d: %d\n", f, res);

	}
	return 0;
}

int Check (int start, int len)
{
	for (int i = 0; i < len; i++)
	{
		if (sat[i + start] > 0)
		{
			return -1;
		}
	}
	return 0;
}

void Minus (int start, int len)
{
	for (int i = 0; i < len; i++)
	{
		sat[i + start]--;
	}
}