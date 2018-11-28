#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <iostream>
#include <string>
#include <map>
#include <vector>
using namespace std;
char getz()
{
	char ret;
	do
	{
		ret = getchar();
	}while(ret != '.' && ret != 'O' && ret != 'X' && ret != 'T');
	return ret;
}
char a[10][10];
int full()
{
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			if (a[i][j] == '.')
				return 0;
	return 1;
}
int check(char cc)
{
	int C, T;
	for (int i = 0; i < 4; i++)
	{
		C = 0, T = 0;
		for (int j = 0; j < 4; j++)
		{
			if (a[i][j] == cc)
				C++;
			if (a[i][j] == 'T')
				T++;
		}
		if (C == 4 || (C == 3 && T == 1)) return 1;
		C = 0, T = 0;
		for (int j = 0; j < 4; j++)
		{
			if (a[j][i] == cc)
				C++;
			if (a[j][i] == 'T')
				T++;
		}
		if (C == 4 || (C == 3 && T == 1)) return 1;
	}
	C = 0, T = 0;
	for (int i = 0; i < 4; i++)
	{
		if (a[i][i] == cc) C++;
		if (a[i][i] == 'T') T++;
	}
	if (C == 4 || (C == 3 && T == 1)) return 1;
		C = 0, T = 0;
	for (int i = 0; i < 4; i++)
	{
		if (a[i][3 - i] == cc) C++;
		if (a[i][3 - i] == 'T') T++;
	}
	if (C == 4 || (C == 3 && T == 1)) return 1;
	return 0;
}
int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int tot;
	cin >> tot;
	for (int tt = 1; tt <= tot; tt++)
	{
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				a[i][j] = getz();
		if (check('X'))
			printf("Case #%d: X won\n", tt);
		else if (check('O'))
			printf("Case #%d: O won\n", tt);
		else if (full())
			printf("Case #%d: Draw\n", tt);
		else
			printf("Case #%d: Game has not completed\n", tt);
	}
	return 0;
}
