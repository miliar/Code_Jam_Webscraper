#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int ca;
	cin>>ca;
	for (int cou=1;cou<=ca;cou++)
	{
		int pd, pg;
		long long n;
		cin>>n>>pd>>pg;
		int ans=1;
		if ((pg==100 && pd!=100) || (pg==0 && pd!=0))
		{
			ans=1;
		}
		else
		{
			while(n>0)
			{
				if (n*pd%100==0)
				{
					ans=0;
					break;
				}
				n--;
			}
		}
		cout<<"Case #"<<cou<<": ";
		if (ans==1)
			cout<<"Broken";
		else
			cout<<"Possible";
		cout<<endl;
	}
}
