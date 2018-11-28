#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <map>
#include <set>
#include <iterator>
#include <algorithm>
#include <queue>
#include <functional>
#include <sstream>
#include <complex>
#include <ctype.h>
#include <math.h>
#include <stdlib.h>
#include <ctime>
#include <iomanip>
#include <time.h>

using namespace std;

#ifdef ONLINE_JUDGE
void init()
{
}
#else
FILE* inputstream;
FILE* outputstream;
void init()
{
	inputstream = freopen("in.txt", "r", stdin);
	outputstream = freopen("output.txt", "w", stdout);
}
#endif

#define maxsize 100

struct hp
{
	int len;
	int s[maxsize+1];
};

bool operator < (const hp& a, const hp& b)
{
	if (a.len != b.len)
	{
		return a.len < b.len;
	}
	for (int i = a.len; i >= 1; --i)
	{
		if (a.s[i] != b.s[i])
		{
			return a.s[i] < b.s[i];
		}
	}
	return false;
}

void input(hp &a,string str)
{
	int i;
	while(str[0]=='0' && str.size()!=1)
		str.erase(0,1);
	a.len=(int)str.size();
	for(i=1;i<=a.len;++i)
		a.s[i]=str[a.len-i]-48;
	for (i=a.len+1;i<=maxsize;++i)
		a.s[i]=0;
}

void print(const hp &y)
{
	int i;
	for(i=y.len;i>=1;i--)
		printf("%d", y.s[i]);
	printf("\n");
}

void plus(const hp &a,const hp &b,hp &c) //高精度加法
{
	int i,len;
	for(i=1;i<=maxsize;i++) c.s[i]=0;
	if(a.len>b.len) len=a.len;
	else len=b.len;
	for(i=1;i<=len;i++)
	{
		c.s[i]+=a.s[i]+b.s[i];
		if(c.s[i]>=10)
		{
			c.s[i]-=10;
			c.s[i+1]++;
		}
	}
	if(c.s[len+1]>0) len++;
	c.len=len;
}

void subtract(const hp &a,const hp &b,hp &c) //高精度减法
{
	int i,len;
	for(i=1;i<=maxsize;i++) c.s[i]=0;
	if(a.len>b.len) len=a.len;
	else len=b.len;
	for(i=1;i<=len;i++)
	{
		c.s[i]+=a.s[i]-b.s[i];
		if(c.s[i]<0)
		{
			c.s[i]+=10;
			c.s[i+1]--;
		}
	}
	while(len>1&&c.s[len]==0) len--;
	c.len=len;
}

int compare(const hp &a,const hp &b)
{
	int len;
	if(a.len>b.len) len=a.len;
	else len=b.len;
	while(len>0 && a.s[len]==b.s[len]) len--;
	if(len==0) return 0;
	else return a.s[len]-b.s[len];
}

void multiply(const hp &a,int b,hp &c) //高精度*单精度
{
	int i,len;
	for(i=1;i<=maxsize;i++) c.s[i]=0;
	len=a.len;
	for(i=1;i<=len;i++)
	{
		c.s[i]+=a.s[i]*b;
		c.s[i+1]+=c.s[i]/10;
		c.s[i]%=10;
	}
	len++;
	while(c.s[len]>=10)
	{
		c.s[len+1]+=c.s[len]/10;
		c.s[len]%=10;
		len++;
	}
	while(len>1&&c.s[len]==0) len--;
	c.len=len;
}

void multiplyh(const hp &a,const hp &b,hp &c) //高精度*高精度
{
	int i,j,len;
	for(i=1;i<=maxsize;i++) c.s[i]=0;
	for(i=1;i<=a.len;i++)
		for(j=1;j<=b.len;j++)
		{
			c.s[i+j-1]+=a.s[i]*b.s[j];
			c.s[i+j]+=c.s[i+j-1]/10;
			c.s[i+j-1]%=10;
		}
	len=a.len+b.len+1;
	while(len>1&&c.s[len]==0) len--;
	c.len=len;
}

void divide(const hp &a,int b,hp &c,int &d) //高精度/单精度 　{d为余数}
{
	int i,len;
	for(i=1;i<=maxsize;i++) c.s[i]=0;
	len=a.len;
	d=0;
	for(i=len;i>=1;i--)
	{
		d=d*10+a.s[i];
		c.s[i]=d/b;
		d%=b;
	}
	while(len>1&&c.s[len]==0) len--;
	c.len=len;
}

void multiply10(hp &a)     //高精度*10
{
	int i;
	for(i=a.len;i>=1;i--)
		a.s[i+1]=a.s[i];
	a.s[1]=0;
	a.len++;
	while(a.len>1&&a.s[a.len]==0) a.len--;
}

void divideh(const hp &a,const hp &b,hp &c,hp &d)  //高精度/高精度 　{d为余数}
{
	hp e;
	int i,len;
	for(i=1;i<=maxsize;i++)
	{
		c.s[i]=0;
		d.s[i]=0;
	}
	len=a.len;
	d.len=1;
	for(i=len;i>=1;i--)
	{
		multiply10(d);
		d.s[1]=a.s[i];
		while(compare(d,b)>=0)
		{
			subtract(d,b,e);
			d=e;
			c.s[i]++;
		}
	}
	while(len>1&&c.s[len]==0) len--;
	c.len=len;
}

hp gcd(const hp& a, const hp& b)
{
	if (b.len <= 1 && b.s[1] == 0)
	{
		return a;
	}
	hp c, d;
	divideh(a,b,c,d);
	return gcd(b, d);
}

int main()
{
	init();
	int a, b;
	int cases;
	scanf("%d", &cases);
	for (int i = 1; i <= cases; ++i)
	{
		printf("Case #%d: ", i);
		int n;
		scanf("%d", &n);
		char data[100];
		vector<hp> hps;
		for (int j = 0; j < n; ++j)
		{
			scanf("%s", data);
			hp hp_tmp;
			input(hp_tmp, string(data));
			hps.push_back(hp_tmp);
		}
		sort(hps.begin(), hps.end());
		vector<hp> dif;
		for (int j = 0; j + 1 < hps.size(); ++j)
		{
			if (hps[j] < hps[j+1])
			{
				hp c;
				subtract(hps[j+1],hps[j],c);
				//print(c);
				dif.push_back(c);
			}
		}
		hp gg = dif[0];
		for (int j = 1; j < dif.size(); ++j)
		{
			gg = gcd(gg, dif[j]);
		}
		hp cc, dd;
		divideh(hps[0],gg,cc,dd);
		if (dd.len <= 1 && dd.s[1] == 0)
		{
			printf("0\n");
		}
		else
		{
			hp res;
			subtract(gg,dd,res);
			print(res);
		}
	}
	return 0;
}
