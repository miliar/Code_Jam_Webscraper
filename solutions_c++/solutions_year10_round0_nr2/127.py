#include <stdio.h>
#include <algorithm>
using namespace std;
#define L 20
#define B 10000000
#define LB 7
class Long
{
public:
	int m[L], l;
	int &operator [](int i) { return m[i]; }
	Long operator =(int x);
	Long operator =(char *s);
	int inp();
	void out();
};
int Long::inp()
{
	char s[L*LB+10], c;
	c=scanf("%s", s);
	*this=s;
	return c!=EOF;
}
void Long::out()
{
	int i;
	char s[8];
	for(sprintf(s, "%%0%dd", LB), printf("%d", m[l-1]), i=l-2; i>=0; printf(s, m[i]), i--);
}
bool operator <(Long x, Long y)
{
	int i;
	if(x.l!=y.l) return x.l<y.l;
	for(i=x.l-1; i>=0 && x[i]==y[i]; i--);
	return i>=0 && x[i]<y[i];
}
Long Long::operator =(char *s)
{
	int i, j, n;
	for(n=0; s[n]>='0' && s[n]<='9'; n++);
	for(l=(n+LB-1)/LB, i=0; i<l; i++)
		for(m[i]=0, j=0; j<LB; j++)
			if(n-i*LB-LB+j>=0) m[i]=m[i]*10+s[n-i*LB-LB+j]-'0';
	return *this;
}
Long Long::operator =(int x)
{
	for(l=1, m[l-1]=x%B, x/=B; x; m[l++]=x%B, x/=B);
	return *this;
}
Long operator +(Long x, Long y)
{
	int i;
	__int64 h;
	Long z;
	for(h=0, i=0; i<x.l || i<y.l || h; h+=(i<x.l)?x[i]:0, h+=(i<y.l)?y[i]:0, z[i]=h%B, h=(h>=B), i++);
	z.l=i;
	return z;
}
Long operator -(Long x, Long y)
{
	int i;
	__int64 h;
	Long z;
	for(h=0, i=0; i<x.l; h+=x[i], h-=(i<y.l)?y[i]:0, z[i]=(h+B)%B, h=-(h<0), i++);
	for(z.l=i; z.l>1 && !z[z.l-1]; z.l--);
	return z;
}
Long operator *(Long x, int y)
{
	int i;
	__int64 h;
	Long z;
	for(h=0, i=0; i<x.l || h; h+=(i<x.l)?((__int64)x[i]*y):0, z[i]=h%B, h/=B, i++);
	for(z.l=i; z.l>1 && !z[z.l-1]; z.l--);
	return z;
}
Long operator *(Long x, Long y)
{
	int i, j;
	__int64 h;
	Long z;
	for(h=0, z.l=x.l+y.l, i=0; i<z.l; z[i]=h%B, h/=B, i++)
		for(j=0; j<=i && j<x.l; h+=(i-j<y.l)?((__int64)x[j]*y[i-j]):0, j++);
	for(z.l=i; z.l>1 && !z[z.l-1]; z.l--);
	return z;
}
Long operator /(Long x, int y)
{
	int i;
	__int64 h;
	Long z;
	for(h=0, i=x.l-1; i>=0; h=(__int64)h*B+x[i], z[i]=h/y, h%=y, i--);
	for(z.l=x.l; z.l>1 && !z[z.l-1]; z.l--);
	return z;
}
int operator %(Long x, int y)
{
	int i;
	__int64 h;
	for(h=0, i=x.l-1; i>=0; h=(__int64)h*B+x[i], h%=y, i--);
	return h;
}
Long operator /(Long x, Long y)
{
	Long l, c, r, u;
	for(u=1, l=0, r=x; l<r; )
	{
		c=(l+r+u)/2;
		if(x<c*y) r=c-u;
		else l=c;
	}
	return r;
}
Long operator %(Long x, Long y)
{
	return x-(x/y)*y;
}
#define N 1010
Long gcd(Long x, Long y) { return (y.l==1 && y[0]==0)?x:gcd(y, x%y); }
Long m[N], g, r;
int main()
{
	int i, t, ts, n;
	for(scanf("%d", &ts), t=0; t<ts; t++)
	{
		for(scanf("%d", &n), i=0; i<n; m[i].inp(), i++);
		sort(m, m+n);
		for(g=0, i=1; i<n; g=gcd(g, m[i]-m[i-1]), i++);
		r=m[0]%g;
		if(r.l>1 || r[0]) r=g-r;
		printf("Case #%d: ", t+1);
		r.out();
		printf("\n");
	}
	return 0;
}