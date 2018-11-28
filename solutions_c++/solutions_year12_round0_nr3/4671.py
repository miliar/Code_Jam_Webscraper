#include<iostream>
#include<string>
#include<cstdio>
#include<algorithm>
#include<sstream>
using namespace std;
int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	int t;
	cin>>t;
	int temp=t;
	while(t--)
	{
		int a,b;
		cin>>a>>b;
		int digits=0;
		int y=a;
		while(y>0)
		{
			digits++;
			y/=10;
		}
		if(digits==1)
		{
			cout<<"Case #"<<temp-t<<": "<<"0"<<endl;
			continue;
		}
	
		int count=0;
		for(int i=a;i<=b;i++)
		{
			for(int j=i+1;j<=b;j++)
			{
				if(digits == 2)
				{
					y=i%10;
					int z=i/10;
					int q=y*10 + z;
					if(q == j)
						count++;
				}
				else
				{
					y=i%10;
					int z=i/10;
					int q=y*100 + z;
					if(q==j)
					{
						count++;
						continue;
					}
					y=q%10;
					z=q/10;
					q=y*100 + z;
					if(q==j)
						count++;
				}
			}
		}
		cout<<"Case #"<<temp-t<<": "<<count<<endl;
	}
}