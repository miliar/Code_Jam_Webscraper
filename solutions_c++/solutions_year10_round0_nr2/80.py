#include <cstdio>

struct BI {
	int d[16];
	BI() {
		for (int i = 0; i < 16; ++i)
			d[i] = 0;
	}
	void st() {
		for (int i = 0; i < 15; ++i) {
			d[i + 1] += d[i]/10000;
			d[i] %= 10000;
			if (d[i] < 0) {
				--d[i + 1];
				d[i] += 10000;
			}
		}
	}
	BI operator<<(int n) {
		BI r = *this;
		for (int j = 0; j < n; ++j) {
			for (int i = 0; i < 16; ++i)
				r.d[i] *= 10;
			r.st();
		}
		return r;
	}
	void read() {
		for (int i = 0; i < 16; ++i)
			d[i] = 0;
		char s[256], sn;
		scanf("%s", s);
		sn = 0;
		while (s[sn]) {
			for (int i = 0; i < 16; ++i)
				d[i] *= 10;
			d[0] += s[sn] - '0';
			st();
			++sn;
		}
	}
	void out() {
		int n = 15;
		while (n && !d[n]) --n;
		if (!n) {
			printf("%d\n", d[0]);
			return;
		}
		printf("%d", d[n]);
		for (int i = n - 1; i >= 0; --i)
			printf("%04d", d[i]);
		puts("");
	}
	BI operator-(const BI &q) const {
		BI r = BI();
		for (int i = 0; i < 16; ++i)
			r.d[i] = d[i] - q.d[i];
		r.st();
		return r;
	}
	bool operator<(const BI &q) const {
		for (int i = 15; i >= 0; --i)
			if (d[i] < q.d[i]) return 1;
			else if (q.d[i] < d[i]) return 0;
		return 0;
	}
	bool operator==(const BI &q) const {
		for (int i = 0; i < 16; ++i)
			if (d[i] != q.d[i]) return 0;
		return 1;
	}
};

const BI z = BI();

BI mod(BI a, BI b) {
/*	puts("doing mod");
	a.out();
	b.out();*/
	if (a < z) return mod(b - mod(z - a, b), b);
	while (!(a < b)) {
		int n = 0;
		while (!(a < (b << n))) ++n;
		a = a - (b << n - 1);
	}
	return a;
};

BI gcd(BI a, BI b) {
/*	puts("doing gcd");
	a.out();
	b.out();*/
	if (b == z) return (a < z) ? z - a : a;
	return gcd(b, mod(a, b));
};

int T, n;
BI p, q, t;

int main() {
	scanf("%d", &T);
	for (int r = 1; r <= T; ++r) {
		t = BI();
		printf("Case #%d: ", r);
		scanf("%d", &n);
		p.read();
		for (int i = 1; i < n; ++i) {
			q.read();
			t = gcd(p - q, t);
			p = q;
		}
		mod(z - p, t).out();
	}
	return 0;
}
