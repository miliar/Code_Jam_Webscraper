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
typedef vector<string> vs;

int a[1024];
int b[1024];

void Solve()
{
	int n;
	cin >> n;
	FOR(i, n)
	{
		cin >> a[i];
		b[i] = a[i];
	}
	sort(a, a + n);
	int x = 0;
	int sum = -a[0];
	FOR(i, n)
	{
		x ^= a[i];
		sum += a[i];
	}
	if (x != 0)
	{
		printf("NO\n");
	}
	else
		printf("%d\n", sum);
}

int main()
{
	freopen("c:\\my\\in.txt", "r", stdin);
	freopen("c:\\my\\out.txt", "w", stdout);
	int t;
	cin >> t;
	FOR(i, t)
	{
		printf("Case #%d: ", i + 1);
		Solve();
	}

	return 0;
}