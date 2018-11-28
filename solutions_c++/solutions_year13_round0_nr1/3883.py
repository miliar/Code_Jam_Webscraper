#include <cstdio>
#include <cmath>
#include <cctype>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <memory.h>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#include <functional>
#include <ctime>

#define FOR(i, n) for (int i = 0; i < n; i++)

#pragma comment(linker, "/STACK:250777216")

using namespace std;

typedef long long LL;
typedef vector<int> vint;
typedef vector<vint> vvint;
const int MOD = int(1e9) + 7;
const int HMOD = (1 << 22) - 1;
const int BASE = int(1e9);

const int N = 100002;

char a[8][8] = {};
int n;

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		getchar();
		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
				a[j][k] = getchar();
			getchar();
		}
		bool empty = false;
		for (int j = 0; j < 4; j++)
		{
			bool flag = true;
			for (int t = 0; t < 4; t++)
			{
				if (a[j][t] != 'X' && a[j][t] != 'T')
					flag = false;
				if (a[j][t] == '.')
					empty = true;
			}
			if (flag)
			{
				printf("Case #%d: X won\n", i + 1);
				goto label1;
			}
			flag = true;
			for (int t = 0; t < 4; t++)
				if (a[j][t] != 'O' && a[j][t] != 'T')
					flag = false;
			if (flag)
			{
				printf("Case #%d: O won\n", i + 1);
				goto label1;
			}
		}

		for (int j = 0; j < 4; j++)
		{
			bool flag = true;
			for (int t = 0; t < 4; t++)
				if (a[t][j] != 'X' && a[t][j] != 'T')
					flag = false;
			if (flag)
			{
				printf("Case #%d: X won\n", i + 1);
				goto label1;
			}
			flag = true;
			for (int t = 0; t < 4; t++)
				if (a[t][j] != 'O' && a[t][j] != 'T')
					flag = false;
			if (flag)
			{
				printf("Case #%d: O won\n", i + 1);
				goto label1;
			}
		}

		bool flag = true;
		for (int t = 0; t < 4; t++)
			if (a[t][t] != 'X' && a[t][t] != 'T')
				flag = false;
		if (flag)
		{
			printf("Case #%d: X won\n", i + 1);
			goto label1;
		}
		flag = true;
		for (int t = 0; t < 4; t++)
			if (a[t][t] != 'O' && a[t][t] != 'T')
				flag = false;
		if (flag)
		{
			printf("Case #%d: O won\n", i + 1);
			goto label1;
		}

		flag = true;
		for (int t = 0; t < 4; t++)
			if (a[t][3 - t] != 'X' && a[t][3 - t] != 'T')
				flag = false;
		if (flag)
		{
			printf("Case #%d: X won\n", i + 1);
			goto label1;
		}
		flag = true;
		for (int t = 0; t < 4; t++)
			if (a[t][3 - t] != 'O' && a[t][3 - t] != 'T')
				flag = false;
		if (flag)
		{
			printf("Case #%d: O won\n", i + 1);
			goto label1;
		}

		if (empty)
			printf("Case #%d: Game has not completed\n", i + 1);
		else
			printf("Case #%d: Draw\n", i + 1);
		label1:;
	}
	return 0;
}