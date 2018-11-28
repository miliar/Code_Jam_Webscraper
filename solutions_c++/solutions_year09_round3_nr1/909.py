#include <iostream>
#include <map>

//---------------------------------------有符号高精------------------------------------------
const int LENGTH = 1<<10; //能保存的数字的长度为LENGTH*4
struct BigNum {
	BigNum() {
		sign = true;
		memset(num, 0, sizeof(num));
		len = 1;
	}
	BigNum(int n) {
		int b;
		if (n >= 0) {sign = true; b = n;}
		else {sign = false; b = -n;}
		memset(num, 0, sizeof(num));
		len = 0;
		while (b) {
			num[len++] = b % 10000;
			b /= 10000;
		}
		if (!len) len = 1;
	}
	bool sign;
	int num[LENGTH];
	int len;
};

void input(BigNum &a, const char str[])
{
	int i, j, len; i = 0;
	memset(a.num, 0, sizeof(a.num));
	if (str[i] == '-') i++, a.sign = false;
	else a.sign = true;
	while (str[i] == '0' && (int)strlen(str) != i+1) i++;
	len = strlen(str) - 1; a.len = 0;
	while (len >= i) {
		for (j = 1; j < 10000 && len >= i; j *= 10)
			a.num[a.len] += j * (str[len--] - '0');
		a.len++;
	}
	return;
}

void print(const BigNum &a)
{
	int i;
	if (!a.sign) printf("-");
//	else printf("+");
	printf("%d", a.num[a.len-1]);
	for (i = a.len-2; i >= 0; i--)
		printf("%04d", a.num[i]);
	return;
}

//比较：相等返回0，a > b返回正数， 否则返回负数
int compare(const BigNum &a, const BigNum &b)
{
	if (a.sign != b.sign) return (a.sign ? 1 : -1);
	if (a.len > b.len) return a.sign ? 1: -1;
	else if (a.len < b.len) return a.sign ? -1 : 1;

	int len = a.len-1;
	while (len > 0 && a.num[len] == b.num[len]) len--;
	return (a.sign ? 1 : -1) * (a.num[len] - b.num[len]);
}

void subtract(const BigNum &a, const BigNum &b, BigNum &c);
//高精加法c = a + b
void plus(const BigNum &a, const BigNum &b, BigNum &c)
{
	if (a.sign != b.sign) {
		//调用高精减法
		BigNum d = b; d.sign = !b.sign;
		subtract(a, d, c); return;
	}
	memset(c.num, 0, sizeof(c.num));
	c.sign = a.sign;
	c.len = a.len > b.len ? a.len : b.len;
	int i, ca = 0;
	for (i = 0; i < c.len; i++) {
		c.num[i] = a.num[i] + b.num[i] + ca;
		ca = c.num[i] / 10000;
		c.num[i] %= 10000;
	}
	if (ca) c.num[c.len++] = ca;
	return;
}

void decrease(BigNum &a, const BigNum &b);
//加法 
void increase(BigNum &a, const BigNum&b)
{
	if (a.sign != b.sign) {
		BigNum d = b; d.sign = !b.sign;
		decrease(a, d); return;
	}
	int i, ca = 0;
	if (a.len < b.len) a.len = b.len;
	for (i = 0; i < a.len; i++) {
		a.num[i] += b.num[i] + ca;
		ca = a.num[i] / 10000;
		a.num[i] %= 10000;
	}
	if (ca) a.num[a.len++] = ca;
	return;
}

//高精减法c = a - b
void subtract(const BigNum &a, const BigNum &b, BigNum &c)
{
	if (a.sign != b.sign) {
		//调用高精加法
		BigNum d = b; d.sign = !b.sign;
		plus(a, d, c); return;
	}
	if (!a.sign) {
		BigNum e = a, d = b;
		e.sign = d.sign = true;
		subtract(d, e, c); return;
	}
	memset(c.num, 0, sizeof(c.num));
	int i, ca, ret = compare(a, b);
	if (ret == 0) {c = 0; return;}
	else if (ret > 0) {
		c.sign = true; ca = 0;
		for (i = 0; i < a.len; i++) {
			c.num[i] = a.num[i] - b.num[i] - ca;
			if (c.num[i] < 0) {c.num[i] += 10000; ca = 1;}
			else ca = 0;
		}
		c.len = a.len;
		while(c.len > 1 && c.num[c.len-1] == 0) c.len--;
	}
	else {
		c.sign = false; ca = 0;
		for (i = 0; i < b.len; i++) {
			c.num[i] = b.num[i] - a.num[i] - ca;
			if (c.num[i] < 0) {c.num[i] += 10000; ca = 1;}
			else ca = 0;
		}
		c.len = b.len;
		while (c.len > 1 && c.num[c.len-1] == 0) c.len--;
	}
	return;
}

//减法
void decrease(BigNum &a, const BigNum &b)
{
	if (a.sign != b.sign) {
		//调用加法
		BigNum d = b; d.sign = !b.sign;
		increase(a, d); return;
	}
	if (!a.sign) {
		BigNum d = b;
		a.sign = d.sign = true;
		decrease(a, d);
		a.sign = !a.sign;
		return;
	}
	int i, ca, ret = compare(a, b);
	if (ret == 0) {a = 0; return;}
	else if (ret > 0) {
		ca = 0;
		for (i = 0; i < a.len; i++) {
			a.num[i] = a.num[i] - b.num[i] - ca;
			if (a.num[i] < 0) {a.num[i] += 10000; ca = 1;}
			else ca = 0;
		}
		while(a.len > 1 && a.num[a.len-1] == 0) a.len--;
	}
	else {
		a.sign = false; ca = 0;
		for (i = 0; i < b.len; i++) {
			a.num[i] = b.num[i] - a.num[i] - ca;
			if (a.num[i] < 0) {a.num[i] += 10000; ca = 1;}
			else ca = 0;
		}
		a.len = b.len;
		while (a.len > 1 && a.num[a.len-1] == 0) a.len--;
	}
	return;
}

// 高精乘法c = a * b
void multiply(const BigNum &a, const BigNum &b, BigNum &c)
{
	c.sign = (a.sign == b.sign ? true : false);
	memset(c.num, 0, sizeof(c.num));
	int i, j;
	for (i = 0; i < a.len; i++) for (j = 0; j < b.len; j++) {
		c.num[i+j] += (a.num[i] * b.num[j]);
		c.num[i+j+1] += c.num[i+j] / 10000;
		c.num[i+j] %= 10000;
	}
	c.len = a.len + b.len;
	while (c.len > 1 && c.num[c.len-1] == 0) c.len--;
	if (c.len == 1 && c.num[0] == 0) c.sign = true;
	return;
}

void multiply10(BigNum &a) // 高精*10
{
	int len, i, ca;
	len = a.len;
	a.num[len-1] *= 10;
	ca = a.num[len-1]/10000;
	a.num[len-1] %= 10000;
	if(ca) {a.num[len] = ca; a.len++;}
	for (i = len-2; i >= 0;i--) {
		a.num[i] *= 10;
		a.num[i+1] += a.num[i]/10000;
		a.num[i] %= 10000;
	}
	return;
}

// 高精除法（d为余数）
void divide(const BigNum &a, const BigNum &b, BigNum &c, BigNum &d)
{
	c.sign = (a.sign == b.sign ? true : false);
	d.sign = true;
	memset(c.num, 0, sizeof(c.num));
	memset(d.num, 0, sizeof(d.num));
	if (!compare(b, 0)) return;
	BigNum e, h; int i, j, p;
	c.len = a.len; d.len = 1; h = b; h.sign = true;
	for (i = c.len-1; i >= 0; i--) {
		p = a.num[i];
		for (j = 1000; j >= 1; j /= 10) {
			multiply10(d);
			d.num[0] += (p/j); p %= j;
			while (compare(d, h) >= 0) {
				subtract(d, h, e); d = e;
				c.num[i] += j;
			}
		}
	}
	while (c.len > 1 && c.num[c.len-1] == 0) c.len--;
	if (compare(d, 0) && !a.sign) {
		j = c.sign ? 1 : -1;
		plus(c, j, e); c = e;
		subtract(h, d, e); d = e;
	}
	return;
}
//*****************************************************************
 
        

int main(void)
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	int t;
	static char in[1<<20];
	int len;
	int i, j;
	
	scanf("%d", &t);
	for (int ca = 1; ca <= t; ++ca) {
		scanf("%s", in);
		len = strlen(in);
		/*
		if (len == 1) {
			printf("Case #%d: 0\n", ca);
			continue;
		}
		*/
		std::map<char, int> m;
		bool mk[64] = {0, 1};
		int n = -1;
		m[in[0]] = 1;
		for (i = 0; i < len; ++i) {
			if (!m.count(in[i])) {
				while (mk[++n]);
				m[in[i]] = n; mk[n] = 1;
			}
			in[i] = m[in[i]];
		}
		/*
		printf("m.size = %d\n", m.size());
		printf("in:");
		for (i = 0; i < len; ++i)
			printf("%d  ", in[i]);
		putchar('\n');
		*/
		BigNum cost(m.size()), sum(0), tt(1), tc;
		if (compare(cost, 1) == 0) increase(cost, 1);
		for (i = len - 1; i >= 0; --i) {
			//void multiply(const BigNum &a, const BigNum &b, BigNum &c);
			//void increase(BigNum &a, const BigNum&b);
			multiply(tt, in[i], tc);
			increase(sum, tc);
			//sum += tt * in[i];
			multiply(tt, cost, tc);
			tt = tc;
			//tt *= cost;
		}
		printf("Case #%d: ", ca);
		print(sum);
		putchar('\n');
	}
	
	return 0;
}
