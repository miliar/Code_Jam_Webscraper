#include <iostream>
#include <algorithm>
#include <string.h>
using namespace std;
int cmp(int a[100],int b[100])
{
	int i;
	if (a[0]>b[0])return 1;else if (a[0]<b[0])return -1;
	for (i=a[0];i;i--)
		if (a[i]>b[i])return 1;else if (a[i]<b[i])return -1;
	return 0;
}
void jian(int a[100],int b[100])
{
	int i,k;
	if (cmp(a,b)==-1)
	{
		for (i=60;i>=0;i--)
		{
			k=a[i];a[i]=b[i];b[i]=k;
		}
	}

	for (i=1;i<=a[0];i++)
	{
		a[i]-=b[i];
		if (a[i]<0){a[i]+=10;a[i+1]--;}
	}
	i=a[0];
	while (a[i]==0&&i!=1)i--;
	a[0]=i;
}
void mod(int a[100],int b[100],int d[100])
{
	int c[100],i,k,j,x,y;
	memset(c,0,sizeof(c));
	c[0]=60;
	x=60;y=b[0];
	while (y!=0)
	{
		c[x]=b[y];
		x--;y--;
	}
	while (c[0]!=b[0]-1)
	{
		while (cmp(a,c)>=0)
		{
			jian(a,c);
		}
		for (i=1;i<c[0];i++)
			c[i]=c[i+1];
		c[c[0]]=0;
		c[0]--;
	}
	for (i=60;i>=0;i--)
		d[i]=a[i];
}
void gcd(int a[100],int b[100],int c[100])
{
	int i,k,j,d[100];
	memset(d,0,sizeof(d));
	if (b[0]!=1||b[1]!=0)
	{
		mod(a,b,d);
		gcd(b,d,c);
	}else
	{
		for (i=0;i<60;i++)
			c[i]=a[i];
	}
}
void readin(int a[100])
{
	memset(a,0,sizeof(a));
	char st[100];
	scanf("%s",&st);
	int i,k,j,l=0;
	while (st[l])l++;
	a[0]=l;
	j=l;
	for (i=0;i<l;i++)
	{
		a[j]=st[i]-'0';
		j--;
	}
}
int a[100],b[100],c[100],n,d[100],e[100];
int main()
{

//	freopen("b.in","r",stdin);
//	freopen("B.out","w",stdout);

	int i,k,j,t,tt;
	scanf("%d",&t);
	for (tt=1;tt<=t;tt++)
	{
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(a));
		memset(c,0,sizeof(a));
		memset(d,0,sizeof(a));
		memset(e,0,sizeof(a));

		printf("Case #%d: ",tt);
		scanf("%d",&n);
		
		readin(a);
		readin(b);
		jian(b,a);
		for (i=1;i<n-1;i++)
		{
			readin(c);
			jian(c,a);
			gcd(b,c,d);
			for (j=0;j<=d[0];j++)
				b[j]=d[j];
		}
		
		{
			mod(a,b,c);
			if (c[0]==1&&c[1]==0)printf("0");else
			{
			jian(c,b);
			for (i=c[0];i;i--)printf("%d",c[i]);}
		}
		puts("");
	}

}