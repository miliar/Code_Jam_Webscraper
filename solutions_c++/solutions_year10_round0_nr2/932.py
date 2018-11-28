#include <stdio.h>
#include <string>
#include <algorithm>
using namespace std;

const int POWOSN=4;
const int OSN=10000;
const int SIZE=13;

class Long
{
	int *buffer;
	int buf_size;

	static Long x10(const Long &a)
	{
		Long res(a);
		res.buffer[res.buf_size]=0;
		for(int i=res.buf_size-1;i>=0;i--)
		{
			int t=res.buffer[i]*10;
			res.buffer[i+1]+=t/OSN;
			res.buffer[i]=t%OSN;
		}
		if(res.buffer[res.buf_size]>0)
			res.buf_size++;
		return res;
	}

	static void Modul(Long &res,const Long &b)
	{
		if(res<b)
			return;
		Modul(res,x10(b));
		while(res>=b)
			res-=b;
	}

public:
	Long()
	{
		buf_size=1;
		buffer=new int[SIZE];
		buffer[0]=0;
	}

	Long(const Long &b)
	{
		buf_size=b.buf_size;
		buffer=new int[SIZE];
		memcpy(buffer,b.buffer,buf_size*sizeof(int));
	}

	Long &operator=(const Long &b)
	{
		if(this==&b)
			return *this;
		buf_size=b.buf_size;
		memcpy(buffer,b.buffer,buf_size*sizeof(int));
		return *this;
	}

	bool isNull() const
	{
		return (buf_size==1)&&(buffer[0]==0);
	}

	~Long()
	{
		delete[] buffer;
	}

	int &operator[](int index)
	{
		return buffer[index];
	}

	void Read()
	{
		char str[52];
		scanf("%s",str);
		int len=strlen(str);
		for(int i=0;i<len/2;i++)
			swap(str[i],str[len-i-1]);
		buf_size=(len+POWOSN-1)/POWOSN;
		for(int i=0;i<buf_size-1;i++)
		{
			buffer[i]=0;
			for(int j=POWOSN-1;j>=0;j--)
				buffer[i]=buffer[i]*10+str[i*POWOSN+j]-'0';
		}
		buffer[buf_size-1]=0;
		int t=len-1;
		while(t>=(buf_size-1)*POWOSN)
			buffer[buf_size-1]=buffer[buf_size-1]*10+str[t--]-'0';
	}

	void Write()
	{
		printf("%d",buffer[buf_size-1]);
		for(int i=buf_size-2;i>=0;i--)
			printf("%0*d",POWOSN,buffer[i]);
	}

	bool operator<(const Long &b) const
	{
		if(buf_size<b.buf_size)
			return true;
		if(buf_size>b.buf_size)
			return false;
		for(int i=buf_size-1;i>=0;i--)
			if(buffer[i]<b.buffer[i])
				return true;
			else if(buffer[i]>b.buffer[i])
				return false;
		return false;
	}

	bool operator>(const Long &b) const
	{
		return b<(*this);
	}

	bool operator==(const Long &b) const
	{
		if(buf_size!=b.buf_size)
			return false;
		for(int i=0;i<buf_size;i++)
			if(buffer[i]!=b.buffer[i])
				return false;
		return true;
	}

	bool operator!=(const Long &b) const
	{
		return !((*this)==b);
	}

	bool operator<=(const Long &b) const
	{
		return ((*this)<b)||((*this)==b);
	}

	bool operator>=(const Long &b) const
	{
		return b<=(*this);
	}

	void Swap(Long &b)
	{
		swap(buf_size,b.buf_size);
		swap(buffer,b.buffer);
	}

	Long &operator-=(const Long &b)
	{
		for(int i=0;i<b.buf_size;i++)
		{
			if(buffer[i]<b.buffer[i])
			{
				buffer[i]+=OSN;
				int t=i+1;
				while(buffer[t]==0)
					buffer[t++]=OSN-1;
				buffer[t]--;
			}
			buffer[i]-=b.buffer[i];
		}
		while((buf_size>1)&&(buffer[buf_size-1]==0))
			buf_size--;
		return *this;
	}

	Long operator-(const Long &b) const
	{
		return (Long(*this)-=b);
	}

	Long &operator%=(const Long &b)
	{
		Modul(*this,b);
		return *this;
	}

	Long operator%(const Long &b) const
	{
		Long res(*this);
		Modul(res,b);
		return res;
	}
};

namespace std
{
	void swap(Long &a,Long &b)
	{
		a.Swap(b);
	}
};

Long Euclid(Long a,Long b)
{
	for(;;)
	{
		if(b.isNull())
			return a;
		if(a.isNull())
			return b;
		a%=b;
		a.Swap(b);
	}
}

Long t[1000];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int Case_count;
	scanf("%d",&Case_count);
	for(int Case=1;Case<=Case_count;Case++)
	{
		printf("Case #%d: ",Case);
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;i++)
			t[i].Read();
		sort(t,t+n);
		Long gcd;
		for(int i=0;i<n;i++)
			for(int j=i+1;j<n;j++)
				gcd=Euclid(gcd,t[j]-t[i]);
		((gcd-(t[0]%gcd))%gcd).Write();
		printf("\n");
	}
	return 0;
}