#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <string.h>
#include <algorithm>
#define BASE 10000000
#define SIZE 20
using namespace std;
typedef long long INT;

struct BIG
{
	INT a[SIZE];
	int len;
}f[1000],g[1000],GCD;

void mul(BIG &a,BIG &b,BIG &c)
{
	int i,j;
	memset(c.a,0,sizeof(c.a));
	for(i = 0;i < a.len;i++)
		for(j = 0;j < b.len;j++)
			c.a[i+j] += a.a[i]*b.a[j];
	for(i = 0;i < a.len + b.len + 3;i++)
		c.a[i+1] += c.a[i]/BASE,c.a[i] %= BASE;
	for(i = a.len + b.len + 3;i >= 0 && c.a[i] == 0;i--);
	c.len = i + 1;
}

void add(BIG &a,BIG &b,BIG &c)
{
	int i,ml = a.len > b.len ? a.len : b.len;
	memset(c.a,0,sizeof(c.a));
	for(i = 0;i < ml;i++)
		c.a[i] = a.a[i] + b.a[i];
	for(i = 0;i < ml;i++)
		c.a[i+1] += c.a[i]/BASE,c.a[i] %= BASE;
	for(i = ml + 1;i >= 0 && c.a[i] == 0;i--);
	c.len = i + 1;
}

void sub(BIG &a,BIG &b,BIG &c)
{
	int i;
	memset(c.a,0,sizeof(c));
	for(i = 0;i < a.len;i++)
		c.a[i] = a.a[i] - b.a[i];
	for(i = 0;i < a.len;i++)
	{
		if(c.a[i] < 0)
			c.a[i+1]--,c.a[i] += BASE;
	}
	for(i = a.len;i >= 0 && c.a[i] == 0;i--);
	c.len = i + 1;
}

void shift(BIG &a)
{
	int i;
	for(i = a.len - 1;i >= 0;i--)
	{
		if(i)
			a.a[i-1] += (a.a[i]&1)*BASE;
		a.a[i] >>= 1;
	}
}

void f1(BIG &a)
{
	a.a[0]++;
	for(int i = 0;i < a.len;i++)
	{
		if(a.a[i] >= BASE)
			a.a[i+1] ++,a.a[i] -= BASE;
	}
	if(a.a[a.len])
		a.len++;
}

void f2(BIG &a)
{
	a.a[0]--;
	for(int i = 0;i < a.len;i++)
	{
		if(a.a[i] < 0)
			a.a[i+1] --,a.a[i] += BASE;
	}
	int i;
	for(i = a.len - 1;i >= 0 && a.a[i] == 0;i--);
	a.len = i + 1;
}

int cmp(BIG &a,BIG &b)
{
	if(a.len != b.len)
	{
		if(a.len > b.len)
			return 1;
		return -1;
	}
	for(int i = a.len - 1;i >= 0;i--)
	{
		if(a.a[i] != b.a[i])
		{
			if(a.a[i] > b.a[i])
				return 1;
			return -1;
		}
	}
	return 0;
}

void mod(BIG &a,BIG &b,BIG &c)
{
	BIG low,high,mid,t,final;
	memset(low.a,0,sizeof(low.a));
	low.len = 0;
	memset(high.a,0,sizeof(high.a));
	high.a[9] = 1,
	high.len = 10;
	while(cmp(high,low) >= 0)
	{
		add(low,high,mid);
		shift(mid);
		mul(b,mid,t);
		int tmp = cmp(t,a);
		if(tmp <= 0)
			final = mid,low = mid,f1(low);
		else
			high = mid,f2(high);
	}
	mul(b,final,t);
	sub(a,t,c);
}

bool zero(BIG &a)
{
	return a.len == 0;
}

void gcd(BIG &a,BIG &b,BIG &c)
{
	if(zero(b))
	{
		c = a;
		return;
	}
	BIG t;
	mod(a,b,t);
	gcd(b,t,c);
}

void per(BIG &a,char *s)
{
	int i,len = strlen(s);
	for(i = 0;i <= len - 1 - i;i++)
		swap(s[i],s[len-1-i]);
	memset(a.a,0,sizeof(a.a));
	a.len = 0;
	for(i = 0;i < len;i += 7)
	{
		int j;
		if(i + 6 < len)
			j = i + 6;
		else
			j = len - 1;
		for(;j >= i;j--)
			a.a[a.len] = a.a[a.len]*10 + (INT)(s[j] - '0');
		a.len++;
	}
}

void print(BIG &a)
{
	if(a.len == 0)
	{
		printf("0\n");
		return;
	}
	printf("%lld",a.a[a.len-1]);
	for(int i = a.len - 2;i >= 0;i--)
		printf("%07lld",a.a[i]);
	printf("\n");
}

bool cmpp(BIG a,BIG b)
{
	if(a.len != b.len)
		return a.len > b.len;
	for(int i = a.len - 1;i >= 0;i--)
	{
		if(a.a[i] != b.a[i])
			return a.a[i] > b.a[i];
	}
	return false;
}

int main()
{
	int T,N,i;
	char s[100];
	//freopen("input","r",stdin);
	//freopen("B.in","r",stdin);
	//freopen("B.out","w",stdout);
	scanf("%d",&T);
	for(int Case = 1;Case <= T;Case++)
	{
		scanf("%d",&N);
		for(i = 0;i < N;i++)
		{
			scanf("%s",s);
			per(f[i],s);
		}
		sort(f,f + N,cmpp);
		for(i = 0;i < N - 1;i++)
			sub(f[i],f[i+1],g[i]);
		GCD = g[0];
		for(i = 1;i < N - 1;i++)
			gcd(g[i],GCD,GCD);
		BIG ans;
		mod(f[0],GCD,ans);
		printf("Case #%d: ",Case);
		if(zero(ans))
		{
			printf("0\n");
			continue;
		}
		BIG t;
		sub(GCD,ans,t);
		print(t);
	}
	return 0;
}



