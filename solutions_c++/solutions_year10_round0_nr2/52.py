#pragma warning(disable:4786)
#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <map>
#include <string>

using namespace std;

const int base=1000000,num_digit=6;

#ifdef _MSC_VER
#define LL __int64
#else
#define LL long long
#endif

struct big_num
{
	big_num():num(0){}
	big_num(const big_num &bn)
	{
		size=bn.size;
		num=new int[size];
		memcpy(num,bn.num,sizeof(int)*size);
	}
	~big_num() 
	{
		if(num) delete num;
	}
	big_num & operator = (const big_num &bn)
	{
		if(num) delete [] num;
		size=bn.size;
		num=new int[size];
		memcpy(num,bn.num,sizeof(int)*size);
		return *this;
	}
	big_num(const char * buf)
	{
		int len=strlen(buf);
		int i;
		size=(len-1)/num_digit+1;
		num=new int[size];
		memset(num,0,sizeof(int)*size);
		for(i=0;i<len;i++)
		{
			num[(len-1-i)/num_digit]*=10;
			num[(len-1-i)/num_digit]+=buf[i]-'0';
		}
		while(size>1&&num[size-1]==0) size--;
	}
	big_num operator () (int x,int y) const;
	int *num;
	int size;
};

big_num int2bn(int a)
{
	int t=a;
	big_num c;
	c.size=0;
	while(t)
	{
		c.size++;
		t/=base;
	}
	if(c.size==0) c.size++;
	c.num=new int[c.size];
	int i;
	t=a;
	for(i=0;i<c.size;i++)
	{
		c.num[i]=t%base;
		t/=base;
	}
	return c;
}

ostream & operator << (ostream &os,const big_num &bn)
{
	int i;
	printf("%d",bn.num[bn.size-1]);
	for(i=bn.size-2;i>=0;i--)
	{
		printf("%0*d",num_digit,bn.num[i]);
	}
	return os;
}

istream & operator >> (istream &is,big_num &bn)
{
	char buf[1000];
	if(scanf("%s",buf)!=1) throw 1;
	bn=buf;
	return is;
}

big_num operator + (const big_num &a,const big_num &b)
{
	big_num c;
	c.size=a.size+1;
	if(b.size+1>c.size) c.size=b.size+1;
	c.num=new int[c.size];
	int i;
	LL tmp=0;
	for(i=0;i<c.size;i++)
	{
		if(i<a.size) tmp+=a.num[i];
		if(i<b.size) tmp+=b.num[i];
		c.num[i]=tmp%base;
		tmp/=base;
	}
	while(c.size>1&&c.num[c.size-1]==0) c.size--;
	return c;
}

big_num operator - (const big_num &a,const big_num &b)
{
	big_num c=a;
	int i;
	for(i=0;i<a.size;i++)
	{
		if(i<b.size) c.num[i]-=b.num[i];
		if(c.num[i]<0)
		{
			c.num[i]+=base;
			c.num[i+1]--;
		}
	}
	while(c.size>1&&c.num[c.size-1]==0) c.size--;
	return c;
}

big_num operator * (const big_num a,int b)
{
	big_num c;
	c.size=a.size;
	int t=b;
	while(t)
	{
		c.size++;
		t/=base;
	}
	c.num=new int[c.size];
	int i;
	LL tmp=0;
	for(i=0;i<c.size;i++)
	{
		if(i<a.size) tmp+=(LL)a.num[i]*b;
		c.num[i] =tmp%base;
		tmp/=base;
	}
	while(c.size>1&&c.num[c.size-1]==0) c.size--;
	return c;
}

big_num operator * (int a,const big_num &b)
{
	return b*a;
}

big_num operator * (const big_num &a,const big_num &b)
{
	big_num c;
	c.size=a.size+b.size;
	c.num=new int[c.size];
	int i,j;
	LL tmp=0;
	for(i=0;i<c.size;i++)
	{
		int bg=0,ed=a.size-1;
		if(i-b.size+1>bg) bg=i-b.size+1;
		if(i<ed) ed=i;
		for(j=bg;j<=ed;j++)
		{
			tmp+=(LL)a.num[j]*b.num[i-j];
		}
		c.num[i]=tmp%base;
		tmp/=base;
	}
	while(c.size>1&&c.num[c.size-1]==0) c.size--;
	return c;
}

bool operator == (const big_num &a,const big_num &b)
{
	if(a.size!=b.size) return false;
	int i;
	for(i=0;i<a.size;i++)
		if(a.num[i]!=b.num[i]) return false;
	return true;
}

bool operator != (const big_num &a,const big_num &b)
{
	return !(a==b);
}

bool operator < (const big_num &a,const big_num &b)
{
	if(a.size!=b.size) return a.size<b.size;
	int i;
	for(i=a.size-1;i>=0;i--)
		if(a.num[i]!=b.num[i]) return a.num[i]<b.num[i];
	return false;
}

bool operator <= (const big_num &a,const big_num &b)
{
	if(a.size!=b.size) return a.size<b.size;
	int i;
	for(i=a.size-1;i>=0;i--)
		if(a.num[i]!=b.num[i]) return a.num[i]<b.num[i];
	return true;
}

bool operator > (const big_num &a,const big_num &b)
{
	return b<a;
}

bool operator >= (const big_num &a,const big_num &b)
{
	return b<=a;
}

big_num operator /(const big_num &a,int b)
{
	big_num c;
	c.size=a.size;
	c.num=new int[c.size];
	int i;
	LL tmp=0;
	for(i=c.size-1;i>=0;i--)
	{
		tmp*=base;
		if(i<a.size) tmp+=a.num[i];
		c.num[i]=tmp/b;
		tmp%=b;
	}
	while(c.size>1&&c.num[c.size-1]==0) c.size--;
	return c;
}

int operator % (const big_num &a,int b)
{
	big_num c;
	c.size=a.size;
	c.num=new int[c.size];
	int i;
	LL tmp=0;
	for(i=c.size-1;i>=0;i--)
	{
		tmp*=base;
		if(i<a.size) tmp+=a.num[i];
		c.num[i]=tmp/b;
		tmp%=b;
	}
	return tmp;
}

big_num operator / (const big_num &a,const big_num &b)
{
	big_num c="0";
	big_num r="1";
	big_num tmp=b;
	while(tmp<a)
	{
		tmp=tmp*2;
		r=r*2;
	}
	big_num t=a;
	while(r!="0")
	{
		if(t>=tmp)
		{
			t=t-tmp;
			c=c+r;
		}
		tmp=tmp/2;
		r=r/2;
	}
	return c;
}

big_num operator % (const big_num &a,const big_num &b)
{
	big_num c="0";
	big_num r="1";
	big_num tmp=b;
	while(tmp<a)
	{
		tmp=tmp*2;
		r=r*2;
	}
	big_num t=a;
	while(r!="0")
	{
		if(t>=tmp)
		{
			t=t-tmp;
			c=c+r;
		}
		tmp=tmp/2;
		r=r/2;
	}
	return t;
}

int xyz;

big_num operator & (const big_num &a,const big_num &b)
{
	big_num ta=a,tb=b;
	big_num c="1";
	while(1)
	{
		xyz++;
		if(ta=="0")
		{
			c=c*tb;
			break;
		}
		if(tb=="0")
		{
			c=c*ta;
			break;
		}
		int ra=ta%2;
		int rb=tb%2;
		if(ra==0&&rb==0) c=c*2;
		if(ra==1&&rb==1) 
		{
			if(ta>=tb) ta=ta-tb;
			else tb=tb-ta;
		}
		if(ra==0) ta=ta/2;
		if(rb==0) tb=tb/2;
	}
	return c;
}

big_num operator | (const big_num &a,const big_num &b)
{
	if(a=="0"&&b=="0") return "0";
	return a/(a&b)*b;
}

big_num operator ^ (const big_num &a,const big_num &b)
{
	big_num t="1";
	while(t<b)
	{
		t=t*2;
	}
	big_num c="1";
	big_num tmp=b;
	while(t!="0")
	{
		c=c*c;
		if(t<=tmp)
		{
			tmp=tmp-t;
			c=c*a;
		}
		t=t/2;
	}
	return c;
}

big_num big_num::operator ()(int x,int y) const
{
	big_num ex=int2bn(10)^int2bn(x);
	big_num ey=int2bn(10)^int2bn(y+1);
	return (*this)/ex%ey;
}

big_num bn[1010];
int ct;

big_num solve()
{
	sort(bn,bn+ct);
	big_num deta="0";
	int i;
	for(i=1;i<ct;i++)
	{
		deta=deta&(bn[i]-bn[i-1]);
	}
	big_num y=bn[0]/deta*deta;
	if(y<bn[0]) y=y+deta;
	return y-bn[0];
}

int main()
{
	int t;
	scanf("%d",&t);
	int cse=0;
	while(t--)
	{
		cse++;
		scanf("%d",&ct);
		int i;
		for(i=0;i<ct;i++)
		{
			char buf[1000];
			scanf("%s",buf);
			bn[i]=buf;
		}
		big_num ret=solve();
		printf("Case #%d: ",cse);
		cout<<ret<<endl;
	}
	return 0;
}
