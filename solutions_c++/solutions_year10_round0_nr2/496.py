#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

#define MAXN 1001

typedef long long ll;
const int base = 1000000000;

#define maxl 1001

struct bigint
{
	int val[maxl],l;
	bigint() : l(0) {}
	bigint(const bigint& x) : l(x.l) { memcpy(val,x.val,l*sizeof*val); }
	bigint(int x) : l(0) { for (;x>0; x /= base) val[l++] = x%base; }
	bigint& operator=(const bigint& x) { l = x.l; memcpy(val,x.val,l*sizeof*val); return *this; }
	bool operator<(const bigint& x) const
	{
		if (l!=x.l) return l<x.l?1:0;
		for (int i = l-1; i >= 0; --i)
			if (val[i]!=x[i]) return val[i]<x[i]?1:0;
		return 0;
	}
	int& operator[](int i) { return val[i]; }
	int operator[](int i) const { return val[i]; }
} a[MAXN], b[MAXN], z;


inline int compare(const bigint& a,const bigint& b)
{
	if (a.l!=b.l) return a.l>b.l?1:-1;
	for (int i = a.l-1; i >= 0; --i)
		if (a[i]!=b[i]) return a[i]>b[i]?1:-1;
	return 0;
}

inline bigint operator+(const bigint& a,const bigint& b)
{
	bigint r;
	int i,carry=0;
	for (i = 0; i < a.l || i < b.l || carry > 0; ++i)
	{
		if (i<a.l) carry += a[i];
		if (i<b.l) carry += b[i];
		r[i] = carry%base;
		carry /= base;
	}         
	r.l = i;
	return r;
}

inline bigint operator-(const bigint& a,const bigint& b)
{
	bigint r;
	int carry = 0;
	r.l = a.l;
	for (int i = 0; i < r.l; ++i)
	{
		r[i] = a[i] - carry;
		if (i<b.l) r[i] -= b[i];
		if (r[i]<0) r[i] += base, carry = 1; else carry = 0;
	}
	while(r.l>0 && r[r.l-1]==0) --r.l;
	return r;
}

inline bigint operator*(const bigint& a,const int b)
{
	int i;
	if (!b) return 0;
	bigint r;
	ll carry = 0;
	for (i = 0; i < a.l || carry > 0; ++i)
	{
		if (i<a.l) carry += ll(a[i])*b;
		r[i] = carry%base;
		carry /= base;
	}
	r.l = i;
	return r;
}

inline bigint operator*(const bigint& a,const bigint& b)
{
	if (!b.l) return 0;
	bigint r;
	for (int i = 0; i < a.l; ++i)
	{
		ll carry = 0;
		for (int j = 0; j < b.l || carry > 0; ++j)
		{
			if (j<b.l) carry += ll(a[i])*b[j];
			if (i+j<r.l) carry += r[i+j];
			if (i+j>=r.l) r[r.l++] = carry%base;
			else r[i+j] = carry%base;
			carry /= base;
		}
	}
	return r;
}

inline bigint operator/(const bigint& a,const int b)
{
	bigint r;
	ll c = 0;
	for (int i = a.l-1; i >= 0; --i)
	{
		c = c*base + a[i];
		r[i] = c/b;
		c %= b;
	}
	r.l = a.l;
	while(r.l>0 && r[r.l-1]==0) --r.l;
	return r;
}

inline bigint operator/(const bigint& a,const bigint& b)
{
	bigint r, carry = 0;
	int l,ri,m;
	for (int i = a.l-1; i >= 0; --i)
	{
		carry = carry*base+a[i];
		l = 0;
		ri = base-1;
		while(l<ri)
		{
			m = (l+ri+1)/2;
			if (compare(b*m,carry)<=0) l = m; else ri = m-1;
		}
		r[i] = l;
		carry = carry - b*l;
	}
	r.l = a.l;
	while(r.l>0 && r[r.l-1]==0) --r.l;
	return r;
}

inline bigint operator%(const bigint& a,const bigint& b)
{
	bigint r, carry = 0;
	int l,ri,m;
	for (int i = a.l-1; i >= 0; --i)
	{
		carry = carry*base+a[i];
		l = 0;
		ri = base-1;
		while(l<ri)
		{
			m = (l+ri+1)/2;
			if (compare(b*m,carry)<=0) l = m; else ri = m-1;
		}
		r[i] = l;
		carry = carry - b*l;
	}
	r.l = a.l;
	while(r.l>0 && r[r.l-1]==0) --r.l;
	return carry;
}                

inline void print(const bigint& x)
{
	cout << x[x.l-1];
	for (int i = x.l-2; i >= 0; --i)
		for (int j = base/10; j>0; j/=10)
			cout << char((x[i]/j) % 10 + '0');
	cout << endl;
}

inline void stob(string x,bigint& a)
{
	a = bigint(0);
	for (int i = 0; i < x.size(); ++i)
		a = a*10+(x[i]-'0');
}

char c[1001];
string s;

int tt, n;

inline bigint gcd(bigint a, bigint b)
{
	while(a.l>0 && b.l>0)
	{
		if (a<b)
			b = b%a;
		else
			a = a%b;
	}
	return a+b;
}

int main()
{
	freopen("input","r",stdin);
	freopen("output","w",stdout);
	scanf("%d", &tt);
	for (int t = 0; t < tt; ++t)
	{
		scanf("%d ", &n);
		for (int i = 0; i < n; ++i)
		{
			scanf("%s", c);
			stob(c, a[i]);
		}
		sort(a, a+n);
		for (int i = 0; i < n-1; ++i)
			b[i] = a[i+1]-a[i];
		for (int i = 1; i < n-1; ++i)
			b[0] = gcd(b[0], b[i]);
		z = (a[0]+b[0]-1)/b[0] * b[0];
		z = z-a[0];
		printf("Case #%d: ", t+1);
		print(z);
	}
	return 0;
}
