#include <cstdio>
#include <string>
#include <math.h>
#include <vector>
#include <map>
#include <set>

using namespace std;

// comment __________________

int testnum;

struct bign
{
	int len;
	int d[10000];

	bign(int k)
	{
		memset(d, 0, sizeof(d));
		len = 0;
		while (k)
		{
			d[len++] = k % 10;
			k /= 10;
		}
	}

};

	bign add(bign a, bign b)
	{
		bign c(0);
		int d = 0;
		c.len = max(a.len, b.len);
		for (int i = 0; i <= c.len; i++)
		{
			d += a.d[i] + b.d[i];
			c.d[i] = d % 10;
			d /= 10;
		}
		if (c.d[c.len])
			c.len++;
		return c;
	}

	bign mult(bign a, bign b)
	{
		bign c(0);
		if (!a.len || !b.len)
			return c;
		c.len = a.len + b.len - 1;
		for (int i = 0; i < a.len; i++)
			for (int j = 0; j < b.len; j++)
				c.d[i + j] += a.d[i] * b.d[j];
		int d = 0;
		for (int i = 0; i <= c.len; i++)
		{
			d += c.d[i];
			c.d[i] = d % 10;
			d /= 10;
		}
		if (c.d[c.len])
			c.len++;
		return c;
	}

string solve(string s)
{
	int val[256];
	int res[800];
	int mx = 1;
	int zero = 0;
	memset(val, 255, sizeof(val));
	for (int i = 0; i < s.length(); i++)
	{
		int digit;
		if (val[s[i]] + 1)
			digit = val[s[i]];
		else if (!zero && i)
		{
			zero = 1;
			val[s[i]] = 0;
			digit = 0;
		}
		else 
		{
			val[s[i]] = mx;
			digit = mx++;
		}
		res[i] = digit;
	}
	bign base(mx);
	bign degr(1);
	bign r(0);
	for (int i = 0; i < s.length(); i++)
	{
		bign t(res[s.length() - i - 1]);
		r = add(r, mult(degr, t));
		degr = mult(degr, base);
	}
	string ress = "";
	for (int i = r.len - 1; i >= 0; i--)
		ress += '0' + r.d[i];
	return ress;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &testnum);
	char s[100];
	for (int testcount = 0; testcount < testnum; testcount++)
	{
		scanf("%s", s);
		string ss = s;
		printf("Case #%d: %s\n", testcount + 1, solve(ss).c_str());
	}
	return 0;
}