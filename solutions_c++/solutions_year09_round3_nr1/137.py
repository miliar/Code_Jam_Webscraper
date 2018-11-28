#include <iostream>
#include <fstream>
#include <string>

using namespace std;

ifstream ci("b1.in");
ofstream co("b1.out");

int main()
{
	int T;
	ci>>T;
	string s;
	int a[256];
	int k;
	for (int t1=0;t1<T;++t1)
	{
		ci>>s;
		k=0;
		for (int i=0;i<256;++i)
			a[i]=-1;
		for (int i=0;i<s.size();++i)
		{
			if (a[int(s[i])]<0)
			{
				if (i==0)
				{
					a[int(s[i])]=1;
				}
				else
				{
					if (k==0)
					{
						k=1;
						a[int(s[i])]=0;
					}
					else
					{
						++k;
						a[int(s[i])]=k;
					}
				}
			}
		}
		if (k==0)
			k=k+2;
		else
		k=k+1;
		int aa=0,b=0,c=0,a1=0,b1=0,c1=1;
		for (int i=s.size()-1;i>-1;--i)
		{
			c=c+c1*a[int(s[i])];
			b=b+b1*a[int(s[i])];
			aa=aa+a1*a[int(s[i])];
			aa=aa+int(b/10000000);
			b=b%10000000+int(c/10000000);
			c=c%10000000;
			c1=c1*k;
			b1=b1*k;
			a1=a1*k;
			a1=a1+int(b1/10000000);
			b1=b1%10000000+int(c1/10000000);
			c1=c1%10000000;
		}
		co<<"Case #"<<t1+1<<": ";
		if (aa>0)
		{
			co<<aa;
		if (b<1000000)
			co<<"0";
		if (b<100000)
			co<<"0";
		if (b<10000)
			co<<"0";
		if (b<1000)
			co<<"0";
		if (b<100)
			co<<"0";
		if (b<10)
			co<<"0";
		co<<b;
		if (c<1000000)
			co<<"0";
		if (c<100000)
			co<<"0";
		if (c<10000)
			co<<"0";
		if (c<1000)
			co<<"0";
		if (c<100)
			co<<"0";
		if (c<10)
			co<<"0";
		co<<c<<endl;
		}
		else
			if  (b>0)
			{
				co<<b;
		if (c<1000000)
			co<<"0";
		if (c<100000)
			co<<"0";
		if (c<10000)
			co<<"0";
		if (c<1000)
			co<<"0";
		if (c<100)
			co<<"0";
		if (c<10)
			co<<"0";
		co<<c<<endl;
			}
			else
				if (c>0)
					co<<c<<endl;
		
	}
	return 0;
}