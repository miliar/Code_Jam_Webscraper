#include <stdio.h>
#include <complex>
#include <vector>
#include <math.h>
using namespace std;

#define L 55
#define B 10000
#define LB 4
#define PI 3.1415926535897932384626433832795
#define N 1005
class Long
{
public:
     int m[L], l;
     int &operator [](int i) { return m[i]; }
     Long &operator =(int x);
     Long &operator =(char *s);
     int inp();
     void out();
};
void fft(vector <complex <double> > &y)
{
     int i, n=y.size();
     complex <double> z(1, 0), z0(cos(2*PI/n), sin(2*PI/n));
     if(n==1) return;
     vector <complex <double> > a(n/2), b(n/2);
     for(i=0; i<n/2; a[i]=y[2*i], b[i]=y[2*i+1], i++);
     for(fft(a), fft(b), i=0; i<n/2; y[i]=a[i]+z*b[i], y[i+n/2]=a[i]-z*b[i], z=z*z0, i++);
}
void rfft(vector <complex <double> > &y)
{
     int i, n=y.size();
     complex <double> z(1, 0), z0(cos(2*PI/n), -sin(2*PI/n));
     if(n==1) return;
     vector <complex <double> > a(n/2), b(n/2);
     for(i=0; i<n/2; a[i]=y[2*i], b[i]=y[2*i+1], i++);
     for(rfft(a), rfft(b), i=0; i<n/2; y[i]=a[i]+z*b[i], y[i+n/2]=a[i]-z*b[i], z=z*z0, i++);
} 
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
Long &Long::operator =(char *s)
{
     int i, j, n;
     for(n=0; s[n]>='0' && s[n]<='9'; n++);
     for(l=(n+LB-1)/LB, i=0; i<l; i++)
          for(m[i]=0, j=LB-1; j>=0; j--)
               if(n-(i*LB+j)-1>=0) m[i]=m[i]*10+s[n-(i*LB+j)-1]-'0';
     return *this;
}
Long &Long::operator =(int x)
{
     for(l=1, m[l-1]=x%B, x/=B; x; m[l++]=x%B, x/=B);
     return *this;
}
bool operator ==(Long x, Long y)
{
     int i;
     if(x.l!=y.l) return 0;
     for(i=0; i<x.l && x[i]==y[i]; i++);
     return i==x.l;
}
bool operator <(Long x, Long y)
{
     int i;
     if(x.l!=y.l) return (x.l<y.l);
     for(i=x.l-1; i>=0 && x[i]==y[i]; i--);
     if(i>=0) return (x[i]<y[i]);
     return 0;
}
bool operator !=(Long x, Long y) { return !(x==y); }
bool operator <=(Long x, Long y) { return (x<y || x==y); }
bool operator >(Long x, Long y) { return !(x<=y); }
bool operator >=(Long x, Long y) { return !(x<y); }
Long operator <<(Long x, int y)
{
     int i;
     Long z;
     for(z.l=x.l+y, i=0; i<z.l; z[i]=(i>y)?x[i-y]:0, i--);
     for(; z.l>1 && !z[z.l-1]; z.l--);
     return z;
}
Long operator >>(Long x, int y)
{
     int i;
     Long z;
     for(z[0]=0, z.l=x.l-y, i=0; i<z.l; z[i]=x[i+y], i++);
     z.l=(z.l>0)?z.l:1;
     return z;
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
__int64 fl(double x) { return x<0?x-0.5:x+0.5; }
Long operator &(Long x, Long y)
{
     int i, n;
     __int64 h, t;
     Long z;
     for(n=1; n<x.l+y.l; n*=2);
     vector <complex <double> > fx(n), fy(n);
     for(i=0; i<n; fx[i]=0, fy[i]=0, i++);
     for(i=0; i<x.l; fx[i]=x[i], i++);
     for(i=0; i<y.l; fy[i]=y[i], i++);
     for(fft(fx), fft(fy), i=0; i<n; fx[i]*=fy[i], i++);
     for(rfft(fx), z.l=x.l+y.l, h=0, i=0; i<z.l; h/=B, i++)
     {
          t=fl(fx[i].real()/(double)n);
          h+=t;
          z[i]=h%B;
     }
     for(; z.l>1 && !z[z.l-1]; z.l--);
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
Long operator /(Long x, Long y)
{
     int i, j;
     Long z, a, b;
     for(j=0, i=0; i<y.l-1; j|=(y[i]>0), i++);
     for(j+=y[y.l-1], b=x, a=1, z=0; (a.l>1 || a[0]); a=(b>>(y.l-1))/j, z=z+a, b=b-a*y);
     a=(y<=b);
     z=z+a;
     return z;
}



Long a[N], b, c, d;

Long gcd(Long a, Long b) {
	if (b.l == 1 && b[0] == 0) {
		return a;
	}
	return gcd(b, a - ((a/b)*b));
}

int i, j, k, n, m, x, y, z, t, tt, T;

int main() {
	freopen("big.in", "r", stdin); freopen("big.out", "w", stdout);
	scanf("%d", &T);
	for (tt = 1; tt <= T; tt ++) {
		scanf("%d", &n);
		b = "999999999999999999999999999999999999999999999999999999999999999999999999999999";
		x = 0;
		for (i = 0; i < n; i ++) {
			a[i].inp();
			if (a[i] < b) {
				b = a[i];
				x = i;
			}
		}
		c = a[n-1];
		a[n-1] = a[x];
		a[x] = c;
		for (i = 0; i < n - 1; i ++) {
			a[i] = a[i] - a[n-1];
		}
		b = a[0];
		for (i = 1; i < n - 1; i ++) {
			b = gcd(b, a[i]);
		}
		c = a[n-1] - (a[n-1] / b)*b;
		if (c.l == 1 && c[0] == 0) {
			c = c;
		} else {
			c = b - c;
		}

		printf("Case #%d: ", tt);
		c.out();
		printf("\n");
	}
	return 0;
}



