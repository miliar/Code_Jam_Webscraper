#include <cstdio>
#include <cstring>
#include <cctype>
#include <utility>
#include <algorithm>

#define REP(AA,BB) for(AA=0; AA<BB; ++AA)
#define FOR(AA,BB,CC) for(AA=BB; AA<CC; ++AA)
#define FC(AA,BB) for(typeof(AA.begin()) BB=AA.begin(); BB!=AA.end(); ++BB)

using namespace std;

#define MSIZE 7
#define BASE 1000000000

struct BigInteger {
    int c[MSIZE], len;
    BigInteger(int);
    BigInteger(long long);
    BigInteger operator+(const BigInteger&) const;
    BigInteger& operator+=(const BigInteger&);
    BigInteger operator-(const BigInteger&) const;
    BigInteger& operator-=(const BigInteger&);
    int operator<(const BigInteger&) const;
    int operator<=(const BigInteger&) const;
    int operator>(const BigInteger&) const;
    int operator>=(const BigInteger&) const;
    int operator==(const BigInteger&) const;
    int operator!=(const BigInteger&) const;
    BigInteger singleMul(int) const;
    BigInteger shiftLeft(int) const;
    BigInteger shiftRight(int) const;
    BigInteger operator*(const BigInteger&) const;
    BigInteger& operator*=(const BigInteger&);
    pair<BigInteger, BigInteger> divide(const BigInteger&) const;
    BigInteger operator/(const BigInteger&) const;
    BigInteger& operator/=(const BigInteger&);
    BigInteger operator%(const BigInteger&) const;
    BigInteger& operator%=(const BigInteger&);
    void print(void) const;
    void get_decimal(int);
};

BigInteger::BigInteger(int n=0) {
    memset(c, 0, sizeof c); len=0;
    if(n==0) {
        c[0]=0;
        len=1;
        return;
    }
    while(n>0) {
        c[len++]=n%BASE;
        n/=BASE;
    }
}

BigInteger::BigInteger(long long n) {
    memset(c, 0, sizeof c); len=0;
    while(n>0LL) {
        c[len++]=n%BASE;
        n/=BASE;
    }
}

BigInteger BigInteger::operator+(const BigInteger& y) const {
    int m=max(len, y.len), i, j;
    BigInteger res=*this;
    REP(i,m) {
        res.c[i]+=y.c[i];
        if(res.c[i]>=BASE) {
            ++res.c[i+1];
            res.c[i]-=BASE;
        }
    }
    if(res.c[m]>0)
        res.len=m+1;
    else
        res.len=m;
    return res;
}

BigInteger& BigInteger::operator+=(const BigInteger& y) {
    return (*this)=(*this)+y;
}

BigInteger BigInteger::operator-(const BigInteger& y) const {
    int i, j;
    BigInteger res=*this;
    REP(i,len) {
        if(res.c[i]>=y.c[i])
            res.c[i]-=y.c[i];
        else {
            --res.c[i+1];
            res.c[i]=res.c[i]+BASE-y.c[i];
        }
    }
    res.len=len;
    while(res.len>1 && res.c[res.len-1]==0)
        --res.len;
    return res;
}

BigInteger& BigInteger::operator-=(const BigInteger& y) {
    return (*this)=(*this)-y;
}

int BigInteger::operator<(const BigInteger& y) const {
    if(len<y.len)
        return 1;
    else if(len>y.len)
        return 0;
    int i;
    for(i=len-1; i>=0; --i)
        if(c[i]<y.c[i])
            return 1;
        else if(c[i]>y.c[i])
            return 0;
    return 0;
}

int BigInteger::operator>(const BigInteger& y) const {
    return (y<(*this));
}

int BigInteger::operator==(const BigInteger& y) const {
    if(len!=y.len)
        return 0;
    int i;
    for(i=len-1; i>=0; --i)
        if(c[i]!=y.c[i])
            return 0;
    return 1;
}

int BigInteger::operator<=(const BigInteger& y) const {
    return !((*this)>y);
}

int BigInteger::operator>=(const BigInteger& y) const {
    return !((*this)<y);
}

int BigInteger::operator!=(const BigInteger& y) const {
    return !((*this)==y);
}

BigInteger BigInteger::singleMul(int p) const {
    if(p==1)
        return (*this);
    BigInteger res;
    if(p==0)
        return res;
    int i; long long x;
    REP(i,len) {
        x=c[i]; x*=p;
        res.c[i]+=(int)(x%BASE);
        if(res.c[i]>=BASE) {
            res.c[i+1]+=res.c[i]/BASE;
            res.c[i]%=BASE;
        }
        res.c[i+1]+=(int)(x/BASE);
    }
    res.len=len;
    if(res.c[len]>0)
        ++res.len;
    return res;
}

BigInteger BigInteger::shiftLeft(int p) const {
    BigInteger res;
    if(len==1 && c[0]==0)
        return res;
    int i;
    REP(i,len)
        res.c[i+p]=c[i];
    res.len=len+p;
    return res;
}

BigInteger BigInteger::shiftRight(int p) const {
    BigInteger res;
    if(len==1 && c[0]==0)
        return res;
    int i;
    REP(i,len-p)
        res.c[i]=c[i+p];
    res.len=len-p;
    return res;
}

BigInteger BigInteger::operator*(const BigInteger& y) const {
    BigInteger res; int i;
    REP(i,y.len)
        res+=(singleMul(y.c[i]).shiftLeft(i));
    return res;
}

BigInteger& BigInteger::operator*=(const BigInteger& y) {
    return (*this)=(*this)*y;
}

pair<BigInteger, BigInteger> BigInteger::divide(const BigInteger& y) const {
    BigInteger res, z=shiftRight(len-y.len), t;
    int i, j, k, l, r, mid;
    res.len=len-y.len+1;
    for(k=len-y.len; k>=0; --k) {
        l=0; r=BASE-1;
        while(l<=r) {
            mid=(l+r)/2;
            t=y.singleMul(mid);
            if(t<=z) {
                if(mid==BASE-1 || t+y>z)
                    break;
                l=mid+1;
            }
            else
                r=mid-1;
        }
        res.c[k]=mid;
        z-=t;
        if(k>0) {
            z=z.shiftLeft(1);
            z.c[0]=c[k-1];
        }
    }
    while(res.len>1 && res.c[res.len-1]==0)
        --res.len;
    return make_pair(res,z);
}

BigInteger BigInteger::operator/(const BigInteger& y) const {
    return divide(y).first;
}

BigInteger& BigInteger::operator/=(const BigInteger& y) {
    return (*this)=divide(y).first;
}

BigInteger BigInteger::operator%(const BigInteger& y) const {
    return divide(y).second;
}

BigInteger& BigInteger::operator%=(const BigInteger& y) {
    return (*this)=divide(y).second;
}

void BigInteger::print(void) const {
    int i;
    printf("%d", c[len-1]);
    for(i=len-2; i>=0; --i)
        printf("%09d", c[i]);
    puts("");
}           

void BigInteger::get_decimal(int max_n) {
    char *d=new char[max_n];
    int i, j, k, n;
    for(n=0; isdigit(d[n]=getchar()); ++n);
    d[n]=0; len=0;
    for(--n; n>=0; ) {
        for(j=0, i=0, k=1; i<9 && n>=0; ++i, --n, k*=10)
            j+=(d[n]-'0')*k;
        c[len++]=j;
    }
}

BigInteger gcd(BigInteger a, BigInteger b) {
    if(b.len==1 && b.c[0]==0)
        return a;
    return gcd(b,a%b);
}

BigInteger p[1010];

int main(void) {
    int t, T, n, m, i, j, k;
    scanf("%d", &T);
    FOR(t,1,T+1) {
    	scanf("%d", &n); getchar();
    	REP(i,n)
    		p[i].get_decimal(53);
    	sort(p,p+n); BigInteger d=p[n-1]-p[n-2];
    	for(i=n-2; i>0; --i)
    		d=gcd(d, p[i]-p[i-1]);
    	printf("Case #%d: ", t);
    	if((p[0]%d)==BigInteger(0))
    		printf("0\n");
    	else
    		(d-(p[0]%d)).print();
    }
    return 0;
}

