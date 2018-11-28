#pragma comment (linker, "/STACK:16000000")
#include <cstdio>
#include <cstring>
#include <math.h>
#include <algorithm>
#include <string>
#include <vector>
#include <cctype>
#include <bitset>
#include <sstream>
#include <set>
#include <map>

using namespace std;
template <class T> T sqr(T a) { return a * a; }

int prime[100000];
int np[1000000];
int a[20];
int pc, n;

void gen()
{
	memset(np, 0, sizeof(np));
	np[0] = np[1] = 1;
	pc = 0;
	for (int i = 2; i < 1000000; i++)
		if (!np[i])
		{
			for (int j = i * 2; j < 1000000; j += i)
				np[j] = 1;
			prime[pc++] = i;			
		}
}

int gcd(int a, int b, int &x, int &y)
{
	if (a == 0)
	{
		x = 0;
		y = 1;
		return b;
	}
	int x1, y1;
	int d = gcd(b % a, a, x1, y1);
	x = y1 - (b / a) * x1;
	y = x1;
	return d;
}

int divp(int a, int b, int p)
{
	int x, y;
	int g = gcd(b, p, x, y);
	if (x < 0)
		x += p;
	return (a * x) % p;	
}

int solve(int p)
{
	for (int i = 0; i < n; i++)
		if (a[i] >= p)
			return -1;

	int res = -1;
	int same = n > 1;

	for (int i = 0; i < n - 1; i++)
		if (a[i] != a[i + 1])
			same = 0;
	if (same)
		res = a[0];

	int mult = 0;
	for (int i = 0; i < n - 1; i++)
		for (int j = i + 1; j < n - 1; j++)
		{
			int a11 = a[i], a12 = 1, a21 = a[j], a22 = 1, b1 = a[i + 1], b2 = a[j + 1];
			int dd = (p + a11 * a22 % p - a12 * a21 % p) % p;
			if (dd)
			{
				int aa = divp((p + b1 * a22 % p - b2 * a12 % p) % p, dd, p);
				int bb = divp((p + a11 * b2 % p - a21 * b1 % p) % p, dd, p);
				int loc = (a[n - 1] * aa + bb) % p;
				int fail = 0;
				for (int i = 0; i < n - 1; i++)
					if ((a[i] * aa + bb) % p != a[i + 1])
						fail = 1;
				if (!fail)
				{
					if (res + 1 && loc != res)
						mult = 1;
					res = loc;
				}
			}
		}
	if (mult)
		return -1;
	return res;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int testNum;
	scanf("%d", &testNum);
	gen();
	for (int testCount = 0; testCount < testNum; testCount++)
	{
		int d;
		scanf("%d%d", &d, &n);
		for (int i = 0; i < n; i++)
			scanf("%d", &a[i]);
		int res = -1;
		int mult = 0;
		for (int i = 0; i < pc && prime[i] < pow(10.0, 1.0 * d); i++)
		{
			int loc = solve(prime[i]);
			if (loc + 1 && res + 1 && loc != res)
				mult = 1;
			if (loc + 1)
				res = loc;
		}
		if (mult || res == -1)
			printf("Case #%d: I don't know.\n", testCount + 1);
		else
			printf("Case #%d: %d\n", testCount + 1, res);
	}
	return 0;
}