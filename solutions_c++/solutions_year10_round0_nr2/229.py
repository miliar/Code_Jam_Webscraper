#include<iostream>
#include<algorithm>
#include<string>
using namespace std;
const int maxn=1000+10;
const int maxl=50+10;
typedef int num[maxl];
int n,p[maxn];
num ans,x,x0,d[maxn],c;
string s;
void init()
{
	cin >>n;
	memset(d,0,sizeof(d));
	for (int i=0;i<n;i++)
	{
		cin >>s;
		d[i][0]=s.size();
		for (int j=1;j<=d[i][0];j++)
			d[i][j]=s[d[i][0]-j]-'0';
	}
}
bool comp(int *a,int *b)
{
	if (a[0]!=b[0])
		return a[0]<b[0];
	for (int i=a[0];i;i--)
		if (a[i]!=b[i])
			return a[i]<b[i];
	return false;
}
bool comp3(num &a,num &b)
{
	if (a[0]!=b[0])
		return a[0]<b[0];
	for (int i=a[0];i;i--)
		if (a[i]!=b[i])
			return a[i]<b[i];
	return true;
}
bool comp2(int i,int j)
{
	return comp(d[i],d[j]);
}
void mul(num &a)
{
	int d=0;
	for (int i=1;i<=a[0];i++)
	{
		a[i]=(a[i]<<1)+d;
		if (a[i]>9)
		{
			a[i]-=10;
			d=1;
		}
		else
			d=0;
	}
	if (d)
		a[++a[0]]=1;
}
void sub(int *a,int *b)
{
	for (int i=1;i<=a[0];i++)
	{
		a[i]-=b[i];
		if (a[i]<0)
		{
			a[i]+=10;
			a[i+1]--;
		}
	}
	while (a[0] && !a[a[0]])
		a[0]--;
}
void div2(int *a)
{
	int x=0;
	for (int i=a[0];i;i--)
	{
		x=x*10+a[i];
		a[i]=x>>1;
		x=x&1;
	}
	while (a[0] && !a[a[0]])
		a[0]--;
}
void calcmod(num &a,num &b)
{
	while (comp3(b,a))
	{
		int tmp=a[0]-b[0]-1;
		if (tmp<0)
			tmp=0;
		memset(c,0,sizeof(c));
		c[0]=b[0]+tmp;
		for (int i=tmp+1;i<maxl;i++)
			c[i]=b[i-tmp];
		while (comp3(c,a))
			sub(a,c);
	}
}
void gcd(num a,num b,int t)
{
	if (!a[0])
	{
		for (int i=0;i<maxl;i++)
			x[i]=b[i];
		for (int i=0;i<t;i++)
			mul(x);
		return;
	}
	if (!b[0])
	{
		for (int i=0;i<maxl;i++)
			x[i]=a[i];
		for (int i=0;i<t;i++)
			mul(x);
		return;
	}
	if (!(a[1]&1) && !(b[1]&1))
	{
		div2(a);
		div2(b);
		gcd(a,b,t+1);
		return;
	}
	if (!(a[1]&1))
	{
		div2(a);
		gcd(a,b,t);
		return;
	}
	if (!(b[1]&1))
	{
		div2(b);
		gcd(a,b,t);
		return;
	}
	if (comp(b,a))
		gcd(b,a,t);
	else
	{
		sub(b,a);
		gcd(a,b,t);
	}
}
void solve()
{
	for (int i=0;i<n;i++)
		p[i]=i;
	sort(p,p+n,comp2);
	memset(x,0,sizeof(x));
	for (int i=n-1;i;i--)
	{
		sub(d[p[i]],d[p[i-1]]);
		if (!d[p[i]][0])
			continue;
		if (!x[0])
		{
			for (int j=0;j<maxl;j++)
				x[j]=d[p[i]][j];
			continue;
		} 
		for (int j=0;j<maxl;j++)
			x0[j]=x[j];
		gcd(x0,d[p[i]],0);
	}
	for (int i=0;i<maxl;i++)
		ans[i]=x[i];
	calcmod(d[p[0]],x);
	if (!d[p[0]][0])
		ans[0]=0;
	else
		sub(ans,d[p[0]]);
}
void out(int t)
{
	cout <<"Case #"<<t<<": ";
	if (!ans[0])
		cout <<0;
	for (int i=ans[0];i;i--)
		cout <<ans[i];
	cout <<endl;
}
int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int t;
	cin >>t;
	for (int i=1;i<=t;i++)
	{
		init();
		solve();
		out(i);
	}
	return 0;
}
