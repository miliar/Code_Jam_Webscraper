#include<iostream>
using namespace std;

int t,n,pd,pg;
bool god;

int main()
{
	//freopen("in.txt","r",stdin);
	freopen("A-small-attempt2.in","r",stdin);
	//freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>t;
	for(int ca=1;ca<=t;++ca)
	{
		god=true;
		cin>>n>>pd>>pg;
		if(pd!=0&&pg==0)
		{
			goto out;
		}
		for(int c=1;c<=n;++c)
		{
			for(int a=0;a<=c;++a)
			{
				if(c*pd==a*100)
				{
					for(int d=0;d<=20000;++d)
					{
						for(int b=0;b<=d;++b)
						{
							if((a+b)*100==(c+d)*pg)
							{
								god=false;
								goto out;
							}
						}
					}
				}
			}
		}
out:	printf("Case #%d: %s\n",ca,god?"Broken":"Possible");
	}
	return 0;
}
