#include <vector>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <functional>

using namespace std;

const int MODULO = 10000;
const int MAX_LEN = 100;
const int MAX_N = 1010;

class BigInteger {

private:
	int sign;
	vector<int> bigInt;

public:
	BigInteger();
	BigInteger(int val);
	BigInteger(char ch[]);
	BigInteger add(BigInteger &val);
	BigInteger subtract(BigInteger &val);
	BigInteger multiply(BigInteger &val);
	BigInteger divide(BigInteger &val);
	BigInteger mod(BigInteger &val);
	BigInteger pow(int exponent);
	int digit();
	int compareTo(BigInteger &val);
	char *toCharArray();
	bool operator <(const BigInteger &val) const;

};

BigInteger::BigInteger() {
}

BigInteger::BigInteger(int val) {
	if (val > 0) {
		sign = 1;
	} else if (!val) {
		sign = 0;
	} else {
		sign = -1;
		val = -val;
	}
	do {
		bigInt.push_back(val % MODULO);
		val /= MODULO;
	} while (val);
}

BigInteger::BigInteger(char ch[]) {
	if (ch[0] == '-') sign = -1, ch++;
	int len = strlen(ch), k = len - 1;
	int t = MODULO, d = -1;
	while (t) t /= 10, d++;
	len = (len - 1) / d + 1;
	bigInt.resize(len, 0);
	for (int i = 0; i < len; i++) {
		for (int j = 1; j < MODULO && k >= 0; j *= 10) {
			bigInt[i] += (ch[k--] - 48) * j;
		}
	}
	while (len > 1 && !bigInt[len - 1]) bigInt.erase(bigInt.end() - 1);
	if (len == 1 && !bigInt[0]) sign = 0;
	else sign = 1;
}

BigInteger BigInteger::add(BigInteger &val) {
	BigInteger &a = *this, &b = val, c;
	if (a.sign * b.sign >= 0) {
		int maxlen, minlen;
		if (a.bigInt.size() < b.bigInt.size()) {
			minlen = a.bigInt.size();
			maxlen = b.bigInt.size();
		} else {
			minlen = b.bigInt.size();
			maxlen = a.bigInt.size();
		}
		if (a.sign > 0 || b.sign > 0) c.sign = 1;
		else if (!a.sign && !b.sign) c.sign = 0;
		else c.sign = -1;
		c.bigInt.reserve(maxlen + 1);
		c.bigInt.push_back(a.bigInt[0] + b.bigInt[0]);
		for (int i = 1; i < minlen; i++) {
			c.bigInt.push_back(c.bigInt[i - 1] / MODULO);
			c.bigInt[i - 1] %= MODULO;
			c.bigInt[i] += a.bigInt[i] + b.bigInt[i];
		}
		if (a.bigInt.size() > b.bigInt.size()) {
			for (int i = minlen; i < maxlen; i++) {
				c.bigInt.push_back(c.bigInt[i - 1] / MODULO);
				c.bigInt[i - 1] %= MODULO;
				c.bigInt[i] += a.bigInt[i];
			}
		} else {
			for (int i = minlen; i < maxlen; i++) {
				c.bigInt.push_back(c.bigInt[i - 1] / MODULO);
				c.bigInt[i - 1] %= MODULO;
				c.bigInt[i] += b.bigInt[i];
			}
		}
		if (c.bigInt[maxlen - 1] >= MODULO) {
			c.bigInt.push_back(c.bigInt[maxlen - 1] / MODULO);
			c.bigInt[maxlen - 1] %= MODULO;
		}
	} else {
		if (a.sign > 0) {
			b.sign = -b.sign;
			c = a.subtract(b);
			b.sign = b.sign;
		} else {
			a.sign = -a.sign;
			c = b.subtract(a);
			a.sign = -a.sign;
		}
	}
	return c;
}

BigInteger BigInteger::subtract(BigInteger &val) {
	BigInteger &a = *this, &b = val, c;
	if (a.sign * b.sign >= 0) {
		int tas = a.sign, tbs = b.sign, cmp;
		a.sign = b.sign = 1;
		cmp = a.compareTo(b);
		a.sign = tas;
		b.sign = tbs;
		if (cmp < 0) {
			c = b.subtract(a);
			c.sign = -c.sign;
		} else if (!cmp) {
			c = BigInteger(0);
		} else {
			int l1 = a.bigInt.size(), l2 = b.bigInt.size(), borrow = 0;
			c.bigInt.reserve(l1);
			for (int i = 0; i < l2; i++) {
				if (a.bigInt[i] < b.bigInt[i] + borrow) {
					c.bigInt.push_back(a.bigInt[i] + MODULO - b.bigInt[i] - borrow);
					borrow = 1;
				} else {
					c.bigInt.push_back(a.bigInt[i] - b.bigInt[i] - borrow);
					borrow = 0;
				}
			}
			for (int i = l2; i < l1; i++) {
				if (a.bigInt[i] < borrow) {
					c.bigInt.push_back(a.bigInt[i] + MODULO - 1);
				} else {
					c.bigInt.push_back(a.bigInt[i] - borrow);
					borrow = 0;
				}
			}
			int l3 = l1 - 1;
			while (!c.bigInt[l3]) l3--;
			c.bigInt.erase(c.bigInt.begin() + l3 + 1, c.bigInt.end());
			c.sign = a.sign;
		}
	} else {
		if (a.sign > 0) {
			b.sign = 1;
			c = a.add(b);
			b.sign = -1;
		} else {
			b.sign = -1;
			c = a.add(b);
			b.sign = 1;
		}
	}
	return c;
}

BigInteger BigInteger::multiply(BigInteger &val) {
	BigInteger &a = *this, &b = val, c;
	int l1 = a.bigInt.size(), l2 = b.bigInt.size();
	c.sign = a.sign * b.sign;
	if (!c.sign) {
		c.bigInt.push_back(0);
		return c;
	}
	c.bigInt.resize(l1 + l2, 0);
	for (int i = 0; i < l1; i++) {
		for (int j = 0; j < l2; j++) {
			c.bigInt[i + j] += a.bigInt[i] * b.bigInt[j];
			if (c.bigInt[i + j] >= MODULO) {
				c.bigInt[i + j + 1] += c.bigInt[i + j] / MODULO;
				c.bigInt[i + j] %= MODULO;
			}
		}
	}
	if (!c.bigInt[l1 + l2 - 1]) c.bigInt.erase(c.bigInt.end() - 1);
	return c;
}

BigInteger BigInteger::divide(BigInteger &val) {
	int tas = this->sign, tbs = val.sign;
	this->sign = val.sign = 1;
	if (this->compareTo(val) < 0) {
		this->sign = tas;
		val.sign = tbs;
		return BigInteger(0);
	}
	this->sign = tas;
	val.sign = tbs;
	BigInteger a = *this, b, c;
	int pos = this->bigInt.size() - val.bigInt.size();
	b.bigInt.resize(pos, 0);
	for (int i = 0, len = val.bigInt.size(); i < len; i++) {
		b.bigInt.push_back(val.bigInt[i]);
	}
	a.sign = b.sign = 1;
	c.bigInt.resize(pos + 1, 0);
	for (int i = pos; i >= 0; i--) {
		if (a.compareTo(b) >= 0) {
			int left = 1, right = MODULO - 1, mid, cmp, ret = 1;
			while (left <= right) {
				BigInteger t = BigInteger(mid = (left + right) >> 1).multiply(b);
				cmp = a.compareTo(t);
				if (cmp >= 0) left = mid + 1, ret = mid;
				else right = mid - 1;
			}
			BigInteger t = BigInteger(c.bigInt[i] = ret).multiply(b);
			a = a.subtract(t);
		}
		if (i) b.bigInt.erase(b.bigInt.begin() + i - 1);
	}
	if (!c.bigInt[pos]) c.bigInt.erase(c.bigInt.end() - 1);
	c.sign = this->sign * val.sign;
	return c;
}

BigInteger BigInteger::mod(BigInteger &val) {
	int tas = this->sign, tbs = val.sign;
	this->sign = val.sign = 1;
	if (this->compareTo(val) < 0) {
		this->sign = tas;
		val.sign = tbs;
		return *this;
	}
	this->sign = tas;
	val.sign = tbs;
	BigInteger a = *this, b;
	int pos = this->bigInt.size() - val.bigInt.size();
	b.bigInt.resize(pos, 0);
	for (int i = 0, len = val.bigInt.size(); i < len; i++) {
		b.bigInt.push_back(val.bigInt[i]);
	}
	a.sign = b.sign = 1;
	for (int i = pos; i >= 0; i--) {
		if (a.compareTo(b) >= 0) {
			int left = 1, right = MODULO - 1, mid, cmp, ret = 1;
			while (left <= right) {
				BigInteger t = BigInteger(mid = (left + right) >> 1).multiply(b);
				cmp = a.compareTo(t);
				if (cmp >= 0) left = mid + 1, ret = mid;
				else right = mid - 1;
			}
			BigInteger t = BigInteger(ret).multiply(b);
			a = a.subtract(t);
		}
		if (i) b.bigInt.erase(b.bigInt.begin() + i - 1);
	}
	a.sign = this->sign;
	if (!a.bigInt[0] && a.bigInt.size() == 1) a.sign = 0;
	return a;
}

BigInteger BigInteger::pow(int exponent) {
	BigInteger s = BigInteger(1), t = *this;
	while (exponent) {
		if (exponent & 1) s = s.multiply(t);
		exponent >>= 1;
		t = t.multiply(t);
	}
	return s;
}

int BigInteger::digit() {
	int t1 = -1, t2 = 0, num = MODULO;
	while (num) num /= 10, t1++;
	num = bigInt[bigInt.size() - 1];
	do num /= 10, t2++; while (num);
	return t1 * (bigInt.size() - 1) + t2;
}

int BigInteger::compareTo(BigInteger &val) {
	if (this->sign > val.sign) return 1;
	else if (this->sign < val.sign) return -1;
	else {
		int l1 = this->bigInt.size(), l2 = val.bigInt.size();
		if (sign > 0) {
			if (l1 > l2) return 1;
			if (l1 < l2) return -1;
			for (int i = l1 - 1; i >= 0; i--) {
				if (this->bigInt[i] > val.bigInt[i]) return 1;
				if (this->bigInt[i] < val.bigInt[i]) return -1;
			}
			return 0;
		} else {
			if (l1 > l2) return -1;
			if (l1 < l2) return 1;
			for (int i = l1 - 1; i >= 0; i--) {
				if (this->bigInt[i] > val.bigInt[i]) return -1;
				if (this->bigInt[i] < val.bigInt[i]) return 1;
			}
			return 0;
		}
	}
}

char *BigInteger::toCharArray() {
	int len = digit();
	if (sign < 0) len++;
	char *ch = new char[len + 1];
	ch[len] = 0;
	if (sign < 0) *(ch++) = '-', len--;
	int t = -1, m = MODULO, num;
	while (m) m /= 10, t++;
	m = bigInt.size();
	for (int i = 0; i < m; i++) {
		num = bigInt[i];
		for (int j = 0; j < t && len; j++) {
			ch[--len] = num % 10 + 48;
			num /= 10;
		}
	}
	return ch - (sign < 0);
}

bool BigInteger::operator<(const BigInteger &val) const {
	if (this->sign > val.sign) return 0;
	else if (this->sign < val.sign) return 1;
	else {
		int l1 = this->bigInt.size(), l2 = val.bigInt.size();
		if (sign > 0) {
			if (l1 > l2) return 0;
			if (l1 < l2) return 1;
			for (int i = l1 - 1; i >= 0; i--) {
				if (this->bigInt[i] > val.bigInt[i]) return 0;
				if (this->bigInt[i] < val.bigInt[i]) return 1;
			}
			return 0;
		} else {
			if (l1 > l2) return 1;
			if (l1 < l2) return 0;
			for (int i = l1 - 1; i >= 0; i--) {
				if (this->bigInt[i] > val.bigInt[i]) return 1;
				if (this->bigInt[i] < val.bigInt[i]) return 0;
			}
			return 0;
		}
	}
}

BigInteger ZERO(0);
BigInteger bi[MAX_N];
char st[MAX_LEN];
int cas, n;

int main(void) {
	freopen("D:\\b.in", "r", stdin);
	freopen("D:\\b.out", "w", stdout);
	scanf("%d", &cas);
	for (int cc = 1; cc <= cas; ++cc) {
		scanf("%d", &n);
		for (int i = 0; i < n; ++i) {
			scanf("%s", st);
			bi[i] = BigInteger(st);
		}
		sort(bi, bi + n);
		for (int i = 0; i < n - 1; ++i) {
			bi[i] = bi[i + 1].subtract(bi[i]);
		}
		BigInteger gcd(bi[0]);
		for (int i = 1; i < n - 1; ++i) {
			BigInteger b(bi[i]), t;
			while (b.compareTo(ZERO) > 0) {
				t = gcd.mod(b);
				gcd = b;
				b = t;
			}
		}
		printf("Case #%d: ", cc);
		if (bi[n - 1].mod(gcd).compareTo(ZERO) > 0) {
			puts(gcd.subtract(bi[n - 1].mod(gcd)).toCharArray());
		} else {
			puts("0");
		}
	}
	return 0;
}

