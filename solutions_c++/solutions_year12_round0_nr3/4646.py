#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

int newnum(int a,int b)
{
	int bb=0;
	bb=a%10;
	a/=10;
	return (int)pow(10,(double)b)*bb+a;
}

int main()
{
	ifstream cin("input.in");
	ofstream cout ("c.out");
	int t ;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		int a,b,c,d,size=0,ans=0;
		cin>>a>>b;
		c=a;
		while(c)
		{
			c/=10;
			size++;
		}
		for(int j=a;j<=b;j++)
		{
			d=j;
			for(int u=0;u<size-1;u++)
			{
				d=newnum(d,size-1);
				if(d>=j && d<=b && j!=d)
					ans++;
			}
		}
		cout<<"Case #"<<i+1<<": "<<ans<<endl;
	}
	return 0;
}