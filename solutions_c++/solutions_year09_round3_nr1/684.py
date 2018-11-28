#include <iostream>
#include <cstring>
#include <cstdio>
#include <map>
#include <cstdlib>

/////////////////////////////////////////////////
//  integer.h
/////////////////////////////////////////////////
//
//  实现高精度的整数类的声明。
//
/////////////////////////////////////////////////

#ifndef _INTEGER_H_DEF
#define _INTEGER_H_DEF

#include <iostream>
#include <cctype>

namespace Eire
{
	//  最大的位数支持，可以修改以扩大/缩小该类的数值表示范围
	const unsigned long _MAX_W = 5000;

	//  每位的最大值，一般不做改动
	const unsigned long _MAX_N = 10000;

	//  类的声明
	class integer
	{
	public:
		//默认构造函数，创建一个为0的高精度整数
		integer();
		//构造函数，由一个长整创建高精度整数
		integer(const long &num);
		//拷贝构造函数
		integer(const integer &i);

		//由一个长整设置该数的值
		void SetValue(const long &num=0);
		//由一个高精度整数设置该数的值
		void SetValue(const integer &i);

		//返回当前数的位数
		inline long GetLength() const;

		//高精度整数的流输入与输出
		friend std::istream & operator >> (std::istream &is,integer &i);
		friend std::ostream & operator << (std::ostream &os,const integer &i);

		//高精度整数的计算
		friend integer operator + (const integer &a,const integer &b);
		friend integer operator - (const integer &a,const integer &b);
		friend integer operator * (const integer &a,const integer &b);
	private:
		//将高精度整数标准化
		long Refresh();
		//成员变量
		unsigned long w;
		unsigned long n[_MAX_W];
	};

	//  类的实现

	integer::integer()
	{
		SetValue();
	}

	integer::integer(const long &num)
	{
		SetValue(num);
	}

	integer::integer(const integer &i)
	{
		SetValue(i);
	}

	void integer::SetValue(const long &num)
	{
		w=0;
		n[0]=num;
		Refresh();
	}

	void integer::SetValue(const integer &i)
	{
		std::memcpy(this,&i,sizeof(integer));
	}

	inline long integer::GetLength() const
	{
		return w;
	}

	std::istream & operator >> (std::istream &is,integer &i)
	{
		int iState=1;
		long len,temp,t;
		char c;
		i.SetValue();
		while (is.get(c))
		{
			if (!iState&&!std::isdigit(c))
			{
				is.putback(c);
				break;
			}
			else
			{
				if (iState&&!std::isdigit(c)) continue;
				iState=0;
				i=i*10+(c-'0');
			}
		}
		return is;
	}

	std::ostream & operator << (std::ostream &os,const integer &i)
	{
		long _t;
		char _c=os.fill();
		os.fill('0');
		os<<i.n[i.w];
		for (_t=i.w-1;_t>=0;_t--)
		{
			os.width(4);
			os<<i.n[_t];
		}
		os.fill(_c);
		return os;
	}

	integer operator + (const integer &a,const integer &b)
	{
		integer c;
		const integer *p;
		long len;
		if (a.w>b.w)
		{
			c=a;
			p=&b;
			len=b.w;
		}
		else
		{
			c=b;
			p=&a;
			len=a.w;
		}
		for (long i=0;i<=len;i++)
		{
			c.n[i]+=p->n[i];
		}
		c.Refresh();
		return c;
	}

	integer operator - (const integer &a,const integer &b)
	{
		integer c;
		const integer *p;
		long len;
		if (a.w>b.w)
		{
			c=a;
			p=&b;
			len=b.w;
		}
		else
		{
			c=b;
			p=&a;
			len=a.w;
		}
		for (long i=0;i<=len;i++)
		{
			c.n[i]+=p->n[i];
		}
		c.Refresh();
		return c;
	}

	integer operator * (const integer &a,const integer &b)
	{
		integer c(0);
		c.w=a.w;
		for (int i=b.w;i>=0;i--)
		{
			for (int j=0;j<=a.w;j++)
			{
				c.n[j]=c.n[j]+a.n[j]*b.n[i];
			}
			if (i!=0)
			{
				c.w++;
				for (int t=c.w;t>=0;t--)
				{
					c.n[t+1]=c.n[t];
				}
				c.n[0]=0;
			}
			c.Refresh();
		}
		return c;
	}

	long integer::Refresh()
	{
		int i;
		std::memset(n+w+1,0,(_MAX_W-w-1)*sizeof(long));
		for (i=0;i<=w;i++)
		{
			n[i+1]+=n[i]/_MAX_N;
			n[i]%=_MAX_N;
		}
		while (n[w+1]>0)
		{
			w++;
			n[w+1]+=n[w]/_MAX_N;
			n[w]%=_MAX_N;
		}
		return w;
	}

}; //namespace Eire

#endif


using namespace std;
using namespace Eire;

char buf[2048];
int len = 0;

int main()
{
	int t,_t;
	cin>>_t;
	for (t=1;t<=_t;t++)
	{
		map<char,int> value;
		cin>>buf;
		len = strlen(buf);
		int cnt = 1, base=0;
		for (int i=0;i<len;i++)
		{
			if (!value.count(buf[i]))
			{
				value[buf[i]]=cnt;
				cnt++;
				base++;
				if (cnt==2) cnt=0;
				if (cnt==1) cnt=2;
			}
		}
		integer res = 0;
		if (base==1) base=2;
		for (int i=0;i<len;i++)
		{
			res = res * base;
			res = res + value[buf[i]];
		}
		cout<<"Case #"<<t<<": "<<res<<endl;
	}
	return 0;
}
