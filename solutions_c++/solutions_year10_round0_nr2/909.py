#include <cstdio>
#include <cstring>
#include <algorithm>
#define maxlen 100
#define base 10
using namespace std;
struct bignum {
	int size, sign;
	short num[maxlen];//Start from num[1]
	bignum() {
		size = 0;
		sign = 0;
		memset(num, 0, sizeof(num));
	}
} t[1010];

bignum operator -(const bignum & a) {
	bignum c;
	c = a;
	c.sign = !a.sign;
	return c;
}
// size = number of digits of bignum
// sign = sign of bignum
// (0 => positive, 1 => negative)
void printbignum(const bignum & a) {
    int i;
    if (a.size == 0) {
        printf("0\n");
        return;
    }
    if (a.size == 1 && a.num[1] == 0) {
        printf("0\n");
        return;
    }
	if (a.sign == 1)
		printf("-");
    for (i = a.size; i > 1; i--)
        if (a.num[i] != 0)
            break;
	for ( ; i >= 1; i--)
		printf("%d", a.num[i]);
	printf("\n");
}

int compare(const bignum & a, const bignum & b) {// A > B === 1; A = B === 0; A < B === -1
	if (a.sign < b.sign)
		return 1;
	else {
		if (a.sign > b.sign)
			return -1;
		else {
			for (int i = max(a.size, b.size); i > 0; i--) {
				if (a.num[i] > b.num[i]) {
					if (a.sign == 0)
						return 1;
					else
						return -1;
				}
				else if (a.num[i] < b.num[i]){
					if (a.sign == 0)
						return -1;
					else
						return 1;
				}
			}
			return 0;
		}
	}
}

bignum absolute_substrcat(const bignum & a, const bignum & b) {
	int borrow = 0, maxsize;
	bignum c;
	maxsize = max(a.size, b.size);
	for (int pos = 1; pos <= maxsize; pos++) {
		c.num[pos] = a.num[pos] - b.num[pos] - borrow;
		if (c.num[pos] < 0) {
			c.num[pos] += base;
			borrow = 1;
		}
		else
			borrow = 0;
		if (c.num[pos] != 0)
			c.size = pos;
	}
	return c;
}

bignum absolute_add(const bignum & a, const bignum & b) {
	int carry = 0;
	bignum c;
	int maxsize = max(a.size, b.size);
	for (int pos = 1; pos <= maxsize; pos++) {
		c.num[pos] = a.num[pos] + b.num[pos] + carry;
		carry = c.num[pos] / base;
		c.num[pos] %= base;
	}
	if (carry != 0) {
		c.num[maxsize + 1] = carry;
		c.size = maxsize + 1;
	}
	else
		c.size = maxsize;
	return c;
}

bignum add(const bignum & a, const bignum & b) {//加法 
	if (a.sign == b.sign) {
		bignum c = absolute_add(a, b);
		c.sign = a.sign;
		return c;
	}
	else {
		if (compare(a, b) == 1) {
			if (compare(a, -b) == 1) {
				bignum c = absolute_substrcat(a, b);
				c.sign = a.sign;				
				return c;
			}
			else {
				bignum c = absolute_substrcat(b, a);
				c.sign = b.sign;
				return c;
			}
		}
		else {
			if (compare(-a, b) == 1) {
				bignum c = absolute_substrcat(a, b);
				c.sign = a.sign;
				return c;
			}
			else {
				bignum c = absolute_substrcat(b, a);
				c.sign = b.sign;
				return c;
			}
		}
	}
}

bignum substract(const bignum & a, const bignum & b) {//减法 
	return add(a, -b);
}

bignum multiply_by_scalar(const bignum & a, int s) {//大整数乘以小整数 
	bignum b;
	if (s < 0) {
		b.sign = 1 - a.sign;
		s = -s;
	}
	else
		b.sign = a.sign;
	int carry = 0, pos;
	for (pos = 1; pos <= a.size; pos++) {
		b.num[pos] = a.num[pos] * s + carry;
		carry = b.num[pos] / base;
		b.num[pos] %= base;
	}
	pos = a.size + 1;
	while(carry != 0) {
		b.num[pos] = carry % base;
		carry /= base;
		pos++;
	}
	b.size = pos - 1;
	return b;
}

void multiply_and_add(const bignum & a, int s, int offset, bignum & c) {
	int carry = 0, pos;
	for (pos = 1; pos <= a.size; pos++) {
		c.num[pos + offset] += a.num[pos] * s + carry;
		carry = c.num[pos + offset] / base;
		c.num[pos + offset] %= base;
	}
	pos = a.size + offset + 1;
	while (carry != 0) {
		c.num[pos] += carry;
		carry = c.num[pos] / base;
		c.num[pos] %= base;
		pos++;
	}
	if (c.size < pos - 1)
		c.size = pos - 1;
}

bignum multiply(const bignum & a, const bignum & b) {//大整数乘法 
	bignum c;
	int pos;
	for (pos = 1; pos <= b.size; pos++) {
		multiply_and_add(a, b.num[pos], pos - 1, c);
	}
	c.sign = (a.sign + b.sign) % 2;
	return c;
}

bignum divide_by_bignum(const bignum & a, const bignum & b, bignum & c) {//大整数除法，返回余数
	bignum rem, tmp;
	rem.size = 1, rem.sign = 0, rem.num[1] = 0;
    c.sign = 0;
	int pos;
	for (pos = a.size; pos > 0; pos--) {
		rem = multiply_by_scalar(rem, base);
		tmp.size = 1, tmp.sign = 0, tmp.num[1] = a.num[pos];
		rem = add(rem, tmp);
		c.num[pos] = 0;
		while(b.sign == 0 && compare(rem, b) >= 0) {
			c.num[pos]++;
			rem = substract(rem, b);
		}
        while(b.sign == 1 && compare(rem, -b) >= 0) {
            c.num[pos]++;
            rem = substract(rem, -b);
        }
		if (c.num[pos] > 0 && pos > c.size)
			c.size = pos;
	}
    if (a.sign == 1 && b.sign == 1) {
        rem.sign = 1;
        c.sign = 0;
    }
    else if (a.sign == 0 && b.sign == 1) {
        rem.sign = 0;
        c.sign = 1;
    }
    else if (a.sign == 1 && b.sign == 0) {
        rem.sign = 1;
        c.sign = 1;
    }
	return rem;
}

bignum gcd(const bignum & a, const bignum & b) {
    //printf("ddddddddddddddddd ");
    //printbignum(b);
    if (b.size == 0) {
        return a;
    }
    if (b.size == 1 && b.num[1] == 0) {
        return a;
    }
    bignum temp;
    return gcd(b, divide_by_bignum(a, b, temp));
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int C, N, tc, i, j, k;
    char tmp[60];
    bignum jian;
    scanf("%d", &C);
    for (tc = 1; tc <= C; tc++) {
        scanf("%d", &N);
        for (i = 1; i <= N; i++) {
            scanf("%s", &tmp);
            t[i].size = strlen(tmp);
            memset(t[i].num, 0, sizeof(t[i].num));
            //printf("%d ", t[i].size);
            t[i].sign = 0;
            for (k = 0, j = t[i].size; j >= 1; j--, k++)
                t[i].num[j] = tmp[k] - '0';
        }
        //printbignum(t[2]);
        bignum d;
        if (compare(t[1], t[2]) >= 0)
            d = substract(t[1], t[2]);
        else
            d = substract(t[2], t[1]);
        /*if (d.size == 0 || (d.size == 1 && d.num[1] == 0)) {
            d.sign = 0;
            d.size = 1;
            d.num[1] = 1;
        }*/
        //printf("ready\n");
        for (i = 1; i <= N; i++) {
            for (j = i + 1; j <= N; j++) {
                //printbignum(d);
                if (compare(t[i], t[j]) >= 0) {
                    jian = substract(t[i], t[j]);
                    if (compare(jian, d) >= 0)
                        d = gcd(jian, d);
                    else
                        d = gcd(d, jian);
                } else {
                    jian = substract(t[j], t[i]);
                    if (compare(jian, d) >= 0)
                        d = gcd(jian, d);
                    else
                        d = gcd(d, jian);
                }
                //printf("########");
                //printbignum(d);
            }
        }
        //printbignum(d);
        //printf("output\n");
        bignum one;
        one.size = 1; one.sign = 0; one.num[1] = 1;
        bignum temp1, temp2, ans;
        temp1 = divide_by_bignum(add(t[1], substract(d, one)), d, temp2);
        temp2 = multiply(temp2, d);
        ans = substract(temp2, t[1]);
        printf("Case #%d: ", tc);
        printbignum(ans);
    }
    return 0;
}
