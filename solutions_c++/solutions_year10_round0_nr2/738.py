#include <iostream>
using namespace std;
const int DN = 512;
const int F = 10000, FK = 4;
class BigInt {
private:
	int n[DN], len, sign;
	void format();
	bool lessThan(const BigInt&, int) const;
	void sub(const BigInt&, int);
	void add(const BigInt&);
public:
	BigInt(int e = 0) : len(1), sign(1) { memset(n, 0, sizeof(n)); n[0] = e; }
	BigInt(char*, int);

	BigInt& operator =(int k) { return *this = BigInt(k); }

	bool operator <(const BigInt&) const;
	bool operator >(const BigInt& b) const { return b < *this; }
	bool operator <=(const BigInt& b) const { return !(*this > b); }
	bool operator >=(const BigInt& b) const { return !(*this < b); }
	bool operator !=(const BigInt& b) const { return *this > b || *this < b; }
	bool operator ==(const BigInt& b) const { return !(*this != b); }

	bool operator <(int b) const { return *this < BigInt(b); }
	bool operator >(int b) const { return *this > BigInt(b); }
	bool operator <=(int b) const { return *this <= BigInt(b); }
	bool operator >=(int b) const { return *this >= BigInt(b); }
	bool operator !=(int b) const { return *this != BigInt(b); }
	bool operator ==(int b) const { return *this == BigInt(b); }

	void operator +=(const BigInt&);
	void operator -=(const BigInt&);
	void operator *=(const BigInt&);
	void operator /=(const BigInt&);
	void operator %=(const BigInt& b) { *this -= *this/b*b; }

	BigInt operator +(const BigInt& b) const { BigInt r = *this; r += b; return r; }
	BigInt operator -(const BigInt& b) const { BigInt r = *this; r -= b; return r; }
	BigInt operator *(const BigInt& b) const { BigInt r = *this; r *= b; return r; }
	BigInt operator /(const BigInt& b) const { BigInt r = *this; r /= b; return r; }
	BigInt operator %(const BigInt& b) const { BigInt r = *this; r %= b; return r; }

	void operator +=(int k) { *this += BigInt(k); }
	void operator -=(int k) { *this -= BigInt(k); }
	void operator *=(int);
	void operator /=(int);
	void operator %=(int k) { *this -= *this/k*k; }

	BigInt operator +(int k) const { BigInt r = *this; r += k; return r; }
	BigInt operator -(int k) const { BigInt r = *this; r -= k; return r; }
	BigInt operator *(int k) const { BigInt r = *this; r *= k; return r; }
	BigInt operator /(int k) const { BigInt r = *this; r /= k; return r; }
	BigInt operator %(int k) const { BigInt r = *this; r %= k; return r; }

	friend BigInt operator +(int k, const BigInt& b) { return BigInt(k)+b; }
	friend BigInt operator -(int k, const BigInt& b) { return BigInt(k)-b; }
	friend BigInt operator *(int k, const BigInt& b) { return BigInt(k)*b; }
	friend BigInt operator /(int k, const BigInt& b) { return BigInt(k)/b; }
	friend BigInt operator %(int k, const BigInt& b) { return BigInt(k)%b; }

	void print() const;
	void sprint(char*) const;
};
BigInt::BigInt(char* str, int slen = -1) {
	memset(n, 0, sizeof(n));
	sign = (*str == '-' ? -1 : 1);
	if(!isdigit(*str)) str++;
	if(slen == -1) slen = strlen(str);
	len = (slen+FK-1)/FK;
	for(int i = slen, k = 0; i > 0; i -= FK, k++) {
		int sum = 0;
		for(int j = max(i-FK, 0); j < i; j++)
			sum = sum*10+str[j]-'0';
		n[k] = sum;
	}
	format();
}
void BigInt::format() {
	while(len > 1 && n[len-1] == 0) len--;
	if(len == 1 && n[0] == 0) sign = 1;
}
bool BigInt::lessThan(const BigInt& b, int bg = 0) const {
	if(len-bg != b.len) return len-bg < b.len;
	for(int i = len-bg-1; i >= 0; i--)
		if(n[bg+i] != b.n[i]) return n[bg+i] < b.n[i];
	return false;
}
void BigInt::add(const BigInt& b) {
	len >?= b.len;
	int r = 0;
	for(int i = 0; i < len; i++) {
		n[i] += r+b.n[i];
		r = n[i]/F; n[i] %= F;
	}
	if(r != 0) n[len++] = r;
	format();
}
void BigInt::sub(const BigInt& b, int bg = 0) {
        int length = len - bg;
	for(int i = 0; i < length; i++) {
		n[bg+i] -= b.n[i];
		if(n[bg+i] < 0) { n[bg+i] += F; n[bg+i+1]--; }
	}
	format();
}
bool BigInt::operator <(const BigInt& b) const {
	if(sign != b.sign) return sign < b.sign;
	else if(sign == 1) return lessThan(b);
	else return b.lessThan(*this);
}
void BigInt::operator +=(const BigInt& b) {
	if(sign == b.sign) add(b);
	else if(b.lessThan(*this)) sub(b);
	else {
		int cs = -sign;
		BigInt r = b; r.sub(*this);
		*this = r; sign = cs;
		format();
	}
}
void BigInt::operator -=(const BigInt& b) {
	if(sign != b.sign) add(b);
	else if(b.lessThan(*this)) sub(b);
	else {
		int cs = -sign;
		BigInt r = b; r.sub(*this);
		*this = r; sign = cs;
		format();
	}
}
void BigInt::operator *=(const BigInt& c) {
	BigInt a = *this, b = c;
	memset(n, 0, sizeof(n)); len = a.len+b.len; sign *= b.sign;
	for(int i = 0; i < a.len; i++)
		for(int j = 0; j < b.len; j++) {
			int k = i+j;
			n[k] += a.n[i]*b.n[j];
			if(n[k] >= F) { n[k+1] += n[k]/F; n[k] %= F; len >?= k+2; }
		}
	format();
}
void BigInt::operator /=(const BigInt& c) {
	BigInt a = *this, b = c;
	memset(n, 0, sizeof(n));
	len = max(a.len-b.len+1, 0); sign *= b.sign;
	for(int i = len-1; i >= 0; i--) {
		int al = a.n[max(i+b.len, a.len)-1], bl = b.n[b.len-1], ar = al+1, br = bl+1;
		if(a.len-i != b.len) { al *= F; ar *= F; }
		int l = al/br, r = ar/bl+1;
		while(r-l != 1) {
			int mid = (l+r)/2;
			if(a.lessThan(b*mid, i)) r = mid;
			else l = mid;
		}
		a.sub(b*l, i);
		n[i] = l;
	}
	if(len == 0) len++;
	format();
}
void BigInt::operator *=(int k) {
	int r = 0;
	for(int i = 0; i < len; i++) {
		n[i] = n[i]*k+r;
		r = n[i]/F; n[i] %= F;
	}
	if(r != 0) n[len++] = r;
	format();
}
void BigInt::operator /=(int k) {
	int r = 0;
	for(int i = len-1; i >= 0; i--) {
		n[i] += r*F;
		r = n[i]%k; n[i] /= k;
	}
	format();
}
void BigInt::print() const {
	if(sign == -1) putchar('-');
	printf("%d", n[len-1]);
	for(int i = len-2; i >= 0; i--)
		printf("%0*d", FK, n[i]);
}
void BigInt::sprint(char* str) const {
	int index = 0;
	if(sign == -1) str[index++] = '-';
	sprintf(str+index, "%d", n[len-1]);
	index = strlen(str);
	for(int i = len-2; i >= 0; i--, index += FK)
		sprintf(str+index, "%0*d", FK, n[i]);
}
BigInt gcd(BigInt a,BigInt b)
{

    if(b==0)
    return a;
    return gcd(b,a%b);
}
    BigInt s[1024];
int main()
{
    freopen("large.in","r",stdin);
    freopen("large.out","w",stdout);
    int T;
    char num[100];
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++)
    {
        int n;
        scanf("%d",&n);
        BigInt gc;
        for(int i=0;i<n;i++)
        {
            scanf("%s",num);
            s[i]=BigInt(num);
            if(i==1)
            {
                gc=s[1]-s[0];
                if(gc<0)
                gc=0-gc;
            }
            else if(i>1)
            {
                BigInt tmp=s[i]-s[i-1];
                if(tmp<0)
                tmp=0-tmp;
                gc=gcd(max(tmp,gc),min(tmp,gc));
            }
            gc.sprint(num);
        }
        BigInt ans;
        if(gc==1)
        ans=0;
        else
        ans=(gc-s[0]%gc)%gc;
        ans.sprint(num);
        printf("Case #%d: %s\n",cas,num);
    }
    return 0;
}
