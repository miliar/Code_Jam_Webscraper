#include <sstream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <string>

using namespace std;

#define MAXN 1024

const int DIG = 4;
const int BASE = 10000; // BASE**3 < 2**51
const int TAM = 2048;

struct bigint { // start: ea95411d6424e3e46ba34e801639db49
int v[TAM], n;
bigint(int x = 0): n(1) { // start: abccfeb09be9c7eda1f70aea80948972
memset(v, 0, sizeof(v));
v[n++] = x; fix();
}
bigint(char *s): n(1) { // start: 959c8166b28135e983fda4929f6c66a0
memset(v, 0, sizeof(v));
int sign = 1;
while (*s && !isdigit(*s)) if (*s++ == '-') sign *= -1;
char *t = strdup(s), *p = t + strlen(t);
while (p > t) {
*p = 0; p = max(t, p - DIG);
sscanf(p, "%d", &v[n]);
v[n++] *= sign;
}
free(t); fix();
}
bigint& fix(int m = 0) { // start: c48040a2d18d109614097bd8473eb48a
n = max(m, n);
int sign = 0;
for (int i = 1, e = 0; i <= n || (e && (n = i)); i++) {
v[i] += e; e = v[i] / BASE; v[i] %= BASE;
if (v[i]) sign = (v[i] > 0) ? 1 : -1;
}
for (int i = 1; i < n; i++)
if (v[i] * sign < 0) { v[i] += sign * BASE; v[i+1] -= sign; }
while (n && !v[n]) n--;
return *this;
}
int cmp (const int& x, const int& y) const {
	return x - y;
}
int cmp(const bigint& x=0) const { // start: 0af6101d468cbc9ce27f720d4e1c4d11
int i = max(n, x.n), t = 0;
while (1) if ((t = cmp(v[i], x.v[i])) || i-- == 0) return t;
}
bool operator <(const bigint& x) const { return cmp(x) < 0; }
bool operator ==(const bigint& x) const { return cmp(x) == 0; }
bool operator !=(const bigint& x) const { return cmp(x) != 0; }
operator string() const { // start: 29d6dcb9a4f970287d0a3fcec244433b
	ostringstream s; s << v[n];
	for (int i = n - 1; i > 0; i--) {
		s.width(DIG); s.fill('0'); s << abs(v[i]);
	}
	return s.str();
}
friend ostream& operator <<(ostream& o, const bigint& x) {
return o << (string) x;
}
bigint& operator +=(const bigint& x) {
for (int i = 1; i <= x.n; i++) v[i] += x.v[i];
return fix(x.n);
}
bigint operator +(const bigint& x) { return bigint(*this) += x; }
bigint& operator -=(const bigint& x) {
for (int i = 1; i <= x.n; i++) v[i] -= x.v[i];
return fix(x.n);
}
bigint operator -(const bigint& x) { return bigint(*this) -= x; }
bigint operator -() { bigint r = 0; return r -= *this; }
void ams(const bigint& x, int m, int b) { // *this += (x * m) << b;
for (int i = 1, e = 0; (i <= x.n || e) && (n = i + b); i++) {
v[i+b] += x.v[i] * m + e; e = v[i+b] / BASE; v[i+b] %= BASE;
}
}
bigint operator *(const bigint& x) const {
bigint r;
for (int i = 1; i <= n; i++) r.ams(x, v[i], i-1);
return r;
}
bigint& operator *=(const bigint& x) { return *this = *this * x; }
// cmp(x / y) == cmp(x) * cmp(y); cmp(x % y) == cmp(x);
bigint div(const bigint& x) { // start: 9cb6d7a22a046e666a8e9e85193bc60f
if (x == 0) return 0;
bigint q; q.n = max(n - x.n + 1, 0);
int d = x.v[x.n] * BASE + x.v[x.n-1];
for (int i = q.n; i > 0; i--) {
int j = x.n + i - 1;
q.v[i] = int((v[j] * double(BASE) + v[j-1]) / d);
ams(x, -q.v[i], i-1);
if (i == 1 || j == 1) break;
v[j-1] += BASE * v[j]; v[j] = 0;
}
fix(x.n); return q.fix();
}
bigint& operator /=(const bigint& x) { return *this = div(x); }
bigint& operator %=(const bigint& x) { div(x); return *this; }
bigint operator /(const bigint& x) { return bigint(*this).div(x); }
bigint operator %(const bigint& x) { return bigint(*this) %= x; }
bigint pow(int x) { // start: 3a233cf5d13d2d59a0ce923e586abefd
if (x < 0) return (*this == 1 || *this == -1) ? pow(-x) : 0;
bigint r = 1;
for (int i = 0; i < x; i++) r *= *this;
return r;
}
bigint root(int x) { // start: a36949a29165de09212495289d176d64
if (cmp() == 0 || cmp() < 0 && x % 2 == 0) return 0;
if (*this == 1 || x == 1) return *this;
if (cmp() < 0) return -(-*this).root(x);
bigint a = 1, d = *this;
while (d != 1) {
bigint b = a + (d /= 2);
if (cmp(b.pow(x)) >= 0) { d += 1; a = b; }
}
return a;
}
};

bigint gcd(bigint x, bigint y)
{
	if (y == 0) return x;

	if (x < y) return gcd(y,x);

	return gcd(y, x % y);
}

bigint t[MAXN];

int main (void)
{
	int n, c;
	char buf[1024];
	bigint mdc, maior;
		
	scanf ("%d", &c);

	for (int testes = 1; testes <= c; testes++)
	{
		scanf ("%d", &n);

		for (int i = 0; i < n; i++)
		{
			scanf (" %s", buf);

			t[i] = *(new bigint(buf));
		}

		for (int i = 1; i < n; i++)
		{
			if (t[i] < t[0])
			{
				mdc = t[0] - t[i];
				break;
			}
			else if (t[0] < t[i])
			{
				mdc = t[i] - t[0];
				break;
			}
		}

		for (int i = 0; i < n; i++)
		{
			for (int j = i+1; j < n; j++)
			{
				if (t[i] < t[j])
					mdc = gcd (mdc, t[j] - t[i]);
				else if (t[j] < t[i])
					mdc = gcd (mdc, t[i] - t[j]);
			}
		}

		if (mdc == 1)
			printf ("Case #%d: 0\n", testes);
		else
		{
			maior = *(new bigint(0));
			for (int i = 0; i < n; i++)
			{
				if (maior < mdc - t[i] % mdc)
					maior = mdc - (t[i] % mdc);
			}

			printf ("Case #%d: %s\n", testes, ((string) (maior % mdc)).c_str());
		}
	}

	return 0;
}
