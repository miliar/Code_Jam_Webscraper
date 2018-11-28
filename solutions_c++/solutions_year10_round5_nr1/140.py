#include <iostream>
#include <fstream>
#include <cstdio>
#include <set>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <string>

using namespace std;

int pr[1100000];
int np;
int isp[1100000];

void GenPrimes()
{
	int i, j;
	np = 0;
	memset(isp, 0, sizeof(isp));
	for (i = 2; i <= 1000000; i++)
	{
		if (isp[i] == 0)
		{
			pr[np++] = i;
			if (i <= 1000)
			{
				for (j = i * i; j <= 1000000; j += i)
				{
					isp[j] = 1;
				}
			}
		}
	}
}

int d, k;
int x[15];

void Load()
{
	scanf("%d%d", &d, &k);
	int i;
	for (i = 0; i < k; i++) scanf("%d", &x[i]);
}

long long ExtGCD(long long a, long long b, long long &x, long long &y)
{
	if (a < b) return ExtGCD(b, a, y, x);
	else if (b == 0)
	{
		x = 1;
		y = 0;
		return a;
	}
	else
	{
		long long d, xx, yy;
		d = ExtGCD(b, a % b, xx, yy);
		x = yy;
		y = xx - (a / b) * yy;
		return d;
	}
}

long long Inv(long long a, long long p)
{
	a %= p;
	long long x, y;
	ExtGCD(a, p, x, y);
	x = x % p;
	if (x < 0) x += p;
	return x;
}

bool Can(int p, int &ra, int &rb)
{
	int i;
	for (i = 0; i < k; i++)
	{
		if (x[i] >= p) return false;
	}
	long long a, b;
	if (x[0] == x[1])
	{
		a = 1;
		b = 0;
	}
	else
	{
		a = ((x[1] - x[2] + p) * Inv(x[0] - x[1] + p, p)) % p;
		b = x[1] - a * x[0];
		b %= p;
		if (b < 0) b += p;
	}
	for (i = 0; i < k - 1; i++)
	{
		long long r = (a * x[i] + b) % p;
		if (x[i + 1] != r) return false;
	}
	ra = (int)a;
	rb = (int)b;
	return true;
}

void Solve()
{
	if (k <= 2)
	{
		if (k == 2 && x[0] == x[1])
		{
			printf("%d", x[0]);
		}
		else
		{
			printf("I don't know.");
		}
		return;
	}
	int i;
	int d10 = 1;
	for (i = 0; i < d; i++) d10 *= 10;
	int a, b, num, p;
	num = a = b = p = 0;
	int prop = 0;
	int good = true;
	for (i = 0; i < np; i++)
	{
		if (pr[i] > d10) break;
		if (Can(pr[i], a, b))
		{
			p = pr[i];
			if (num == 0) prop = (((long long)a) * x[k - 1] + b) % p; 
			else
			{
				if (prop != (((long long)a) * x[k - 1] + b) % p)
				{
					good = false;
				}
			}
			num++;
		}
	}
	if (!good || num == 0) printf("I don't know.");
	else
	{
		printf("%d", (int)((((long long)x[k - 1]) * a + b) % p));
	}
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	GenPrimes();
	int nt, it;
	scanf("%d", &nt);
	for (it = 0; it < nt; it++)
	{
		printf("Case #%d: ", it + 1);
		Load();
		Solve();
		printf("\n");
	}
	return 0;
}