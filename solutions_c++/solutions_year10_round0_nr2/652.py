#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define forsn(i,s,n) for(int i=(s);i<(int)(n);i++)
#define dforn(i,n) for(int i=(n)-1;i>=0;i--)
#define dforsn(i,s,n) for(int i=(n)-1;i>=(int)(s);i--)

typedef long long tint;

// BIG INT START

typedef tint tipo;
#define BASEXP 6
#define BASE 1000000
#define LMAX 128

struct Long {
	int l;
	tipo n[LMAX];
	Long(tipo x) { 	l = 0; forn(i, LMAX) { n[i]=x%BASE; l+=!!x||!i; x/=BASE;} }
	Long(){*this = Long(0);}
	Long(string x) {
		l=(x.size()-1)/BASEXP+1;
		fill(n, n+LMAX, 0);
		tipo r=1;
		forn(i,x.size()){
			n[i / BASEXP] += r * (x[x.size()-1-i]-'0');
			r*=10; if(r==BASE)r=1;
		}
	}
};

void out(Long& a) {
	char msg[BASEXP+1];
	cout << a.n[a.l-1];
	dforn(i,a.l-1) {
		sprintf(msg, "%6.6llu", a.n[i]); cout << msg; // 6 = BASEXP !
	}
	cout << endl;
}
void invar(Long &a) {
	fill(a.n+a.l, a.n+LMAX, 0);
	while(a.l>1 && !a.n[a.l-1]) a.l--;
}

void lsuma(const Long&a, const Long&b, Long&c) { // c = a + b
	c.l = max(a.l, b.l);
	tipo q = 0;
	forn(i, c.l) q += a.n[i]+b.n[i], c.n[i]=q%BASE, q/=BASE;
	if(q) c.n[c.l++] = q;
	invar(c);
}
Long& operator+= (Long&a, const Long&b) { lsuma(a, b, a); return a; }
Long operator+ (const Long&a, const Long&b) { Long c; lsuma(a, b, c); return c; }

bool lresta(const Long&a, const Long&b, Long&c) { // c = a - b
	c.l = max(a.l, b.l);
	tipo q = 0;
	forn(i, c.l) q += a.n[i]-b.n[i], c.n[i]=(q+BASE)%BASE, q=(q+BASE)/BASE-1;
	invar(c);
	return !q;
}
Long& operator-= (Long&a, const Long&b) { lresta(a, b, a); return a; }
Long operator- (const Long&a, const Long&b) {Long c; lresta(a, b, c); return c;}

bool operator< (const Long&a, const Long&b) { Long c; return !lresta(a, b, c); }
bool operator<= (const Long&a, const Long&b) { Long c; return lresta(b, a, c); }
bool operator== (const Long&a, const Long&b) { return a <= b && b <= a; }

void lmul(const Long&a, const Long&b, Long&c) { // c = a * b
	c.l = a.l+b.l;
	fill(c.n, c.n+b.l, 0);
	forn(i, a.l) {
		tipo q = 0;
		forn(j, b.l) q += a.n[i]*b.n[j]+c.n[i+j], c.n[i+j] = q%BASE, q/=BASE;
		c.n[i+b.l] = q;
	}
	invar(c);
}

Long& operator*= (Long&a, const Long&b) { Long c; lmul(a, b, c); return a=c; }
Long operator* (const Long&a, const Long&b) { Long c; lmul(a, b, c); return c; }

void lmul(const Long&a, int b, Long&c) { // c = a * b
	int q = 0;
	forn(i, a.l) q += a.n[i]*b, c.n[i] = q%BASE, q/=BASE;
	c.l = a.l;
	while(q) c.n[c.l++] = q%BASE, q/=BASE;
}

Long& operator*= (Long&a, int b) { lmul(a, b, a); return a; }
Long operator* (const Long&a, int b) { Long c = a; c*=b; return c; }

void ldiv(const Long& a, tipo b, Long& c, tipo& rm) { // c = a / b ; rm = a % b
	rm = 0;
	dforn(i, a.l) {
		rm = rm * BASE + a.n[i];
		c.n[i] = rm / b; rm %= b;
	}
	c.l = a.l;
	invar(c);
}

void ldiv(const Long& a, const Long& b, Long& c, Long& rm) { // c = a / b ; rm = a % b
	rm = 0;
	dforn(i, a.l) {
		dforn(j, rm.l) rm.n[j+1] = rm.n[j];
		rm.n[0] = a.n[i]; rm.l++;
		tipo q = rm.n[b.l] * BASE + rm.n[b.l-1];
		tipo u = q / (b.n[b.l-1] + 1);
		tipo v = q /  b.n[b.l-1] + 1;
		while (u < v-1) {
			tipo m = (u+v)/2;
			if (b*m <= rm) u = m; else v = m;
		}
		c.n[i] = u;
		rm -= b*u;
	}
	c.l = a.l;
	invar(c);
}

// END BIG INT

void modu(Long &a, const Long &b)
{
	Long r,aux;
	ldiv(a,b,aux,r);
	a = r;
}

Long euclides(Long al, Long bl)
{
	Long *a = &al, *b = &bl;
	if (*a < *b) swap(a,b);
	while (!(*b == Long()))
	{
		modu(*a,*b);
		swap(a,b);
	}
	return *a;
}

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int TT; cin >> TT;
	forn(tt,TT)
	{
		int n; cin >> n;
		int mini = 0;
		vector<Long> v(n+5);
		Long i;
		forn(i,n)
		{
			string s; cin >> s;
			v[i] = Long(s);
			if (v[mini] > v[i])
				mini = i;
		}
		Long t0 = v[mini];
		forn(i,n) v[i] -= t0;
		Long mcd;
		forn(i,n) if (!(v[i] == Long())) mcd = euclides(mcd,v[i]);
		modu(t0,mcd);
		Long res = mcd - t0;
		modu(res,mcd);
		printf("Case #%d: ",tt+1);
		out(res);
	}
	return 0;
}