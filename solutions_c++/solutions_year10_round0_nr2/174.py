#include <cstdio>
#include <cstring>
#include <cassert>
#pragma comment (linker,"/STACK:10000000")
using namespace std;
const int d=15;
const int base=10000;
struct tlong {
	int n;
	int a[d];
	tlong (int d=0) {
		memset(a,0,sizeof(a));
		n=0;
		while (d>0) {
			a[n++]=d%base;
			d/=base;
		}
	}
};
const int c=1024;
tlong a[c];
int ii,t,n;
tlong m,p,tp,ans;
char temp[100];
void read(tlong &a) {
	a=tlong(0);
	scanf("%s",temp);
	int ls=strlen(temp);
	int i,j;
	for (i=0; i<ls; ++i) {
		for (j=a.n; j>=1; --j) a.a[j]=(a.a[j]*10+a.a[j-1]*10/base)%base;
		a.a[0]=a.a[0]*10%base;
		a.a[0]+=temp[i]-'0';
		if (a.a[a.n]>0) ++a.n;
	}
}
bool operator < (const tlong &a, const tlong &b) {
	if (a.n!=b.n) return a.n<b.n;
	int i;
	for (i=a.n-1; i>=0; --i) if (a.a[i]!=b.a[i]) return a.a[i]<b.a[i];
	return 0;
}
bool operator == (const tlong &a, const tlong &b) {
	if (a.n!=b.n) return 0;
	int i;
	for (i=a.n-1; i>=0; --i) if (a.a[i]!=b.a[i]) return 0;
	return 1;
}
void sub(tlong &a, const tlong &b, int k) {
	int i,j;
	for (i=k; i<a.n && i<b.n+k; ++i) {
		a.a[i]-=b.a[i-k];
		j=i;
		while (a.a[j]<0) {
			a.a[j]+=base;
			j++;
			a.a[j]--;
		}
	}
	while (a.n>0 && a.a[a.n-1]==0) --a.n;
}
tlong operator - (const tlong &a, const tlong &b) {
	tlong c=a;
	sub(c,b,0);
	return c;
}
tlong operator * (const tlong &a, const tlong &b) {
	tlong c(0);
	int i,j;
	for (i=0; i<a.n; ++i)
		for (j=0; j<b.n; ++j) {
			c.a[i+j+1]+=(c.a[i+j]+a.a[i]*b.a[j])/base;
			c.a[i+j]=(c.a[i+j]+a.a[i]*b.a[j])%base;
		}
	c.n=a.n+b.n+1;
	while (c.n>0 && c.a[c.n-1]==0) --c.n;
	return c;
}
bool ls (const tlong &a, const tlong &b, int k) {
	int i;
	if (a.n!=b.n+k) return a.n<b.n+k;
	for (i=a.n-1; i>=k; --i) if (a.a[i]!=b.a[i-k]) return a.a[i]<b.a[i-k];
	return 0;
}
tlong operator % (const tlong &a, const tlong &b) {
	int i,k,q;
	int lf,rg,md;
	tlong c=a;
	tlong tmp;
	for (i=c.n-1; i>=b.n-1; --i) {
		lf=0;
		rg=base;
		while (lf<rg-1) {
			md=(lf+rg)>>1;
			tmp=b*tlong(md);
			if (ls(c,tmp,i-b.n+1)) rg=md; else lf=md;
		}
		tmp=b*lf;
		sub(c,tmp,i-b.n+1);
	}
	while (c.n>0 && c.a[c.n-1]==0) --c.n;
	return c;
}
tlong gcd(const tlong &a, const tlong &b) {
	if (b==tlong(0)) return a; else return gcd(b,a%b);
}
void write (const tlong &a) {
	int i;
	if (a.n==0) printf("0"); else {
		printf("%d",a.a[a.n-1]);
		for (i=a.n-2; i>=0; --i) printf("%04d",a.a[i]);
	}
	printf("\n");
}
int main() {
	int i,j;
	scanf("%d",&t);
	for (ii=1; ii<=t; ++ii) {
		printf("Case #%d: ",ii);
		scanf("%d",&n);
		for (i=1; i<=n; ++i) read(a[i]);
		m=0;
		for (i=1; i<=n; ++i)
			for (j=i+1; j<=n; ++j)
				if (a[j]<a[i]) m=gcd(m,a[i]-a[j]); else m=gcd(m,a[j]-a[i]);
		p=a[1]%m;
		for (i=2; i<=n; ++i) {
			tp=a[i]%m;
			assert(p==tp);
		}
		ans=(m-p)%m;
		write(ans);
	}
	return 0;
}