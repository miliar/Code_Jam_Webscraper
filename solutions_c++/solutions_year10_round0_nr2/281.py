#include <stdio.h>
#include <string.h>

class bigint
{
	int data[100], dp;

public:
	bigint ()
	{
		dp = 1; data[0] = 0;
	}

	bigint (int a)
	{
		dp = 0;
		while (a) data[dp ++] = a % 10, a /= 10;
		if (!dp) data[dp ++] = 0;
	}

	bigint (char* s)
	{
		dp = 0;
		for (int i = strlen(s) - 1; i >= 0; i --)
			data[dp ++] = s[i] - '0';
	}

	bool is_zero () const
	{
		return dp == 1 && data[0] == 0;
	}

	bool less_than (const bigint& a)
	{
		if (dp < a.dp) return true;
		if (dp > a.dp) return false;
		for (int i = dp - 1; i >= 0; i --)
			if (data[i] != a.data[i])
				return data[i] < a.data[i];
		return false;
	}

	void operator <<= (int x)
	{
		for (int i = dp - 1; i >= 0; i --)
			data[i + x] = data[i];
		for (int i = 0; i < x; i ++)
			data[i] = 0;
		dp += x;
	}

	void operator -= (const bigint& a)
	{
		int j = 0;
		for (int i = 0; i < dp; i ++)
		{
			j = j + data[i];
			if (i < a.dp)
				j -= a.data[i];
			if (j < 0)
			{
				data[i] = j + 10;
				j = -1;
			}
			else
			{
				data[i] = j;
				j = 0;
			}
		}
		while (dp > 1 && data[dp - 1] == 0)
			dp --;
	}

	void remainder (const bigint& b)
	{
		for (int i = dp - b.dp; i >= 0; i --)
		{
			bigint c = b;
			c <<= i;
			while (!(this -> less_than(c)))
				this ->operator -= (c);
		}
	}

	bigint difference (const bigint& b)
	{
		if (this -> less_than(b))
		{
			bigint c = b;
			c -= *this;
			return c;
		}
		
		bigint c = *this;
		c -= b;
		return c;
	}

	void dump () const
	{
		for (int i = dp - 1; i >= 0; i --)
			printf ("%d", data[i]);
	}
};

bigint gcd (const bigint& a, const bigint& b)
{
	if (b.is_zero())
		return a;
	bigint c = a;
	c.remainder(b);
	return gcd(b, c);
}

int main ()
{
	int n;

	freopen ("Blarge.in", "r", stdin);
	freopen ("Blarge.out", "w", stdout);

	scanf ("%d", &n);
	for (int i = 0; i < n; i ++)
	{
		int k;
		scanf ("%d", &k);

		bigint a, b, c, d;
		char buf[256];

		a = 0;
		for (int j = 0; j < k; j ++)
		{
			scanf ("%s", buf);
			b = bigint(buf);

			if (j)
			{
				d = c;
				bigint e = d.difference(b);
				a = gcd(a, d.difference(b));
			}
			else
				c = b;
		}

		b.remainder(a);
		c = a;
		c -= b;
		c.remainder(a);

		printf ("Case #%d: ", i + 1);
		c.dump ();
		printf ("\n");
	}

	return 0;
}