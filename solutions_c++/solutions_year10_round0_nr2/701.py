#include <stdio.h>
#include <string.h>
#include <stdlib.h>

const int MAX_NUMBER_OF_DIGITS = 200;

const int LB = 8;
const int L = MAX_NUMBER_OF_DIGITS/LB+1;
const long long B = 100000000;

//////////////////////// Exception
#define SUM 0
#define SUB 1
#define MUL 2
#define MUL_INT 3
void exception(int OPER)
{
	printf("Out of bound! operator ");
	if (OPER == SUM)
		printf("+\n");
	if (OPER == SUB)
		printf("-\n");
	if (OPER == MUL)
		printf("*\n");
	if (OPER == MUL_INT)
		printf("* int\n");
	exit(0);
}
//////////////////////////////////

struct BigInt
{
	int st;
	long long d[L];
	void clear()
	{
		st = L;
		memset(d, 0, sizeof(d));
	}
	BigInt()
	{
		clear();
	}
	void correct()
	{
		for (st = 0; st < L && d[st] == 0; st++);
	}
	void read()
	{
		int i, j, k;
		long long ten = 1;
		char s[MAX_NUMBER_OF_DIGITS+10];
		scanf("%s", s);
		k = 0;
		j = L-1;
		clear();
		for (i = strlen(s)-1; i >= 0; i--)
		{
			d[j] = d[j]+(s[i]-'0')*ten;
			k++;
			ten *= 10;
			if (k == LB)
			{
				k = 0;
				ten = 1;
				j--;
			}
		}
		correct();
	}
	void print()
	{
		if (st == L)
		{
			printf("0\n");
			return;
		}
		int i;
		printf("%lld", d[st]);
		for (i = st+1; i < L; i++)
			printf("%08lld", d[i]);
		putchar('\n');
	}
};

bool operator < (BigInt a, BigInt b)
{
	if (a.st < b.st)
		return 0;
	if (a.st > b.st)
		return 1;
	int i;
	for (i = a.st; i < L; i++)
	{
		if (a.d[i] < b.d[i])
			return 1;
		if (a.d[i] > b.d[i])
			return 0;
	}
	return 0;
}
bool operator == (BigInt a, BigInt b)
{
	if (a.st != b.st)
		return 0;
	int i;
	for (i = a.st; i < L; i++)
		if (a.d[i] != b.d[i])
			return 0;
	return 1;
}
bool operator > (BigInt a, BigInt b)
{
	if (a.st < b.st)
		return 1;
	if (a.st > b.st)
		return 0;
	int i;
	for (i = a.st; i < L; i++)
	{
		if (a.d[i] < b.d[i])
			return 0;
		if (a.d[i] > b.d[i])
			return 1;
	}
	return 0;
}
bool operator <= (BigInt a, BigInt b)
{
	if (a.st < b.st)
		return 0;
	if (a.st > b.st)
		return 1;
	int i;
	for (i = a.st; i < L; i++)
	{
		if (a.d[i] < b.d[i])
			return 1;
		if (a.d[i] > b.d[i])
			return 0;
	}
	return 1;
}
bool operator >= (BigInt a, BigInt b)
{
	if (a.st < b.st)
		return 1;
	if (a.st > b.st)
		return 0;
	int i;
	for (i = a.st; i < L; i++)
	{
		if (a.d[i] < b.d[i])
			return 0;
		if (a.d[i] > b.d[i])
			return 1;
	}
	return 1;
}
BigInt operator + (BigInt a, BigInt b)
{
	int m, i;
	BigInt c;
	long long k, s;
	if (a.st < b.st)
		m = a.st;
	else
		m = b.st;
	k = 0;
	for (i = L-1; i >= m; i--)
	{
		s = a.d[i]+b.d[i]+k;
		c.d[i] = s%B;
		k = s/B;
	}
	if (k)
	{
		if (m == 0)
			exception(SUM);
		c.d[--m] = k;
	}
	c.st = m;
	return c;
}
BigInt operator - (BigInt a, BigInt b)
{
	if (a < b)
		exception(SUB);
	int i;
	BigInt c;
	for (i = L-1; i >= a.st; i--)
	{
		if (a.d[i] < b.d[i])
		{
			a.d[i] += B;
			a.d[i-1]--;
		}
		c.d[i] = a.d[i]-b.d[i];
	}
	c.correct();
	return c;
}
BigInt operator * (BigInt a, BigInt b)
{
	if (a.st+b.st <= L-1)
		exception(MUL);
	BigInt c;
	long long m;
	int i, j;
	for (i = L-1; i >= a.st; i--)
		for (j = L-1; j >= b.st; j--)
		{
			m = a.d[i]*b.d[j]+c.d[i+j-L+1];
			c.d[i+j-L+1] = m%B;
			c.d[i+j-L] += m/B;
		}
	c.correct();
	return c;
}
BigInt operator * (BigInt a, long long x)
{
	int i;
	BigInt ret;
	long long m;
	for (i = L-1; i >= a.st; i--)
	{
		m = a.d[i]*x+ret.d[i];
		ret.d[i] = m%B;
		ret.d[i-1] += m/B;
	}
	ret.correct();
	if (ret.st == 0)
		exception(MUL_INT);
	return ret;
}
BigInt operator / (BigInt a, long long x)
{
	int i;
	BigInt ret;
	long long m = 0;
	for (i = a.st; i < L; i++)
	{
		m = m*B+a.d[i];
		ret.d[i] = m/x;
		m %= x;
	}
	ret.correct();
	return ret;
}

BigInt ONE;
BigInt operator / (BigInt a, BigInt b)
{
	BigInt ret, p, q, k;
	p.clear();
	q = a;
	ONE.d[L-1] = 1;
	ONE.correct();
	while ((p+ONE) < q)
	{
		k = (p+q)/2;
		if ((k*b) == a)
			return k;
		if ((k*b) < a)
			p = k;
		else
			q = k;
	}
	if ((b*q) <= a)
		return q;
	return p;
}

BigInt operator % (BigInt a, BigInt b)
{
	return a-((a/b)*b);
}
BigInt gcd(BigInt a, BigInt b)
{
	BigInt temp;
	while (b.st < L)
	{
		a = a%b;
		temp = a;
		a = b;
		b = temp;
	}
	return a;
}
BigInt t[1010];
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
/*	BigInt a, b;
	a.read();
	b.read();
	BigInt c = a%b;
	c.print();*/
	BigInt g, ans;
	int n, c, l, i, j;
	ONE.d[L-1] = 1;
	ONE.correct();
	scanf("%d", &c);
	for (l = 1; l <= c; l++)
	{
		scanf("%d", &n);
		for (i = 0; i < n; i++)
			t[i].read();
		g.clear();
		for (i = 1; i < n; i++)
			if (t[i] > t[0])
				g = gcd(t[i]-t[0], g);
			else
				g = gcd(t[0]-t[i], g);
		for (i = j = 0; i < n; i++)
			if (t[i] > t[j])
				j = i;
		ans = ((t[j]+g-ONE)/g)*g - t[j];
		printf("Case #%d: ", l);
		ans.print();
	}
	return 0;
}
