#include <stdio.h>
#include <math.h>
#include <string.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#pragma comment(linker, "/STACK:16777216")
using namespace std;

#define bit(n) (1<<(n))
#define inf 1000000000
#define eps 1e-9
#define pi 3.1415926535897932385
#define pb push_back
#define sz size()
#define mp make_pair
#define cl clear()
#define all(a) a.begin(),a.end()
#define fill(ar,val) memset(ar,val,sizeof ar)
#define MIN(a,b) if(a>(b)) a=(b)
#define MAX(a,b) if(a<(b)) a=(b)
#define sqr(x) ((x)*(x))
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))

typedef vector<int> VI;
typedef pair<int,int> PII;
//typedef long long LL;

#define p_len 4
const int p=10000;
#define NN 66/p_len

struct num
{
	int len;
	int it[NN];
	num(int n=0)
	{
		for(len=0;n>0;n/=p) it[len++]=n%p;
	}
};

num operator+(const num &a,const num &b)
{
	num s;
	int i,div=0;
	for(i=0;i<a.len || i<b.len;i++)
	{
		if(i<a.len) div+=a.it[i];
		if(i<b.len) div+=b.it[i];
		s.it[i]=div%p;
	    div/=p;
	}
	if(div>0) s.it[i++]=div;
	s.len=i;
	return s;
}

void operator+=(num &a,const num &b)
{
	int i,div=0;
	for(i=0;i<a.len || i<b.len;i++)
	{
		if(i<a.len) div+=a.it[i];
		if(i<b.len) div+=b.it[i];
		a.it[i]=div%p;
	    div/=p;
	}
	if(div>0) a.it[i++]=div;
	a.len=i;
}

void operator++(num &a)
{
	int i;
	for(i=0;i<a.len && a.it[i]==p-1;i++) a.it[i]=0;
	if(i==a.len) a.it[a.len++]=1; else a.it[i]++;
}

num operator-(const num &a,const num &b)
{
	num s;
	int i,div=0;
	for(i=0;i<a.len;i++)
	{
		div+=a.it[i]-(i<b.len?b.it[i]:0)+2*p;
		s.it[i]=div%p;
		div=div/p-2;
	}
	for(;i-->=0 && s.it[i]==0;);
	s.len=i+1;
	return s;
}

void operator-=(num &a,const num &b)
{
	int i,div=0;
	for(i=0;i<a.len;i++)
	{
		div+=a.it[i]-(i<b.len?b.it[i]:0)+2*p;
		a.it[i]=div%p;
		div=div/p-2;
	}
	for(;i-->=0 && a.it[i]==0;);
	a.len=i+1;
}


void operator--(num &a)
{
	int i;
	for(i=0;i<a.len && a.it[i]==0;i++) a.it[i]=p-1;
	a.it[i]--;
	if(a.it[a.len-1]==0) a.len--;
}

num operator*(num &a,num &b)
{
	num prod(0);
	memset(prod.it,0,sizeof prod.it);
	if(b.len==0 || a.len==0) return prod;
	int i,j,div;
	for(i=0;i<a.len;i++)
	{
		if(a.it[i]>0)
		{
			div=0;
			for(j=0;j<b.len;j++)
			{
				div+=prod.it[i+j]+a.it[i]*b.it[j];
				prod.it[i+j]=div%p;
				div/=p;
			}
			if(div>0) prod.it[i+j]=div;
		}
	}
	prod.len=a.len+b.len;
	if(prod.it[prod.len-1]==0) prod.len--;
	return prod;
}

num pow(num &a,int n)
{
	num p(1);
	for(;n>0;n/=2)
	{
		if(n%2>0) p=p*a;
		if(n/2>0) a=a*a;
	}
	return p;
}

num operator*(int b,const num &a)
{
	num prod(0);
	if(b==0) return prod;
	int i,div=0;
	for(i=0;i<a.len;i++)
	{
		div+=a.it[i]*b;
		prod.it[i]=div%p;
		div/=p;
	}
	for(;div>0;div/=p) prod.it[i++]=div%p;
	prod.len=i;
	return prod;
}

void operator*=(num &a,int b)
{
	if(b==0) a.len=0; else
	{
		int i,div=0;
		for(i=0;i<a.len;i++)
		{
			div+=a.it[i]*b;
			a.it[i]=div%p;
			div/=p;
		}
		for(;div>0;div/=p) a.it[i++]=div%p;
		a.len=i;
	}
}

bool operator==(const num &a,const num &b)
{
	if(a.len!=b.len) return false;
	int i;
	for(i=a.len-1;i>=0 && a.it[i]==b.it[i];i--);
	return (i<0);
}

bool operator!=(const num &a,const num &b)
{
	if(a.len!=b.len) return true;
	int i;
	for(i=a.len-1;i>=0 && a.it[i]==b.it[i];i--);
	return (i>=0);
}

bool operator<(const num &a,const num &b)
{
	if(a.len!=b.len) return (a.len<b.len);
	int i;
	for(i=a.len-1;i>=0 && a.it[i]==b.it[i];i--);
	return (i>=0 && a.it[i]<b.it[i]);
}

bool operator<=(const num &a,const num &b)
{
	if(a.len!=b.len) return (a.len<b.len);
	int i;
	for(i=a.len-1;i>=0 && a.it[i]==b.it[i];i--);
	return (i<0 || a.it[i]<b.it[i]);
}

bool operator>(const num &a,const num &b)
{
	if(a.len!=b.len) return (a.len>b.len);
	int i;
	for(i=a.len-1;i>=0 && a.it[i]==b.it[i];i--);
	return (i>=0 && a.it[i]>b.it[i]);
}

bool operator>=(const num &a,const num &b)
{
	if(a.len!=b.len) return (a.len>b.len);
	int i;
	for(i=a.len-1;i>=0 && a.it[i]==b.it[i];i--);
	return (i<0 || a.it[i]>b.it[i]);
}


num operator/(const num &a,int q)
{
	num b;
	int c=0,i;
	for(i=a.len-1;i>=0;i--)
	{
		c=p*c+a.it[i];
		b.it[i]=c/q;
		c%=q;
	}
	for(i=a.len-1;i>=0 && b.it[i]==0;i--);
	b.len=i+1;
	return b;
}

void operator/=(num &a,int q)
{
	int c=0,i;
	for(i=a.len-1;i>=0;i--)
	{
		c=p*c+a.it[i];
		a.it[i]=c/q;
		c%=q;
	}
	for(i=a.len-1;i>=0 && a.it[i]==0;i--);
	a.len=i+1;
}


num operator/(num &a,num &b)
{
	num s,w;
	int i,j,v,vv=0,m=b.len;
	s.len=0;
	for(i=0;i<=m;i++) s.it[i]=0;
	if(b.it[m-1]<p/2)
	{
		vv=p/(b.it[m-1]+1);
		a*=vv;b*=vv;
	}
	v=b.it[m-1];
	for(i=a.len-1;i>=0;i--)
	{
		for(j=s.len;j>0;j--) s.it[j]=s.it[j-1];
		s.it[0]=a.it[i];
		for(j=s.len;j>=0 && s.it[j]==0;j--);
		s.len=j+1;
		int q=(p*s.it[m]+s.it[m-1])/v;
		if(q>=p) q=p-1;
		if(q*b>s){q--;if(q*b>s)q--;}
		w.it[i]=q;
		s-=q*b;
	}
	if(vv)
	{
		a/=vv;b/=vv;s/=vv;
	}
	for(i=a.len-1;i>=0 && w.it[i]==0;i--);
	w.len=i+1;
	return w;
}

num operator%(num &a,num &b)
{
	num s,w;
	int i,j,v,vv=0,m=b.len;
	s.len=0;
	for(i=0;i<=m;i++) s.it[i]=0;
	if(b.it[m-1]<p/2)
	{
		vv=p/(b.it[m-1]+1);
		a*=vv;b*=vv;
	}
	v=b.it[m-1];
	for(i=a.len-1;i>=0;i--)
	{
		for(j=s.len;j>0;j--) s.it[j]=s.it[j-1];
		s.it[0]=a.it[i];
		for(j=s.len;j>=0 && s.it[j]==0;j--);
		s.len=j+1;
		int q=(p*s.it[m]+s.it[m-1])/v;
		if(q>=p) q=p-1;
		if(q*b>s){q--;if(q*b>s)q--;}
		w.it[i]=q;
		s-=q*b;
	}
	if(vv)
	{
		a/=vv;b/=vv;s/=vv;
	}
	for(i=a.len-1;i>=0 && w.it[i]==0;i--);
	w.len=i+1;
	return s;
}

void divide(num &a,num &b,num &w,num &s)//a=b*w+s
{
	int i,j,v,vv=0,m=b.len;
	s.len=0;
	for(i=0;i<=m;i++) s.it[i]=0;
	if(b.it[m-1]<p/2)
	{
		vv=p/(b.it[m-1]+1);
		a*=vv;b*=vv;
	}
	v=b.it[m-1];
	for(i=a.len-1;i>=0;i--)
	{
		for(j=s.len;j>0;j--) s.it[j]=s.it[j-1];
		s.it[0]=a.it[i];
		for(j=s.len;j>=0 && s.it[j]==0;j--);
		s.len=j+1;
		int q=(p*s.it[m]+s.it[m-1])/v;
		if(q>=p) q=p-1;
		if(q*b>s){q--;if(q*b>s)q--;}
		w.it[i]=q;
		s-=q*b;
	}
	if(vv)
	{
		a/=vv;b/=vv;s/=vv;
	}
	for(i=a.len-1;i>=0 && w.it[i]==0;i--);
	w.len=i+1;
}

int operator%(num &a,int b)
{
	int i,s=0;
	for(i=a.len-1;i>=0;i--) s=(p*s+a.it[i])%b;
	return s;
}

void print(num &a)
{
	if(a.len==0) printf("0"); else
	{
		long i=a.len-1;
		printf("%d",a.it[i]);
		char s[10];
		sprintf(s,"%%0%dd",p_len);
		for(i--;i>=0;i--) printf(s,a.it[i]);
	}
	printf("\n");
}

bool read(num &a)
{
	char w[NN*p_len];
	if(scanf("%s",w)==-1) return false;
	int i,n=strlen(w),m=0,p=1;
	a.len=0;
	for(i=0;i<n;i++)
	{
		m+=p*(w[n-i-1]-'0');p*=10;
		if((i+1)%p_len==0)
		{
			a.it[a.len++]=m;
			m=0;p=1;
		}
	}
	if(m>0) a.it[a.len++]=m;
	return true;
}

num gcd(num a,num b)
{
	num c;
	while(b.len>0)c=a%b,a=b,b=c;
	return a;
}

#define N 1111
num a[N];

int main()
{
	freopen("B2.in","r",stdin);
	freopen("B2.out","w",stdout);
	int T,t=0;
	for(scanf("%d",&T);T--;)
	{
		int n,i;
		scanf("%d",&n);
		for(i=0;i<n;i++) read(a[i]);
		num d(0);
		for(i=1;i<n;i++)
			if(a[0]>a[i])
				d=gcd(d,a[0]-a[i]);
			else
				d=gcd(d,a[i]-a[0]);
		num y=d-a[0]%d;
		if(y==d) y=num(0);
		printf("Case #%d: ",++t);
		print(y);
	}
	return 0;
}
