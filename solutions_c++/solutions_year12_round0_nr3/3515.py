#include <iostream>
#include <cstring>
#include <cctype>
#include <cstdlib>
#include <cstdio>
using namespace std;

bool check(int a, int b)
{
	char x[22];
	int len;
	sprintf(x, "%d%d", a, a);
	len = strlen(x) / 2;
	for (int i = 1, j = len+1; i<len; i++, j++)
	{
		char ch = x[j];
		x[j] = 0;

		if (x[i] != '0' && atoi(x+i) == b) return true;
		x[j] = ch;
	}
	return false;
}

int main(void)
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int cnmb=1; cnmb<=T; cnmb++)
	{
		int a, b;
		int ans = 0;
		scanf("%d%d", &a, &b);
		for (int i=a; i<=b; i++)
			for (int j=i+1; j<=b; j++)
			{
				if (check(i, j))
				{
					ans++;
				}	
			}
		printf("Case #%d: %d\n", cnmb, ans);	
	}
	return 0;
}
