#include<iostream>
using namespace std;
int p,g,times,now;
long long n;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.out","w",stdout);
	scanf("%d",&times);
	for (int z=1;z<=times;++z)
	{
		cin>>n>>p>>g;
		cout<<"Case #"<<z<<": ";
		int now=100;
		for (int a=1;a<=2;++a)
		{
			if (p%2==0)
			{
				p/=2;
				now/=2;
			}
			if (p%5==0)
			{
				p/=5;
				now/=5;
			}
		}
		if (now>n) 
		{
			cout<<"Broken"<<endl;
			continue;
		}
		if ((p!=now)&&(g==100))
		{
			cout<<"Broken"<<endl;
			continue;
		}
		if ((p!=0)&&(g==0))
		{
			cout<<"Broken"<<endl;
			continue;
		}
		cout<<"Possible"<<endl;
	}
}
