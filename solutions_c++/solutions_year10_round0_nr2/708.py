#include <stdio.h>
#include <string.h>

typedef int Type;
const int MAX_DIG = 1009;
const int BASE = 4;
const int BIT_LENGTH = 15;
const Type MOD = 1 << BIT_LENGTH;
const Type MASK = (1 << BIT_LENGTH) - 1;

struct Int {
public:
	int len;
	Type dig[MAX_DIG];

	Int() {
		len = 0; dig[0] = 0;
	}

	Int(const Int& b) {
		*this = b;
	}

	Int(const char b[]) {
		*this = b;
	}

	Int(Type b) {
		*this = b;
	}

	Int& operator =(const char data[]) {
		int i, p, w = strlen(data) - 1;
		Type j, k;
		for (len = p = 0; p <= w && data[p] == '0'; p++);
		while (true) {
			for (i = 0, j = 0, k = 1; i < BASE && w >= p; k *= 10, i++)
				j += (data[w--] - '0') * k;
			dig[len++] = j;
			if (w < p) break;
		}
		len--;
		Int t;
		for (i = len; i >= 0; --i)
			t = t * 10000 + dig[i];
		return (*this) = t;
	}


	Int& operator =(const Int& b) {
		memcpy(dig, b.dig, (b.len + 1) * sizeof(Type));
		len = b.len;
		return (*this);
	}

	Int& operator =(Type b) {
		if (b == 0) {
			len = 0; dig[0] = 0; return (*this);
		}
		for (len = - 1; b;) {
			dig[++len] = b & MASK;
			b >>= BIT_LENGTH;
		}
		return (*this);
	}

	Int add(Type b) const {
		int i; Int c;
		for (i = 0; i <= len || b; i++) {
			if (i <= len) b += dig[i];
			c.dig[i] = b % 10000;
			b /= 10000;
		}
		c.len = i - 1;
		return c;
	}

	Int mul(Type b) const {
		int i; Type carry; Int c;
		for (i = 0, carry = 0; i <= len || carry; i++) {
			if (i <= len) carry += b * dig[i];
			c.dig[i] = carry % 10000;
			carry /= 10000;
		}
		i--;
		while (i && !c.dig[i]) i--;
		c.len = i;
		return c;
	}

	void output() const {
		Int ans = 0;
		int i;
		for (i = len; i >= 0; --i) {
			ans = ans.mul(1 << BIT_LENGTH);
			ans = ans.add(dig[i]);
		}
		i = ans.len - 1;
		printf("%d", ans.dig[ans.len]);
		while (i >= 0)
			printf("%04d", ans.dig[i--]);
	}

	int cmp(const Int& b) const {
		if (len < b.len)
			return -1;
		if (len > b.len)
			return 1;
		int i = len;
		while (i && dig[i] == b.dig[i])
			i--;
		return dig[i] > b.dig[i] ? 1 : (dig[i] == b.dig[i] ? 0 : -1);
	}

	void shift(int k) {
		int i;
		for (i = len + k; i >= k; i--)
			dig[i] = dig[i - k];
		while (i >= 0)
			dig[i--] = 0;
		len += k;
	}

	Int operator +(Type b) const {
		int i; Int c;
		for (i = 0; i <= len || b; i++) {
			if (i <= len)
				b += dig[i];
			c.dig[i] = b & MASK;
			b >>= BIT_LENGTH;
		}
		c.len = i - 1;
		return c;
	}


	Int operator -(Type b) const {
		int i; Int c;
		for (i = 0; i <= len; i++) {
			c.dig[i] = dig[i] - b;
			if (c.dig[i] < 0) {
				b = (-c.dig[i] + MOD - 1) / MOD;
				c.dig[i] += b * MOD;
			} else
				b = 0;
		}
		i--;
		while (i && !c.dig[i])
			i--;
		c.len = i;
		return c;
	}

	Int operator *(Type b) const {
		int i; Type carry; Int c;
		for (i = 0, carry = 0; i <= len || carry; i++) {
			if (i <= len)
				carry += b * dig[i];
			c.dig[i] = carry & MASK;
			carry >>= BIT_LENGTH;
		}
		i--;
		while (i && !c.dig[i])
			i--;
		c.len = i;
		return c;
	}

	Int operator /(Type b) const {
		int i; Type d; Int c;
		for (i = len, d = 0; i >= 0; i--) {
			d = d * MOD + dig[i];
			c.dig[i] = d / b; d %= b;
		}
		i = len;
		while (i && !c.dig[i])
			i--;
		c.len = i;
		return c;
	}

	Type operator %(Type b) const {
		int i; Type d; Int c;
		for (i = len, d = 0; i >= 0; i--) {
			d = d * MOD + dig[i];
			c.dig[i] = d / b; d %= b;
		}
		return d;
	}

	Int operator +(const Int& b) const {
		int i; Type carry; Int c;
		for (i = 0, carry = 0; i <= len || i <= b.len || carry; i++) {
			if (i <= len && i <= b.len)
				carry += dig[i] + b.dig[i];
			else if (i <= len && i > b.len)
				carry += dig[i];
			else if (i > len && i <= b.len)
				carry += b.dig[i];
			c.dig[i] = carry & MASK; carry >>= BIT_LENGTH;
		}
		c.len = i - 1;
		return c;
	}

	Int operator -(const Int& b) const {
		int i; Type carry; Int c;
		for (i = 0, carry = 0; i <= len; i++) {
			c.dig[i] = dig[i] - carry;
			if (i <= b.len)
				c.dig[i] -= b.dig[i];
			if (c.dig[i] < 0) {
				carry = 1; c.dig[i] += MOD;
			} else
				carry = 0;
		}
		i--;
		while (i && c.dig[i] == 0)
			i--;
		c.len = i;
		return c;
	}

	Int operator *(const Int& b) const {
		int i, j; Type carry; Int c;
		for (i = len + b.len + 1; i >= 0; i--)
			c.dig[i] = 0;
		for (i = 0; i <= len; i++)
			for (j = 0, carry = 0; j <= b.len || carry; j++) {
				if (j <= b.len) carry += c.dig[i + j] + dig[i] * b.dig[j];
				else			carry += c.dig[i + j];
				c.dig[i + j] = carry & MASK; carry >>= BIT_LENGTH;
			}
		i = len + b.len + 1;
		while (i && c.dig[i] == 0)
			i--;
		c.len = i;
		return c;
	}

	Int operator /(const Int& b) const {
		int k; Type x; Int temp, c, d = *this;
		while (d.cmp(b) > 0) {
			k = d.len - b.len;
			if (d.dig[d.len] > b.dig[b.len])
				x = d.dig[d.len] / (b.dig[b.len] + 1);
			else if (k) {
				k--;
				x = (d.dig[d.len] * MOD + d.dig[d.len - 1]) /
				    (b.dig[b.len] + 1);
			} else
				break;
			temp = b * x; temp.shift(k);
			d = d - temp; temp = x;
			temp.shift(k); c = c + temp;
		}
		if (d.cmp(b) >= 0)
			c = c + 1;
		return c;
	}

	Int operator %(const Int& b) const {
		int k; Type x; Int temp, c, d = *this;
		while (d.cmp(b) > 0) {
			k = d.len - b.len;
			if (d.dig[d.len] > b.dig[b.len])
				x = d.dig[d.len] / (b.dig[b.len] + 1);
			else if (k) {
				k--;
				x = (d.dig[d.len] * MOD + d.dig[d.len - 1]) /
				    (b.dig[b.len] + 1);
			} else
				break;
			temp = b * x; temp.shift(k);
			d = d - temp; temp = x;
			temp.shift(k); c = c + temp;
		}
		if (d.cmp(b) >= 0)
			d = d - b;
		return d;
	}
};

struct Bint {
	Int data;
	int sign;

	Bint() : sign(0) {}
	Bint(const Bint& b) { *this = b; }
	Bint(const char s[]) { *this = s; }
	Bint(Type b) { *this = b; }
	Bint& operator =(const char s[]) {
		int i;
		sign = 0;
		for (i = 0; s[i]; ++i)
			if (s[i] == '-') {
				sign = 1;
				break;
			}
		if (sign) data = s + i + 1;
		else data = s;
		return (*this);
	}
	Bint& operator =(const Bint& b) {
		sign = b.sign;
		data = b.data;
		return (*this);
	}
	Bint& operator =(Type b) {
		if (b < 0) { b = -b; sign = 1; }
		else sign = 0;
		data = b;
		return (*this);
	}

	Bint operator -() const {
		Bint c = *this;
		c.sign = !c.sign;
		return c;
	}

	Bint operator +(const Bint& b) const {
		Bint c;
		if (sign == b.sign) {
			c.sign = sign;
			c.data = data + b.data;
		} else {
			if (data.cmp(b.data) >= 0) {
				c.sign = sign;
				c.data = data - b.data;
			} else {
				c.sign = b.sign;
				c.data = b.data - data;
			}
		}
		return c;
	}

	Bint operator -(const Bint &other) const {
		return (*this) + (-other);
	}

	Bint operator *(const Bint& other) const {
		Bint c;
		sign ^ other.sign ? c.sign = 1 : c.sign = 0;
		c.data = data * other.data;
		return c;
	}

	Bint operator /(const Bint &other) const {
		Bint c;
		(sign ^ other.sign) ? c.sign = 1 : c.sign = 0;
		c.data = data / other.data;
		return c;
	}

	Bint operator %(const Bint &other) const {
		Bint c;
		(sign ^ other.sign) ? c.sign = 1 : c.sign = 0;
		c.data = data % other.data;
		return c;
	}

	void output() const {
		if (data.len == 0 && data.dig[0] == 0) {
			printf("0");
			return;
		}
		if (sign) printf("-");
		data.output();
	}
};


Bint t[10009];

Bint gcd(Bint a, Bint b) {
	Bint t;
	//if (a.data.cmp(0) < 0) a = -a;
	//if (b.data.cmp(0) < 0) b = -b;
//	printf("a =");
//	a.output();
//	printf("b = ");
	//b.output();
	if (a.sign) a.sign = 0;
	if (b.sign) b.sign = 0;
	while (b.data.cmp(0) > 0) {
		t = a % b;
		a = b;
		b = t;
	}
	return a;
}

int main() {
	freopen("B-large.in.txt", "r", stdin);
	freopen("B-large.out.txt", "w", stdout);
	int T;
	int i, n, j;
	int cas = 0;
	char s[1009];
	Bint gd;
	scanf("%d", &T);
	while (T--) {
		scanf("%d", &n);
		for (i = 0; i < n; ++i) {
			//scanf("%I64d", &t[i]);
			scanf("%s", s);
			t[i] = s;
	//		t[i] = s;
	//		printf("t[i] =");
	//		t[i].output();
	//		printf("\n");
		}
		gd = 0;
		for (i = 1; i < n; ++i) {
			gd = gcd(gd, t[i] - t[0]);
	//		gd.output();
	//		printf("----\n");
		}
		//ll T = gd;
	//	gd.output();
	//	printf("\n");
		Bint x = (-t[0] % gd + gd) % gd;
		printf("Case #%d: ", ++cas);
		x.output();
		printf("\n");
	//	return 0;
	}
	return 0;
}

		