#include <cstdio>
#include <cstring>
#include <stack>
#include <algorithm>
#define MOD 10
using namespace std;

struct liczba {
	liczba() { znak = '+'; }
	char znak;
	int len, tab[200];
};

bool operator==(const liczba &a, const liczba &b) {
	if(a.len != b.len) return false;
	for(int i=a.len-1; i>=0; --i)
		if(a.tab[i] != b.tab[i]) return false;
	return true;
}

bool operator!=(const liczba &a, const liczba &b) {
	return !(a == b);
}

struct binar {
	int len;
	char tab[360];
};

void wczytaj(liczba &a) {
	stack<char> S;
	char ccc;
	do {	scanf("%c", &ccc);
		S.push(ccc);
	} while(ccc != '\n' && ccc != ' ');
	S.pop();
	int i = 0;
	while(!S.empty()) {
		a.tab[i] = int(S.top() - '0');
		S.pop(), ++i;
	}
	a.len = i;
}

void przepisz(liczba &a, liczba &b) {
	b.znak = a.znak, b.len = a.len;
	for(int i=0; i<b.len; ++i) b.tab[i] = a.tab[i];
}

void wypisz(liczba &a) {
	if(a.znak == '-') printf("-");
	for(int i=a.len-1; i>=0; --i) printf("%d", a.tab[i]);
	printf("\n");
}

void odejmij(liczba &, liczba &, liczba &);

void dodaj(liczba &a, liczba &b, liczba &c) {
	if(a.znak != b.znak) {
		b.znak = a.znak, odejmij(a, b, c);
		b.znak = (a.znak == '+') ? '-' : '+'; return;
	}
	int n1 = min(a.len, b.len), n2 = max(a.len, b.len), prz = 0;
	for(int i=0; i<n1; ++i) {
		c.tab[i] = a.tab[i] + b.tab[i] + prz;
		prz = c.tab[i] / MOD;
		c.tab[i] %= MOD;
	}
	if(n2 == a.len) {
		for(int i=n1; i<n2; ++i) {
			c.tab[i] = a.tab[i] + prz;
			prz = c.tab[i] / MOD;
			c.tab[i] %= MOD;
		}
	} else {
		for(int i=n1; i<n2; ++i) {
			c.tab[i] = b.tab[i] + prz;
			prz = c.tab[i] / MOD;
			c.tab[i] %= MOD;
		}
	}
	c.znak = a.znak;
	if(prz) c.len = n2 + 1, c.tab[n2] = prz;
	else c.len = n2;
}

bool wieksza(liczba &a, liczba &b) {
	if(a.len > b.len) return true;
	else if(a.len < b.len) return false;
	for(int i=a.len-1; i>=0; --i) {
		if(a.tab[i] > b.tab[i]) return true;
		else if(a.tab[i] < b.tab[i]) return false;
	}
	return false;
}

void odejmij(liczba &a, liczba &b, liczba &c) {
	if(a.znak != b.znak) {
		b.znak = a.znak, dodaj(a, b, c);
		b.znak = (a.znak == '+') ? '-' : '+'; return;
	}
	int prz = 0;
	if(wieksza(a, b)) {
		for(int i=0; i<b.len; ++i) {
			c.tab[i] = a.tab[i] - b.tab[i] - prz;
			if(c.tab[i] < 0) prz = 1, c.tab[i] += MOD;
			else prz = 0;
		}
		for(int i=b.len; i<a.len; ++i) {
			c.tab[i] = a.tab[i] - prz;
			if(c.tab[i] < 0) prz = 1, c.tab[i] += MOD;
			else prz = 0;
		}
		c.znak = a.znak, c.len = a.len;
		while(c.len > 1 && c.tab[c.len-1] == 0) --c.len;
	} else if(wieksza(b, a)) {
		for(int i=0; i<a.len; ++i) {
			c.tab[i] = b.tab[i] - a.tab[i] - prz;
			if(c.tab[i] < 0) prz = 1, c.tab[i] += MOD;
			else prz = 0;
		}
		for(int i=a.len; i<b.len; ++i) {
			c.tab[i] = b.tab[i] - prz;
			if(c.tab[i] < 0) prz = 1, c.tab[i] += MOD;
			else prz = 0;
		}
		c.znak = (b.znak == '+') ? '-' : '+', c.len = b.len;
		while(c.len > 1 && c.tab[c.len-1] == 0) --c.len;
	} else c.znak = '+', c.len = 1, c.tab[0] = 0;
}

bool zero(liczba &a) {
	return a.len == 1 && a.tab[0] == 0;
}

void wymnoz(liczba &a, liczba &b, liczba &c) {
	if(zero(a)) { przepisz(a, c); return; }
	if(zero(b)) { przepisz(b, c); return; }
	liczba d;
	c.tab[0] = 0, c.len = 1;
	for(int i=0; i<a.len; ++i) {
		int prz = 0, ind = i;
		for(int j=0; j<b.len; ++j) {
			d.tab[ind] = a.tab[i] * b.tab[j] + prz;
			prz = d.tab[ind] / MOD;
			d.tab[ind] %= MOD, ++ind;
		}
		if(prz) d.tab[ind] = prz, d.len = ind + 1;
		else d.len = ind;
		dodaj(c, d, c);
		d.tab[i] = 0;
	}
	while(c.len > 1 && c.tab[c.len-1] == 0) --c.len;
	if(a.znak != b.znak) c.znak = '-';
}

void modulo(liczba &a, liczba &b) {
	liczba s;
	int p = a.len, q = b.len;
	for(int i=0; i<p; ++i) s.tab[i] = 0;
	s.len = q;
	for(int i=p-q; i>=0; --i) {
		while(p > 1 && a.tab[p-1] == 0) --p;
		int k = i + s.len;
		for(int j=s.len-1; j>=0; --j) s.tab[j] = a.tab[i+j];
		while(s.len > 1 && s.tab[s.len-1] == 0) --s.len;
		for(int j=0; j<MOD; ++j) {
			if(wieksza(b, s) || j == MOD - 1) break;
			odejmij(s, b, s);
		}
		for(int j=s.len-1; j>=0; --j) a.tab[i+j] = s.tab[j];
		++s.len;
		while(k >= i + s.len - 1) a.tab[k--] = 0;
	}
	while(p > 1 && a.tab[p-1] == 0) --p;
	a.len = p;
}

void podziel(liczba &a, liczba &b, liczba &c) {
	liczba s;
	int p = a.len, q = b.len;
	for(int i=0; i<p; ++i) c.tab[i] = s.tab[i] = 0;
	c.len = p, s.len = q;
	for(int i=p-q; i>=0; --i) {
		while(p > 1 && a.tab[p-1] == 0) --p;
		int k = i + s.len;
		for(int j=s.len-1; j>=0; --j) s.tab[j] = a.tab[i+j];
		while(s.len > 1 && s.tab[s.len-1] == 0) --s.len;
		for(int j=0; j<MOD; ++j) {
			if(wieksza(b, s) || j == MOD - 1) { c.tab[i] = j; break; }
			odejmij(s, b, s);
		}
		for(int j=s.len-1; j>=0; --j) a.tab[i+j] = s.tab[j];
		++s.len;
		while(k >= i + s.len - 1) a.tab[k--] = 0;
	}
	while(c.len > 1 && c.tab[c.len-1] == 0) --c.len;
	while(p > 1 && a.tab[p-1] == 0) --p;
	a.len = p;
}

void zrob_binar(liczba &a, binar &b) {
	liczba c;
	przepisz(a, c);
	int j = 0;
	while(c.len != 1 || c.tab[0] != 1) {
		b.tab[j++] = c.tab[0] % 2;
		int prz = 0, k;
		for(int i=c.len-1; i>=0; --i) {
			k = c.tab[i] + prz * MOD;
			c.tab[i] = k / 2, prz = k % 2;
		}
		if(c.tab[c.len-1] == 0) --c.len;
	}
	b.tab[j++] = 1, b.len = j;
}

void modexp(liczba &a, liczba &b, liczba &n, liczba &d) {
	liczba dd;
	binar bb;
	zrob_binar(b, bb);
	d.len = d.tab[0] = 1;
	for(int i=bb.len-1; i>=0; --i) {
		wymnoz(d, d, dd), modulo(dd, n);
		if(bb.tab[i] == 1) wymnoz(dd, a, d), modulo(d, n);
		else przepisz(dd, d);
	}
}

void gcd(liczba &a, liczba &b, liczba &c) {
	if(zero(b)) przepisz(a, c);
	else modulo(a, b), gcd(b, a, c);
}

int main() {
	int Z;
	scanf("%d", &Z);
	for(int z=1; z<=Z; ++z) {
		int n;
		liczba a, b, k, amin, d;
		scanf("%d ", &n);
		for(int i=0; i<n; ++i) {
			wczytaj(a);
			if(i == 0) {
				przepisz(a, amin), d.len = 1, d.tab[0] = 0;
			} else {
				przepisz(amin, b);
				if(wieksza(amin, a)) przepisz(a, amin);
				odejmij(a, b, a), a.znak = '+';
				przepisz(d, k), gcd(k, a, d);
			}
		}
		przepisz(amin, a), podziel(a, d, k), wymnoz(k, d, b);
		if(!zero(a)) dodaj(b, d, b);
		odejmij(b, amin, b);
		printf("Case #%d: ", z), wypisz(b);
	}
	return 0;
}
