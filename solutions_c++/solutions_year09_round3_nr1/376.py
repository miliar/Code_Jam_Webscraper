#include <cstdio>
#include <string>

void OpenFiles()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
}

char temp[5000];
std::string scanString()
{
	gets(temp);
	return std::string(temp);
}

char val[256];

const int base = 10000;

struct bignum
{
	int digits[4000];
	int len;

	void init(int num = 0)
	{
		clear();
		len = 1;
		digits[0] = num;
	}

	void mult(int num)
	{
		int k = 0;
		for (int i = 0; i < len; i++)
		{
			digits[i] = (digits[i]) * num + k;
			k = digits[i] / base;
			digits[i] %= base;
		}

		if (k > 0) 
			digits[len++] = k;
	}

	int digit(int pos)
	{
		if (pos < len)
			return digits[pos];
		else
			return 0;
	}

	void add(bignum & x)
	{
		len = std::max(x.len, len);
		int d = 0;
		for (int i = 0; i < len; i++)
		{
			digits[i] = digit(i) + x.digit(i) + d;
			d = digits[i] / base;
			digits[i] %= base;
		}

		if (d > 0)
			digits[len++] = d;
	}

	void clear()
	{
		for (int i = 0; i < len; i++)
			digits[i] = 0;
		len = 0;
	}

	void copy(bignum & from)
	{	
		clear();
		len = from.len;
		for (int i = 0; i < from.len; i++)
			digits[i] = from.digits[i];
	}

	void print()
	{
		printf("%d", digits[len-1]);
		for (int i = len-2; i >= 0; i--)
			printf("%.4d", digits[i]);
	}
};

int code(char c)
{
	int code = c;
	if (code < 0)
		code = 255 + code;
	return code;
}

bignum res;
bignum pow10;
bignum t;

bignum solve(std::string s)
{
	memset(val, -1, sizeof(val));
	int cur = 1;
	int inc = 0;
	for (int i = 0; i < s.size(); i++)
	{
		int code = ::code(s[i]);
		if (val[code] == -1) 
		{
			if (cur != 2)
			{
				val[code] = cur++;				
			}
			else
			{
				if (inc == 0)
				{
					val[code] = 0;
					inc++;
				}
				else
				{
					val[code] = 2;
					cur++;
				}
			}
		}		
	}

	res.init(0);
	pow10.init(1);
	t.init(0);
	
	for (int i = s.size()-1; i >= 0; i--)
	{
		t.copy(pow10);		
		int v = val[code(s[i])];
		t.mult(v);
		res.add(t);
		pow10.mult(cur);
	}

	return res;
}

int main()
{
	OpenFiles();
	int t;
	scanf("%d\n", &t);
	for (int i = 0; i < t; i++)
	{
		std::string s = scanString();
		printf("Case #%d: ", i+1);
		solve(s).print();
		printf("\n");
	}
	
	return 0;
}