#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>

using namespace std;

const int base = 10;

struct tlong {
	int len;
	int val[100];
	int clear () {
		len = 0;
		memset (val, 0, sizeof (val));
		return 0;
	}
};

tlong fstring (string x) {
	tlong a; a.clear ();
	a.len = x.size ();
	for (int i = 0; i < a.len; i++) a.val[a.len - i - 1] = x[i] - '0';
	return a;
}

tlong fint (int x) {
	tlong a; a.clear ();
	a.len = 0;
	while (x) {
		a.val[a.len++] = x % 10;
		x /= 10;
	}
	return a;
}

int print (tlong a, bool nextline) {
	if (a.len == 0) printf ("0");
	for (int i = a.len; i > 0; i--)
		printf ("%d", a.val[i - 1]);
	if (nextline) printf ("\n");
}

bool operator>= (tlong a, tlong b) {
	if (a.len > b.len) return true;
	if (a.len < b.len) return false;
	for (int i = a.len - 1; i >= 0; i--) {
		if (a.val[i] > b.val [i]) return true;
		if (a.val[i] < b.val [i]) return false;
	}
	return true;
}

tlong operator+ (tlong a, tlong b) {
	tlong c;
	c.clear ();
	c.len = max (a.len, b.len);
	int r = 0;
	for (int i = 0; i < c.len; i++) {
		c.val[i] = a.val[i] + b.val[i] + r;
		r = c.val[i] / 10;
		c.val[i] %= 10;
	}
	while (r) {
		c.val[c.len] = r % 10;
		c.len++;
		r /= 10;
	}
	return c;		
}

tlong operator- (tlong a, tlong b) {
	tlong c;
	c.clear ();
	c.len = max (a.len, b.len);
	for (int i = 0; i < c.len; i++) {
		c.val[i] = c.val[i] + a.val[i] - b.val[i];
		if (c.val[i] < 0) {
			c.val[i + 1]--;
			c.val[i] += 10;
		}
	}
	while (c.len > 0 && c.val[c.len - 1] == 0) c.len--;
	return c;		
}

tlong operator* (tlong a, tlong b) {
	tlong c; c.clear ();
	c.len = a.len + b.len - 1;
	for (int i = 0; i < a.len; i++)
		for (int j = 0; j < b.len; j++)
			c.val[i + j] += a.val[i] * b.val[j];
	int r = 0;
	for (int i = 0; i < c.len; i++) {
		c.val[i] += r;
		r = c.val[i] / 10;
		c.val[i] %= 10;
	}
	while (r) {
		c.val[c.len] = r % 10;
		c.len++;
		r /= 10;
	}
	return c;		
}

tlong operator% (tlong a, tlong b) {
	tlong c; c.clear ();
	for (int i = a.len - 1; i >= 0; i--) {
		for (int j = c.len; j > 0; j--)
			c.val[j] = c.val[j - 1];
		c.val[0] = a.val[i];
		c.len++;
		while (c.len > 0 && c.val[c.len - 1] == 0) c.len--;
		while (c >= b) c = c - b;
	}
	return c;		
}

tlong operator/ (tlong a, tlong b) {
	tlong d; d.clear ();
	tlong c; c.clear ();
	for (int i = a.len - 1; i >= 0; i--) {
		for (int j = c.len; j > 0; j--)
			c.val[j] = c.val[j - 1];
		c.val[0] = a.val[i];
		c.len++;
		while (c.len > 0 && c.val[c.len - 1] == 0) c.len--;
		int k = 0;
		while (c >= b) {
			c = c - b;
			k++;
		}
		if (d.len > 0 || k > 0) {
			d.val[d.len] = k;
			d.len++;
		}
	}
	for (int i = 0; d.len - i - 1 > i; i++) swap (d.val[i], d.val[d.len - i - 1]);
	return d;
}

tlong operator* (tlong a, int b) {
	int r = 0;
	for (int i = 0; i < a.len; i++) {
		a.val[i] = a.val[i] * b + r;
		r = a.val[i] / base;
		a.val[i] = a.val[i] % base;
	}
	while (r) {
		a.val[a.len] = r % base;
		a.len++;
		r /= base;
	}
	while (a.len > 0 && a.val[a.len - 1] == 0) a.len--;
	return a;		
}

tlong operator/ (tlong a, int b) {
	tlong d; d.clear ();
	long long c = 0;
	for (int i = a.len - 1; i >= 0; i--) {
		c = c * base + a.val[i];
		int k = c / b;
		c %= b;
		if (d.len > 0 || k > 0) {
			d.val[d.len] = k;
			d.len++;
		}
	}
	for (int i = 0; d.len - i - 1 > i; i++) swap (d.val[i], d.val[d.len - i - 1]);
	return d;
}

tlong gcd (tlong a, tlong b) {
	if (a.len == 0) return b; else return gcd (b % a, a);
}

tlong x[1000];

int main () {
	int tt;
	scanf ("%d", &tt);
	for (int it = 1; it <= tt; it++) {
		int n;
		scanf ("%d", &n);
		for (int i = 0; i < n; i++) {
			string s;
			cin >> s;
			x[i] = fstring (s);
		}
		tlong cur;
		cur.len = 0;
		for (int i = 0; i + 1 < n; i++)
			if (x[i + 1] >= x[i])
				cur = gcd (cur, x[i + 1] - x[i]);
			else
				cur = gcd (cur, x[i] - x[i + 1]);
		tlong y = ((x[0] + cur - fint (1)) / cur) * cur - x[0];
		printf ("Case #%d: ", it);
		print (y, true);
	}
}