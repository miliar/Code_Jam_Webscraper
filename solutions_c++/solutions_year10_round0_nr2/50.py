#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#include <iostream>
#include <sstream>
#include <iomanip>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <utility>
#include <numeric>
#include <complex>
#include <functional>
#include <bitset>
#include <string>
#include <valarray>
#include <algorithm>
using namespace std;

#define MP(a,b)     make_pair(a,b)
#define two(i)      (1<<(i))
#define REP(i,n)    for(int i=0; i<(n); ++i)
#define FOR(i,s,e)  for(int i=(s); i<(e); ++i)
#define FORD(i,s,e) for(int i=(s); i>=(e); --i)
typedef long long i64;
typedef unsigned long long u64;

const unsigned int MaxLen = 8;
const unsigned int BitMax = 100000000;
const unsigned int BitLen = 8;

struct BigUInt {
	unsigned  int  d[MaxLen];
	unsigned  int  len;
	
	bool isZero() {return len==0 || len==1 && d[0]==0;}

	BigUInt(int val = 0) {
		len = 0;
		do {
			d[len++] = val%BitMax;
			val /= BitMax;
		}while(val > 0);
	}

	BigUInt& set(const char* s) {
		if(!s) {
			len=1; d[0]=0; return *this;
		}
		int  beg=0, idx=0, ten=1, cur=0;

		while(s[beg] == '0') ++beg;
		if(!s[beg]) --beg;

		while(s[idx]) ++idx;
		len = 0;
		for(--idx; idx>=beg; --idx) {
			if(ten == BitMax) {
				d[len++] = cur;
				ten = 1;
				cur = 0;
			}
			cur += (s[idx]-'0')*ten;
			ten *= 10;
		}
		d[len++] = cur;
		return *this;
	}
	string to_str() {
		ostringstream  os;
		int  idx = len-1;
		os << d[idx--];
		for(; idx>=0; --idx)
			os << setw(BitLen) << setfill('0') << d[idx];
		return os.str();
	}

	int  compare_to(const BigUInt& b) const {
		const BigUInt& a = *this;
		if(a.len != b.len)  return a.len < b.len ? -1 : 1;
		for(int i=len-1; i>=0; --i) if(a.d[i] != b.d[i])
			return a.d[i] < b.d[i] ? -1 : 1;
		return 0;
	}

	bool operator==(const BigUInt& v) const {return compare_to(v) == 0;}
	bool operator!=(const BigUInt& v) const {return compare_to(v) != 0;}
	bool operator <(const BigUInt& v) const {return compare_to(v) <  0;}
	bool operator<=(const BigUInt& v) const {return compare_to(v) <= 0;}
	bool operator >(const BigUInt& v) const {return compare_to(v) > 0;}
	bool operator>=(const BigUInt& v) const {return compare_to(v) >= 0;}
	
	
	BigUInt operator+(const BigUInt& b) const {
		const BigUInt& a=*this;
		BigUInt  c;  //the ans
		unsigned int  i, carry = 0;
		for(i=0; i<a.len || i<b.len || carry; ++i) {
			if(i < a.len)  carry += a.d[i];
			if(i < b.len)  carry += b.d[i];
			c.d[i] = carry % BitMax;
			carry /= BitMax;
		}
		c.len = i;
		return  c;
	}

	BigUInt operator-(const BigUInt& b) const {
		const BigUInt& a=*this;
		BigUInt  c = *this;  //the ans
		unsigned int  i, borrow = 0;
		for(i=0; i<b.len || borrow; ++i) {
			if(i < b.len)  borrow += b.d[i];
			if(c.d[i] < borrow) {
				c.d[i] = BitMax + c.d[i] - borrow;
				borrow = 1;
			}
			else {
				c.d[i] -= borrow;
				borrow = 0;
			}
		}
		for(i=c.len-1; i>0 && c.d[i]==0; --i);
		c.len = i+1;
		return  c;
	}

	BigUInt operator*(const BigUInt& b) const {
		const BigUInt& a=*this;
		BigUInt  c;  //the ans
		memset(&c, 0, sizeof(c));
		unsigned int  i, j, k=0;
		unsigned long long cur = 0;
		for(i=0; i<a.len; ++i) for(j=0; j<b.len; ++j) {
			cur = a.d[i]*1LL*b.d[j];
			for(k=i+j; cur; cur/=BitMax, ++k) {
				cur += c.d[k];
				c.d[k] = cur%BitMax;
			}
			if(k > c.len)  c.len = k;
		}
		return  c;
	}


	BigUInt operator/(const BigUInt& b) const {
		const BigUInt& a = *this;
		BigUInt  c; //the answer
		BigUInt  r, t;
		unsigned int  lo, hi, mi;
		for(int i=a.len-1; i>=0; --i) {
			r = r*BitMax + a.d[i];
			if(r < b) {c.d[i] = 0; continue;}
			if(i >= c.len) c.len = i+1;
			lo = 0;   hi = BitMax;
			while(lo+1 < hi) {
				mi = (lo + hi) >> 1;
				t = b*mi;
				if(t <= r)  lo = mi;
				else 		hi = mi;
			}
			c.d[i] = lo;
			r = r - b*lo;
		}
		return c;
	}

	BigUInt operator%(const BigUInt& b) const {
		const BigUInt& a = *this;
		return  a - (a/b)*b;
	}

};



string name = "B-large";
bool   is_file__ = true;

int  N;
BigUInt  srcT[1024];
BigUInt  factor;


BigUInt gcd(BigUInt a, BigUInt b) {
	BigUInt  t = 0;
	if(a < b) {t=a; a=b; b=t;}
	while(!b.isZero()) {
		t=a%b; a=b; b=t;
	} return a;
}

void calc_factor() {
	factor = srcT[1] - srcT[0];
	for(int i=2; i<N; ++i) {
		factor = gcd(factor, srcT[i]-srcT[i-1]);
		if(factor == 1)
			break;
	}
}

string go() {
	char  ts[64];

	scanf("%d", &N);
	REP(i, N) {
		scanf("%s", ts);
		srcT[i].set(ts);
	}
	sort(srcT, srcT+N);

	calc_factor();

	if(factor == 1)
		return "0";

	BigUInt y = srcT[0]%factor;

	if(y == 0)
		return "0";

	y = factor - y;

	return y.to_str();
}

void solve() {
	int  T;
	scanf("%d", &T);
	REP(idx_case, T) {
		
		printf("Case #%d: %s\n", idx_case+1,
			go().c_str());

	}
}


void set_file() {
	string in = name+".in";
	string ou = name + ".out";
	freopen(in.c_str(), "r", stdin);
	freopen(ou.c_str(), "w", stdout);
}

int  main(int argc, char* argv[])
{
	if(is_file__)
		set_file();
	solve();
	return 0;
}

