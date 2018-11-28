//google code jam 2010 qualification round 2010 b

#include <stdio.h>
#include <string.h>

const long m=10;
const int mlen=1;
const int maxlen=100;
const int maxn=1005;

typedef struct{
	long val[maxlen];
	int len;
}big2;

big2 t[maxn],d[maxn], dd, tmp, ans;

int big2cp(big2 &dest, big2 source)
{
	int i;

	dest.len=source.len;
	for (i=0; i<=source.len; i++)
		dest.val[i]=source.val[i];
	return 0;
}

int mod(big2 a, big2 b, big2 &c)
{
	int i,j,t,t1;
	bool flag;

	big2cp(c, a);
	for (i=a.len-b.len; i>=0;)
	{
		flag=true;
		if (c.len<i+b.len) flag=false;
		else if (c.len==i+b.len)
		{
			for (j=b.len; c.val[i+j]==b.val[j] && j>0; j--);			
			if (j>0 && c.val[i+j]<b.val[j]) flag=false;
		}
		if (flag)
		{
			t=0;
			for (j=1; j<=b.len; j++)
			{
				t1=c.val[i+j]-b.val[j]-t;
				t=0;
				while (t1<0)
				{
					t1+=m;
					t++;
				}
				while (t1>=m)
				{
					t1-=m;
					t--;
				}
				c.val[i+j]=t1%m;
			}
			for ( ; t!=0; j++)
			{
				t1=c.val[i+j]-t;
				t=0;
				while (t1<0)
				{
					t1+=m;
					t++;
				}
				c.val[i+j]=t1;
			}
			while (c.len>0 && c.val[c.len]==0) c.len--;
		}else i--;
	}

	return 0;
}

bool big2zero(big2 a)
{
	if (a.len==0 || (a.len==1 && a.val[1]==0)) return true;
	else return false;
}

int gcd(big2 a, big2 b, big2 &c)
{
	big2 t1, t2;
	big2cp(t1, a);
	big2cp(t2, b);
	while (big2zero(t2)==false)
	{
		mod(t1, t2, c);
		big2cp(t1, t2);
		big2cp(t2, c);
	}
	big2cp(c, t1);
	return 0;
}

int absminus(big2 a, big2 b, big2 &c)
{
	int i;
	long t=0, t1;

	for (i=b.len+1; i<=a.len; i++)
		b.val[i]=0;
	for (i=1; i<=a.len; i++)
	{
		t1=a.val[i]-b.val[i]-t;
		t=0;
		while (t1<0)
		{
			t1+=m;
			t++;
		}
		while (t1>=m)
		{
			t1-=m;
			t--;
		}
		c.val[i]=t1;
	}
	c.len=a.len;
	while (c.len>0 && c.val[c.len]==0) c.len--;
	return 0;
}

int compare(big2 a, big2 b)
{
	int i;

	if (a.len>b.len) return 1;
	else if (a.len<b.len) return -1;

	i=a.len;
	while (i>0 && a.val[i]==b.val[i]) i--;
	return a.val[i]-b.val[i];
}

int minus(big2 a, big2 b, big2 &c)
{
	if (compare(a,b)<0) absminus(b, a, c);
	else absminus(a, b, c);

	return 0;
}

int big2in(char* str, big2 &a)
{
	int i,j,k,len;
	long p;

	len=strlen(str);

	k=0;
	j=0;
	a.val[0]=0;
	for (i=len-1; i>=0; i--)
	{
		if (j%mlen==0)
		{
			k++;
			a.val[k]=0;
			j=0;
			p=1;
		}
		a.val[k]+=p*(str[i]-'0');
		p*=10;
		j++;
	}
	a.len=k;
	return 0;
}

int big2out(big2 &a)
{
	int i;

	if (a.len==0) printf("0");
	else
	{
		printf("%ld", a.val[a.len]);
		for (i=a.len-1; i>0; i--)
			printf("%01ld", a.val[i]);
	}
	return 0;
}

int main()
{
	int c,cas,i,j, n;
	char str[1000];

	scanf("%d", &c);
	for (cas=1; cas<=c; cas++)
	{
		scanf("%d", &n);
		for (i=1; i<=n; i++)
		{
			scanf("%s", &str);
			big2in(str, t[i]);
		}
		for (i=1; i<n; i++)
			minus(t[i], t[i+1], d[i]);

		big2cp(dd, d[1]);
		for (i=2; i<n; i++)
		{
			big2cp(tmp, dd);
			gcd(tmp, d[i], dd);
		}
		mod(t[1], dd, tmp);
		minus(dd, tmp, ans);
		big2cp(tmp, ans);
		mod(tmp, dd, ans);
		printf("Case #%d: ", cas);
		big2out(ans);
		printf("\n");
	}

	return 0;
}