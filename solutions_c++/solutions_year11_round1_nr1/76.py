#define _CRT_SECURE_NO_DEPRECATE
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <stdlib.h>
#include <ctime>
#include <set>
#include <map>
#include <queue>
#include <string>
#include <math.h>
#include <queue>
#include <memory.h>
#include <iostream>
#include <stack>
//#include <complex>

using namespace std;

void ASS(bool b)
{
	if (!b)
	{
		++*(int*)0;
	}
}

#define FOR(i, x) for (int i = 0; i < (int)(x); i++)
#define CL(x) memset(x, 0, sizeof(x))

#pragma comment(linker, "/STACK:106777216")

typedef vector<int> vi;
typedef long long LL;

int d[128][128];

int cnt = 0;

void Init()
{
	memset(d, 0xFF, sizeof(d));
	d[0][0] = 1;
	for (int A = 1; A <= 100; A++)
		for (int a = 1; a <= 100; a++)
		{
			if (a * A % 100 != 0) continue;
			int xa = a * A / 100;
			for (int b = 1; b <= 100; b++)
			{
				if (d[a][b] != -1)
					continue;
				for (int x = 0; x <= 10000; x++)
				{
					cnt++;
					if ((xa + x) * 100 % b != 0) continue;
					int B = (xa + x) * 100 / b;
					int xb = xa + x;
					if (xb > B || A > B || A - xa > B - xb) continue;
					{
						if (a == 10 && b == 100)
						{
							cnt = cnt;
						}
						d[a][b] = A;
//						break;
					}
				}
			}
		}
}

void Solve()
{
	LL N, a, b;
	cin >> N >> a >> b;
	if (d[a][b] == -1 || d[a][b] > N)
		printf("Broken\n");
	else
		printf("Possible\n");
}

int main()
{
#ifndef _DEBUG
	freopen("c:\\my\\in.txt", "r", stdin);
	freopen("c:\\my\\out.txt", "w", stdout);
#endif
	Init();
//	cout << cnt << endl;
	int n;
	cin >> n;
	FOR(i, n)
	{
		printf("Case #%d: ", i + 1);
		Solve();
	}
	return 0;
}