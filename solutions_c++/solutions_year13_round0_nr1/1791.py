#include <cstdio>
using namespace std;

char a[4][4];

int calc()
{
	int res = 0;
	bool ok;

	for (int i = 0; i < 4; i++)
	{
		ok = true;
		for (int j = 0; j < 4; j++)
			if (a[i][j] != 'X' && a[i][j] != 'T')
				ok = false;
		if (ok)
			res = 1;
	}
	for (int j = 0; j < 4; j++)
	{
		ok = true;
		for (int i = 0; i < 4; i++)
			if (a[i][j] != 'X' && a[i][j] != 'T')
				ok = false;
		if (ok)
			res = 1;
	}
	ok = true;
	for (int i = 0; i < 4; i++)
	{
		if (a[i][i] != 'X' && a[i][i] != 'T')
			ok = false;
	}
	if (ok) res = 1;

	ok = true;
	for (int i = 0; i < 4; i++)
	{
		if (a[i][3 - i] != 'X' && a[i][3 - i] != 'T')
			ok = false;
	}
	if (ok) res = 1;
	if (res == 1)
		return res;

	
	for (int i = 0; i < 4; i++)
	{
		ok = true;
		for (int j = 0; j < 4; j++)
			if (a[i][j] != 'O' && a[i][j] != 'T')
				ok = false;
		if (ok)
			res = 2;
	}
	for (int j = 0; j < 4; j++)
	{
		ok = true;
		for (int i = 0; i < 4; i++)
			if (a[i][j] != 'O' && a[i][j] != 'T')
				ok = false;
		if (ok)
			res = 2;
	}
	ok = true;
	for (int i = 0; i < 4; i++)
	{
		if (a[i][i] != 'O' && a[i][i] != 'T')
			ok = false;
	}
	if (ok) res = 2;

	ok = true;
	for (int i = 0; i < 4; i++)
	{
		if (a[i][3 - i] != 'O' && a[i][3 - i] != 'T')
			ok = false;
	}
	if (ok) res = 2;
	if (res == 2)
		return res;

	ok = true;
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			if (a[i][j] == '.') ok = false;
	if (ok)
		return 3;

	return 4;
}


int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n, p;
	scanf("%d\n", &n);

	for (int k = 1; k <= n; k++)
	{

		for (int j = 0; j < 4; j++)
			scanf("%s \n", &a[j]);
		scanf("\n");

		printf("Case #%d: ", k);
		p = calc();
		if (p == 1)
			printf("X won \n");
		if (p == 2)
			printf("O won \n");
		if (p == 3)
			printf("Draw \n");
		if (p == 4)
			printf("Game has not completed \n");
	}

	return 0;
}