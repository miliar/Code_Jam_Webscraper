#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;
const int BASE = 1000000000;
const int DIGS = 9;
const int LEN = 10;

struct bignum
{
	int t[LEN];
	int l;
};
bignum ZERO;
void wypisz(bignum a)
{
	printf("%d", a.t[a.l-1]);
	for(int i = a.l-2; i >= 0; i--)
		printf("%0*d", DIGS, a.t[i]);
}
void czytaj(bignum &a)
{
	char s[DIGS*LEN+1];
	scanf("%s", s);
	int dl = strlen(s);
	a.l = dl / DIGS;
	if(dl % DIGS)
		a.l++;
	dl--;
	for(int i = 0; i < a.l; i++)
	{
		a.t[i] = 0;
		for(int k = max(0, dl-DIGS+1); k <= dl; k++)
			a.t[i] = 10*a.t[i] + (s[k] - '0');
		dl -= DIGS;
	}
}
bignum operator- (bignum a, bignum b)
{
	bignum w;
	w.l = a.l;
	int c = 0;
	for(int i = 0; i < a.l; i++)
	{
		if(i < b.l)
			w.t[i] = a.t[i] - b.t[i] + c;
		else
			w.t[i] = a.t[i] + c;
			if(w.t[i] < 0)
			{
				w.t[i] += BASE;
				c = -1;
			}
			else
				c = 0;
	}
	while(w.l > 1 && w.t[w.l-1] == 0)
		w.l--;
	return w;
}
bool operator< (bignum x, bignum y)
{
	if (x.l < y.l)
		return true;
	if(x.l > y.l)
		return false;
	int i = x.l - 1;
	while (i >= 0 && x.t[i] == y.t[i])
		i--;
	if (i < 0)
		return false;
	if (x.t[i] < y.t[i])
		return true;
	return false;
}

bool operator== (bignum x, bignum y)
{
	return !(x < y) && !(y < x);
}

bignum nwd(bignum a, bignum b)
{
	while(!(a == ZERO) && !(b == ZERO))
	{
		if(a < b)
			b = b - a;
		else
			a = a - b;
	}
	if(a == ZERO)
		return b;
	return a;
}
int main()
{
	ZERO.t[0] = 0;
	ZERO.l = 1;
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++)
	{
		int n;
		scanf("%d", &n);
		bignum a, b, T[1005];
		for(int j = 0; j < n; j++)
		{
			if(j)
				b = a;
			czytaj(a);
			if(j)
			{
				if(b < a)
					T[j] = a - b;
				else
					T[j] = b - a;
			}
		}
		bignum NWD = T[1];
		for(int j = 2; j < n; j++)
			NWD = nwd(NWD, T[j]);
		while(NWD < a)
			a = a - NWD;
			printf("Case #%d: ", i);
		wypisz(NWD - a);
		printf("\n");
	}
	return 0;
}
