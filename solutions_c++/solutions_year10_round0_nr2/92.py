#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

const int maxlen= 15;
const int base=10000;

class HP
{
public:
	int len,s[maxlen];   //s[1]就表示第一位
	HP() { (* this)=0;};
	HP(int inte) { (*this)=inte;};
	HP(const char*str) { (* this)=str;};
	friend ostream& operator<<(ostream &cout,const HP &x)
	{
		printf("%d",x.s[x.len]);
		for(int i=x.len-1;i>=1;i--)
			printf("%04d",x.s[i]);
		return cout;
	}
	HP operator=(int inte);
	HP operator=(const char*str);
	HP operator*(const HP &b);
	HP operator+(const HP &b);
	HP operator-(const HP &b);
	HP operator/(const HP &b);
	HP operator%(const HP &b);
	int Compare(const HP &b);
};

HP HP::operator=(const char * str)
{
	int pow=1,v=0,slen=strlen(str);
	len=0;
    for(int i=slen-1;i>=0;i--)
    {
        v+=pow*(str[i]-'0');
        pow*=10;
        if(pow==base)
        {
            s[++len]=v;
            v=0;
            pow=1;
        }
    }
    if(v||!len) s[++len]=v;
	return *this;
}

HP HP::operator=(int inte)
{
	if(inte==0) 
	{
		len=1;
		s[1]=0;
		return (*this);
	}
	for(len=0;inte>0;)
	{
		s[++len]=inte%base;
		inte/=base;
	}
	return (*this);
}

HP HP::operator*(const HP &b)
{
	int i,j;
	HP c;
	c.len=len+b.len;
	for(i=1;i<=c.len;i++) 
		c.s[i]=0;
	for(i=1;i<=len;i++)
		for(j=1;j<=b.len;j++)
			c.s[i+j-1]+=s[i]*b.s[j];
	for(i=1;i<c.len;i++) 
	{
		c.s[i+1]+=c.s[i]/base;
		c.s[i]%=base;
	}
	while(c.s[i])
	{ 
		c.s[i+1]=c.s[i]/base;
		c.s[i]%=base;
		i++;
	}
	while(i>1 &&!c.s[i])
		i--;
	c.len=i;
	return c;
}

HP HP::operator+(const HP &b)
{
	int i;
	HP c;
	c.s[1]=0;
	for(i=1;i<=len||i<=b.len||c.s[i];i++)
	{
		if(i<=len) c.s[i]+=s[i];
		if(i<=b.len) c.s[i]+=b.s[i];
		c.s[i+1]=c.s[i]/base;
		c.s[i]%=base;
	}
	c.len=i-1;
	if(c.len==0) c.len=1;
	return c;
}

HP HP::operator-(const HP &b)
{
	int i,j;
	HP c;
	for(i=1,j=0;i<=len;i++)
	{
		c.s[i]=s[i]-j;
		if(i<=b.len) c.s[i]-=b.s[i];
		if(c.s[i]<0)
		{ 
			j=1;
			c.s[i]+=base;
		} 
		else j=0;
	}
	c.len=len;
	while(c.len>1&&!c.s[c.len]) 
		c.len--;
	return c;
}

int HP::Compare(const HP &y)
{
	if(len>y.len) return 1;
	if(len<y.len) return -1;
	int i=len;
	while((i>1)&&(s[i]==y.s[i]))
		i--;
	return s[i]-y.s[i];
}

HP HP::operator/(const HP &b)
{
	int i,j;
	HP d(0),c;
	for(i=len;i>0;i--) 
	{
		if(!(d.len==1&&d.s[1]==0))
		{
			for(j=d.len;j>0;j--) 
				d.s[j+1]=d.s[j];
			++d.len;
		}
		d.s[1]=s[i];
		c.s[i]=0;
		while((j=d.Compare(b))>=0)
		{ 
			d=d-b;
			c.s[i]++;
			if(j==0) break;
		}
	}
	c.len=len;
	while((c.len>1)&&(c.s[c.len]==0))
		c.len--;
	return c;
}

HP HP::operator%(const HP &b)
{
	int i,j;
	HP d(0);
	for(i=len;i>0;i--)
	{
		if(!(d.len==1 && d.s[1]==0))
		{ 
			for(j=d.len;j>0;j--) 
				d.s[j+1]=d.s[j];
			++d.len;
		}
		d.s[1]=s[i];
		while((j=d.Compare(b))>=0)
		{ 
			d=d-b;
			if(j==0) break;
		}
	}
	return d;
}

HP gcd(HP a,HP b)
{
	if(b.Compare(0)==0) return a;
	else return gcd(b,a%b);
}
bool cmp(HP& a,HP& b)
{
	if(a.Compare(b)<0)
		return true;
	return false;
}
int main()
{
	freopen("C:\\Documents and Settings\\Administrator\\桌面\\gcj\\B-small-attempt2.in","r",stdin);
	freopen("C:\\Documents and Settings\\Administrator\\桌面\\gcj\\B-small-attempt2.out","w",stdout);

	int cas;
	cin>>cas;
	int n;
	HP t[1010];
	HP cha[1010];
	char str[60];
	for(int cs=1;cs<=cas;cs++)
	{
		cin>>n;
		for(int i=0;i<n;i++)
		{
			cin>>str;
			t[i]=str;
		}
		sort(t,t+n,cmp);
		for(int i=0;i<n-1;i++)
		{
			cha[i]=t[i+1]-t[i];
		}
		
		HP g=cha[0];
		for(int i=1;i<n-1;i++)
		{
			g=gcd(g,cha[i]);
		}
		HP minn=t[0];
		for(int i=1;i<n;i++)
		{
			if(minn.Compare(t[i])>0)
				minn=t[i];
		}
		cout<<"Case #"<<cs<<": ";
		if((minn%g).Compare(0)==0)
			cout<<0<<"\n";
		else
		{
			cout<<g-minn%g<<"\n";
		}
	}
}