#include<iostream>
#include<vector>
#include<utility>
#include<string>
#include<algorithm>

using namespace std;

int main()
{
	int t,n,pd,pg;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		cin>>n>>pd>>pg;
		cout<<"Case #"<<i+1<<": ";
		if((pg==100&&pd<100)||(pg==0&&pd>0))
		{
			cout<<"Broken"<<endl;
		}
		else
		{
			if(n<100)
			{
				for(int i=1;i<=n;i++)
				{
					if((pd*i)%100==0)
					{
						cout<<"Possible"<<endl;
						break;
					}
					if(i==n)
					{
						cout<<"Broken"<<endl;
					}
				}
			}
			else
				cout<<"Possible"<<endl;
		}
	}
	return 0;
}
