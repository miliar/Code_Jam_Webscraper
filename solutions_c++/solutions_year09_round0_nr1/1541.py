#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

char a[5009][20], x[999];
int l, pl;

bool fc(char g)
{
	for (; pl < (int) strlen(x); pl++)
	{
		if (x[pl] == '(')
		{
			bool ok = false;
			for (pl++; x[pl] != ')'; pl++)
			{
				if (x[pl] == g)
				{
					ok = true;
				}
			}
			pl++;
			return ok;
		}
		else
		{
			pl++;
			return (g == x[pl - 1]);
		}
	}
	return false;
}

bool f(int z)
{
	pl = 0;
	for (int i = 0; i < l; i++)
	{
		if (!fc(a[z][i]))
		{
			return false;
		}
	}
	return true;
}

int main(void)
{
	int d, n, t = 1;

	scanf("%d %d %d ", &l, &d, &n);

	for (int i = 0; i < d; i++)
	{
		gets(a[i]);
	}
	for (int i = 0; i < n; i++)
	{
		int r = 0;
		gets(x);
		for (int i = 0; i < d; i++)
		{
			if (f(i))
			{
				r++;
			}
		}
		printf("Case #%d: %d\n", t++, r);
	}
	
	return 0;
}
