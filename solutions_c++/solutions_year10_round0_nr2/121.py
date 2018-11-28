#include <vector>
#include <cstring>
#include <cstdio>
using namespace std;

const int base = 10000;
const int blen = 4;
const int maxbuf = 10000;

typedef vector<int> bignum;
char buf[maxbuf];

void load(char buf[], bignum &a)
{
	int n = strlen(buf);
	int l = 0, t = 1;
	a.clear();
	
	for (int i = n - 1; i >= 0; i--)
	{
		l += (buf[i] - '0') * t;
		t *= 10;
		if ((n - i) % blen == 0 || i == 0)
		{
			a.push_back(l);
			l = 0;
			t = 1;
		}
	}
}

void print(const bignum &a)
{
	int n = a.size();
	if (n == 0)
	{
		printf("0");
		return;
	}
	printf("%d", *(a.end() - 1));
	for (int i = n - 2; i >= 0; i--)
		printf("%0*d", blen, a[i]);
}

void add(const bignum &a, const bignum &b, bignum& c)
{
	int n1 = a.size();
	int n2 = b.size();
	int min = n1 < n2 ? n1 : n2;
	int now = 0;
	c.clear();
	for (int i = 0; i < min; i++)
	{
		now = now + a[i] + b[i];
		c.push_back(now % base);
		now /= base;
	}
	for (int i = min; i < n1; i++)
	{
		now = now + a[i];
		c.push_back(now % base);
		now /= base;
	}
	for (int i = min; i < n2; i++)
	{
		now = now + b[i];
		c.push_back(now % base);
		now /= base;
	}
	while (now)
	{
		c.push_back(now % base);
		now /= base;
	}
}

void sub(const bignum &a, const bignum &b, bignum &c)
{
	int n1 = a.size();
	int n2 = b.size();
	int now = 0;
	c.clear();
	for (int i = 0; i < n2; i++)
	{
		now = now + a[i] - b[i];
		if (now < 0)
		{
			c.push_back(now + base);
			now = -1;
		}
		else
		{
			c.push_back(now);
			now = 0;
		}
	}
	for (int i = n2; i < n1; i++)
	{
		now = now + a[i];
		if (now < 0)
		{
			c.push_back(now + base);
			now = -1;
		}
		else
		{
			c.push_back(now);
			now = 0;
		}
	}
	while (c.size() > 0 && *(c.end() - 1) == 0)
		c.pop_back();
}

void lshift(bignum &a)
{
	int n = a.size();
	int now = 0;
	for (int i = 0; i < n; i++)
	{
		now = now + a[i] * 10;
		a[i] = now % base;
		now /= base;
	}
	while (now)
	{
		a.push_back(now % base);
		now /= base;
	}
}

void rshift(bignum &a)
{
	int n = a.size();
	int now = 0;
	for (int i = n - 1; i >= 0; i--)
	{
		now = now + a[i];
		a[i] = now / 10;
		now = now % 10 * base;
	}
	while (a.size() > 0 && *(a.end() - 1) == 0)
		a.pop_back();
}

bool gr(const bignum &a, const bignum &b)
{
	if (a.size() > b.size()) return true;
	else
	if (a.size() < b.size()) return false;
	
	int n = a.size();
	for (int i = n - 1; i >= 0; i--)
		if (a[i] > b[i]) return true;
		else
		if (a[i] < b[i]) return false;
	return false;
}

void remain(const bignum &a, const bignum &b, bignum &c)
{
	c = a;
	bignum d = b;
	while (!gr(d, a)) lshift(d);
	while (d != b)
	{
		rshift(d);
		bignum res;
		while (!gr(d, c))
		{
			sub(c, d, res);
			c = res;
		}
	}
}

void gcd(const bignum &a, const bignum &b, bignum &c)
{
	if (b.size() == 0) c = a;
	else
	{
		bignum r;
		remain(a, b, r);
		gcd(b, r, c);
	}
}

int n;

int main()
{
	int testnumber;
	bignum a, b, c, g, t;
	
	freopen("B-large.in", "r", stdin);
	freopen("b.out", "w", stdout);
	scanf("%d", &testnumber);
	for (int testcount = 0; testcount < testnumber; testcount++)
	{
		g.clear();
		scanf("%d", &n);
		scanf("%s", buf);
		load(buf, a);
		for (int i = 1; i < n; i++)
		{
			scanf("%s", buf);
			load(buf, b);
			if (gr(a, b)) sub(a, b, c);
			else sub(b, a, c);
			gcd(g, c, t);
			g = t;
		}
		printf("Case #%d: ", testcount + 1);
		if (g.size() == 0) print(bignum());
		else
		{
			remain(a, g, t);
			if (t.size() == 0) print(bignum());
			else
			{
				sub(g, t, c);
				print(c);
			}
		}
		printf("\n");
	}
	
	return 0;
}
