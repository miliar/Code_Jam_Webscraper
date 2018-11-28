#include <stdio.h>
#include <memory.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

#define FOR(i, n)	for (int i = 0; i < (int) (n); i++)
#define RFOR(i, n)	for (int i = (int) (n) - 1; i >= 0; i--)
#define CL(x)		memset(x, 0, sizeof(x))
#define CLX(x, v)	memset(x, v, sizeof(x))
#define ALL(x)		(x).begin(), (x).end()
#define PB			push_back
#define MP			make_pair

typedef long long LL;
typedef unsigned long long UL;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

/////////////////////////////////////////////////////////////

const int SIZE = 50;
const int BASE = 32;

struct big
{
	unsigned m[SIZE];

	big()
	{
		CL(m);
	}

	big(unsigned a)
	{
		CL(m);
		m[0] = a;
	}

	unsigned & operator [] (int i)
	{
		return m[i];
	}

};

bool operator < (big a, big b)
{
	int i = SIZE - 1;
	while (i  &&  a[i] == b[i]) i--;
	return a[i] < b[i];
}

bool operator <= (big a, big b)
{
	int i = SIZE - 1;
	while (i  &&  a[i] == b[i]) i--;
	return a[i] <= b[i];
}

bool operator == (big a, big b)
{
	int i = SIZE - 1;
	while (i  &&  a[i] == b[i]) i--;
	return a[i] == b[i];
}

big operator + (big a, big b)
{
	big res;
	UL ofs = 0;
	FOR(i, SIZE)
	{
		ofs += (UL) a[i] + b[i];
		res[i] = ofs;
		ofs >>= BASE;
	}
	return res;
}

big operator - (big a, big b)
{
	big res;
	UL ofs = 1;
	FOR(i, SIZE)
	{
		ofs += (UL) a[i] + ~b[i];
		res[i] = ofs;
		ofs >>= BASE;
	}
	return res;
}

big operator * (big a, unsigned b)
{
	big res;
	UL ofs = 0;
	FOR(i, SIZE)
	{
		ofs += (UL) a[i] * b;
		res[i] = ofs;
		ofs >>= BASE;
	}
	return res;
}

big operator * (big a, big b)
{
	big res;
	FOR(i, SIZE)
	{
		UL ofs = 0;
		FOR(j, SIZE) if (i + j < SIZE)
		{
			ofs += res[i + j] + (UL) a[i] * b[j];
			res[i + j] = ofs;
			ofs >>= BASE;
		}
	}
	return res;
}

big operator / (big a, unsigned b)
{
	big res;
	UL ofs = 0;
	RFOR(i, SIZE)
	{
		ofs = (ofs << BASE) + a[i];
		res[i] = ofs / b;
		ofs -= (UL) res[i] * b;
	}
	return res;
}

unsigned operator % (big a, unsigned b)
{
	big res;
	UL ofs = 0;
	RFOR(i, SIZE)
	{
		ofs = (ofs << BASE) + a[i];
		res[i] = ofs / b;
		ofs -= (UL) res[i] * b;
	}
	return ofs;
}

big operator / (big a, big b)
{
	big res;

	int k = 0;
	while (b < a)
	{
		b = b * 2;
		k++;
	}

	while (k >= 0)
	{
		if (b <= a)
		{
			a = a - b;
			res[k >> 5] |= 1 << (k & 31);
		}
		b = b / 2;
		k--;
	}

	return res;
}

big operator % (big a, big b)
{
	big res;

	int k = 0;
	while (b < a)
	{
		b = b * 2;
		k++;
	}

	while (k >= 0)
	{
		if (b <= a)
		{
			a = a - b;
			res[k >> 5] |= 1 << (k & 31);
		}
		b = b / 2;
		k--;
	}

	return a;
}

big scan(char *s)
{
	big res;
	for (int i = 0; s[i]; i++)
		res = res * 10 + (unsigned) (s[i] - '0');
	return res;
}

void print(big a)
{
	string s;
	while (0 < a)
	{
		s = (char) ('0' + (a % 10)) + s;
		a = a / 10;
	}
	if (s == "") printf("0\n");
	else printf("%s\n", s.c_str());
}

///////////////////////////////////////////////////////////////

const int N = 1000 + 5;

int n, k;
big a[N];
big b[N * N];

big nod(big a, big b)
{
	while (0 < b)
	{
		big t = a % b;
		a = b;
		b = t;
	}
	return a;
}

void solve()
{
	k = 0;
	FOR(i, n) FOR(j, n)
	{
		if (i <= j) continue;
		b[k++] = (a[i] < a[j]) ? (a[j] - a[i]) : (a[i] - a[j]);
	}

	big x = b[0];
	FOR(i, k) x = nod(x, b[i]);

	big y; 
	y[SIZE - 1] = 1 << 16;

	FOR(i, n)
	{
		big q = a[i] / x;
		if (q * x < a[i]) q = q + 1;
		big yy = q * x - a[i];
		if (yy < y) y = yy;
	}

	print(y);
}

int main()
{
//#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
//#endif

	int tt;
	scanf("%d", &tt);

	FOR(i, tt)
	{
		scanf("%d", &n);
		FOR(j, n)
		{
			static char buf[1 << 10];
			scanf("%s", buf);
			a[j] = scan(buf);
		}
		printf("Case #%d: ", i+1);
		solve();
	}

	return 0;
}
