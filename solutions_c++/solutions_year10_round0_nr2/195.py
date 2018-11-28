#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
char s[150];
struct bint
{
	int k,x[150];
	void scan()
	{
		int i;
		scanf("%s",s);
		k=strlen(s);
		for (i=0;i<k;i++)
			x[k-i-1]=s[i]-48;
	}
	void operator -=(const bint &a)
	{
		int i,temp;
		temp=0;
		for (i=0;i<a.k;i++)
		{
			x[i]-=(a.x[i]+temp);
			if (x[i]<0)
			{
				x[i]+=10;
				temp=1;
			}
			else
				temp=0;
		}
		while (temp==1)
		{
			x[i]--;
			if (x[i]<0)
			{
				x[i]+=10;
				temp=1;
			}
			else
				temp=0;
			i++;
		}
		while (k>0&&x[k-1]==0)
			k--;
	}
	bool iszero()
	{
		return k==0;
	}
	bool d2()
	{
		return x[0]%2==0;
	}
	void div2()
	{
		int i,temp;
		temp=0;
		for (i=k-1;i>=0;i--)
		{
			x[i]+=temp*10;
			temp=x[i]%2;
			x[i]/=2;
		}
		while (k>0&&x[k-1]==0)
			k--;
	}
	void mul2()
	{
		int i,temp;
		temp=0;
		for (i=0;i<k;i++)
		{
			x[i]=x[i]*2+temp;
			if (x[i]>=10)
			{
				x[i]-=10;
				temp=1;
			}
			else
				temp=0;
		}
		if (temp==1)
		{
			x[k]=1;
			k++;
		}
	}
	void pri()
	{
		int i;
		if (k==0)
			printf("0");
		else
		{
			for (i=k-1;i>=0;i--)
				printf("%d",x[i]);
		}
	}
};
bool operator <(const bint &a,const bint &b)
{
	int i;
	if (a.k!=b.k)
		return a.k<b.k;
	for (i=a.k-1;i>=0;i--)
		if (a.x[i]!=b.x[i])
			return a.x[i]<b.x[i];
	return 0;
}
bool operator ==(const bint &a,const bint &b)
{
	return (!(a<b)&&!(b<a));
}
bint gcd(bint a,bint b)
{
	bint temp;
	int s;
	s=0;
	while (1)
	{
		if (a<b)
		{
			temp=b;
			b=a;
			a=temp;
		}
		if (b.iszero())
			break;
		if (a.d2()&&b.d2())
		{
			s++;
			a.div2();
			b.div2();
		}
		else if (a.d2())
			a.div2();
		else if (b.d2())
			b.div2();
		else
			a-=b;
	}
	while (s>0)
	{
		s--;
		a.mul2();
	}
	return a;
}
bint mul(const bint &a,const bint &b)
{
	int i,j;
	bint c;
	memset(c.x,0,sizeof(c.x));
	for (i=0;i<a.k;i++)
		for (j=0;j<b.k;j++)
			c.x[i+j]+=a.x[i]*b.x[j];
	for (i=0;i<130;i++)
	{
		if (c.x[i]>=10)
		{
			c.x[i+1]+=c.x[i]/10;
			c.x[i]%=10;
		}
	}
	c.k=130;
	while (c.k>0&&c.x[c.k-1]==0)
		c.k--;
	return c;
}
bint a[1000],b,temp,c,v;
int main()
{
	int t,tt,n,i,j;
	scanf("%d",&t);
	for (tt=1;tt<=t;tt++)
	{
		scanf("%d",&n);
		for (i=0;i<n;i++)
			a[i].scan();
		sort(a,a+n);
		for (i=n-1;i>0;i--)
			a[i]-=a[i-1];
		b=a[0];
		a[0]=a[n-1];
		n--;
		temp=a[0];
		for (i=1;i<n;i++)
			temp=gcd(temp,a[i]);
		memset(c.x,0,sizeof(c.x));
		for (i=50;i>=0;i--)
		{
			c.k=i+1;
			c.x[i]=1;
			v=mul(temp,c);
			if (b<v)
				c.x[i]=0;
			else
				break;
		}
		for (i=c.k-1;i>=0;i--)
		{
			for (c.x[i]=9;c.x[i]>=0;c.x[i]--)
			{
				v=mul(temp,c);
				if (b<v)
					continue;
				else
					break;
			}
		}
		v=mul(temp,c);
		if (b==v)
			temp.k=0;
		else
		{
			b-=v;
			temp-=b;
		}
		printf("Case #%d: ",tt);
		temp.pri();
		printf("\n");
	}
	return 0;
}