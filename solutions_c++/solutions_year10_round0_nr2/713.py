#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int base = 10000;

struct BigInt
{
	int a[100];
	BigInt& operator = (BigInt& x)
	{
		for (int i = 0; i <= x.a[0]; ++i)
			a[i] = x.a[i];
		return *this;
	}
	BigInt(BigInt& x)
	{
		for (int i = 0; i <= x.a[0]; ++i)
			a[i] = x.a[i];
	}
	BigInt(int x = 0)
	{
		a[0] = 1;
		a[1] = 0;
		while (x > 0)
		{
			a[a[0]] = x % base;
			++a[0];
			a[a[0]] = 0;
			x /= base;
		}
		norm();
	}
	BigInt operator + (BigInt& x)
	{
		int n = max(x.a[0], a[0]);
		BigInt ret;
		ret.fill(n + 1);
		for (int i = 1; i <= n; ++i)
		{
			if (i <= a[0])
				ret.a[i] += a[i];
			if (i <= x.a[0])
				ret.a[i] += x.a[i];
			ret.a[i + 1] += ret.a[i] / base;
			ret.a[i] %= base;
		}
		ret.a[0] = n + 1;
		ret.norm();
		return ret;
	}
	BigInt operator - (BigInt& x)
	{
		BigInt ret = *this;
		int n = a[0];
		for (int i = 1; i <= n; ++i)
		{
			if (i <= x.a[0])
				ret.a[i] -= x.a[i];
			if (ret.a[i] < 0)
			{
				--ret.a[i + 1];
				ret.a[i] += base;
			}
		}
		ret.norm();
		return ret;
	}

	BigInt operator * (BigInt& x)
	{
		BigInt ret;
		ret.fill(a[0] + x.a[0]);
		for (int i = 1; i <= a[0]; ++i)
		{
			for (int j = 1; j <= x.a[0]; ++j)
			{
				ret.a[i + j - 1] += a[i] * x.a[j];
				ret.a[i + j] += ret.a[i + j - 1] / base;
				ret.a[i + j - 1] %= base;
			}
		}
		ret.norm();
		return ret;
	}
	BigInt operator / (int x)
	{
		BigInt ret;
		int n = a[0];
		ret.fill(n);
		int mod = 0;
		for (int i = n; i >= 1; --i)
		{
			mod = mod * base + a[i];
			ret.a[i] = mod / x;
			mod %= x;
		}		
		ret.norm();
		return ret;
	}
	int operator % (int x)
	{
		int n = a[0];
		int mod = 0;
		for (int i = n; i >= 1; --i)
		{
			mod = mod * base + a[i];
			mod %= x;
		}		
		return mod;
	}

	bool operator < (const BigInt& x) const
	{
		if (a[0] != x.a[0])
			return a[0] < x.a[0];
		for (int i = a[0]; i > 0; --i)
			if (a[i] != x.a[i])
				return a[i] < x.a[i];
		return false;
	}
	bool operator > (const BigInt& x) const
	{
		if (a[0] != x.a[0])
			return a[0] > x.a[0];
		for (int i = a[0]; i > 0; --i)
			if (a[i] != x.a[i])
				return a[i] > x.a[i];
		return false;
	}
	bool operator == (const BigInt& x) const
	{
		for (int i = 0; i <= a[0]; ++i)
			if (a[i] != x.a[i])
				return false;
		return true;
	}

	BigInt operator / (BigInt& x)
	{
		BigInt l, r;
		l = BigInt(0);
		r = *this;
		while (r - l > BigInt(1))
		{
			BigInt m = (l + r) / 2;
			
			if (m * x > *this)
				r = m;
			else
				l = m;
		}
		if (r * x > *this)
			return l;
		return r;
	}


	void fill(int n)
	{
		a[0] = n;
		for (int i = 1; i <= n; ++i)
			a[i] = 0;
	}

	void norm()
	{
		while (a[a[0]] == 0 && a[0] > 1)
			--a[0];
	}

	void print()
	{
		printf("%d", a[a[0]]);
		for (int i = a[0] - 1; i >= 1; --i)
			printf("%.4d", a[i]);
	}

	bool is0()
	{
		return a[0] == 1 && a[1] == 0;
	}

	BigInt(char *s)
	{
		int n;
		for (n = 0; s[n]; ++n);
		int h = 1;
		int j = 1;
		a[1] = 0;
		for (int i = n - 1; i >= 0; --i)
		{
			a[j] += h * (s[i] - '0');
			h *= 10;
			if (h >= base)
			{
				h = 1;
				++j;
				a[j] = 0;
			}
		}
		a[0] = j;
		norm();
	}
};

BigInt gcd(BigInt x, BigInt y)
{
	if (y.is0())
		return x;
	if (x < y)
		return gcd(y, x);
	int xx = x % 2;
	int yy = y % 2;
	if (xx == 0 && yy == 0)
		return gcd(x / 2, y / 2) * BigInt(2);
	if (xx == 0)
		return gcd(x / 2, y);
	if (yy == 0)
		return gcd(x, y / 2);
	return gcd(x - y, y);
}


char s[10000];

BigInt a[1010];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; ++t)
	{
		int n;	
		scanf("%d", &n);
		for (int i = 0; i < n; ++i)
		{
			scanf("%s", s);
			a[i] = BigInt(s);
		}
		
		for (int i = 0; i < n; ++i)
		{
			if (a[i] < a[0])
				swap(a[0], a[i]);
		}

		BigInt g = a[1] - a[0];
		for (int i = 2; i < n; ++i)
		{
			g = gcd(g, a[i] - a[0]);
		}
		BigInt y = a[0] - (a[0] / g) * g;
		if (!y.is0())
			y = g - y;
		printf("Case #%d: ", t + 1);
		y.print();
		printf("\n");
	}



	return 0;
}
