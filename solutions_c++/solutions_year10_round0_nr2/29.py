#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;

const int maxleng=50;

class BigInt
{
public:
	int leng;
	int num[maxleng];
	BigInt()
	{
		leng=1;
		memset(num,0,sizeof(num));
	}
	BigInt(int x)
	{
		leng=0;
		memset(num,0,sizeof(num));
		while(x)
		{
			num[leng++]=x%10000;
			x/=10000;
		}
		if(leng==0)leng=1;
	}
	operator int()
	{
		int x=0,l=leng-1;
		while(l>=0)
		{
			x=x*10000+num[l];
			l--;
		}
		return x;
	}
	operator int*()
	{
		return num;
	}
	int length()
	{
		return leng;
	}
	void read()
	{
		clear();
		char s[maxleng+1];
		scanf("%s",s);
		int l=strlen(s);
		leng=0;
		for(int i=l-1;i>=0;)
		{
			if(i>=0)num[leng]+=(s[i--]-'0');
			if(i>=0)num[leng]+=(s[i--]-'0')*10;
			if(i>=0)num[leng]+=(s[i--]-'0')*100;
			if(i>=0)num[leng]+=(s[i--]-'0')*1000;
			leng++;
		}
		if(leng==0)leng=1;
	}
	void clear()
	{
		leng=1;
		memset(num,0,sizeof(num));
	}
	void write()
	{
		int i=leng-1;
		printf("%d",num[i]);i--;
		while(i>=0)printf("%04d",num[i--]);
	}
	void writeln()
	{
		write();
		printf("\n");
	}
	void getlength()
	{
		leng=maxleng-1;
		while(num[leng]==0&&leng>0)leng--;
		leng++;
	}
	friend BigInt operator+(BigInt a,BigInt b);
	friend BigInt operator+(BigInt a,int b);
	friend BigInt operator-(BigInt a,BigInt b);
	friend BigInt operator*(BigInt a,BigInt b);
	friend BigInt operator*(BigInt a,int b);
	friend BigInt operator/(BigInt a,BigInt b);
	friend bool operator<=(BigInt a,BigInt b);
	friend bool operator<(BigInt a,BigInt b);
	friend BigInt operator%(BigInt a,BigInt b);
};

BigInt operator+(BigInt a,BigInt b)
{
	int l=a.leng>b.leng?a.leng:b.leng,t=0;
	BigInt ans;
	for(int i=0;i<l;i++)
	{
		ans[i]=(a[i]+b[i]+t)%10000;
		t=(a[i]+b[i]+t)/10000;
	}
	while(t)
	{
		ans[l++]=t%10000;
		t/=10000;
	}
	ans.leng=l;
	return ans;
}

BigInt operator+(BigInt a,int b)
{
	int t=0;
	BigInt ans;
	memcpy(ans.num,a.num,sizeof(a.num));
	ans[t]+=b;
	while(a[t]>=10000)
	{
		ans[t+1]+=ans[t]/10000;
		ans[t]%=10000;
	}
	ans.getlength();
	return ans;
}

BigInt operator-(BigInt a,BigInt b)
{
	int l=a.leng;
	BigInt ans;
	memcpy(ans.num,a.num,sizeof(a.num));
	for(int i=0;i<l;i++)
	{
		ans[i]-=b[i];
		if(ans[i]<0)
		{
			ans[i]+=10000;
			ans[i+1]--;
		}
	}
	ans.getlength();
	return ans;
}

BigInt operator*(BigInt a,BigInt b)
{
	int la=a.leng,lb=b.leng,t,p;
	BigInt ans;
	for(int i=0;i<la;i++)
	{
		t=0;
		for(int j=0;j<lb;j++)
		{
			p=(ans[i+j]+a[i]*b[j]+t)/10000;
			ans[i+j]=(ans[i+j]+a[i]*b[j]+t)%10000;
			t=p;
		}
		p=i+lb;
		if(t)
		{
			ans[p]+=t;
			while(ans[p]>=10000)
			{
				ans[p+1]+=ans[p]/10000;
				ans[p]%=10000;
				p++;
			}
		}
	}
	ans.getlength();
	return ans;
}

BigInt operator*(BigInt a,int b)
{
	int t=0,p=a.leng;
	BigInt ans;
	for(int i=0;i<p;i++)
	{
		ans[i]=(a[i]*b+t)%10000;
		t=(a[i]*b+t)/10000;
	}
	while(t)
	{
		ans[p++]=t%10000;
		t/=10000;
	}
	ans.getlength();
	return ans;
}

bool operator<=(BigInt a,BigInt b)
{
	if(a.leng!=b.leng)return a.leng<b.leng;
	for(int i=a.leng-1;i>=0;i--)
		if(a[i]!=b[i])return a[i]<b[i];
	return true;
}

bool operator<(BigInt a,BigInt b)
{
	if(a.leng!=b.leng)return a.leng<b.leng;
	for(int i=a.leng-1;i>=0;i--)
		if(a[i]!=b[i])return a[i]<b[i];
	return false;
}

BigInt operator/(BigInt a,BigInt b)
{
	int la=a.leng,lb=b.leng;
	BigInt ans,p;
	for(int i=la-1;i>=0;i--)
	{
		p=p*10000+a[i];
		for(int j=13;j>=0;j--)
		{
			if(b*(1<<j)<=p)
			{
				p=(p-b*(1<<j));
				ans[i]+=(1<<j);
			}
		}
	}
	ans.getlength();
	return ans;
}

BigInt operator%(BigInt a,BigInt b)
{
	return a-(a/b)*b;
}

BigInt gcd(BigInt a,BigInt b)
{
	if (a.leng==1 && a[0]==0) return b;
	return gcd(b%a,a);
}

BigInt a[1005],ans;

int main()
{
	freopen("B_large.in","r",stdin);
	freopen("B_large.out","w",stdout);
	
	int test=1,T;
	for (scanf("%d",&T);test<=T;++test)
	{
		int n;
		scanf("%d",&n);
		for (int i=0;i<n;++i)
			a[i].read();
		sort(a,a+n);
		ans=a[1]-a[0];
		for (int i=2;i<n;++i)
			ans=gcd(ans,a[i]-a[i-1]);
		printf("Case #%d: ",test);
		((ans-a[0]%ans)%ans).writeln();
	}
	
	return 0;
}
