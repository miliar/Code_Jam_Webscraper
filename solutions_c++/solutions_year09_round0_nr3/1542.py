#include <iostream>

using namespace std;

int main()
{
	int n;
	cin>>n;
	string u;
	
	getline(cin,u);
	u="welcome to code jam";
	
	for (int i=1;i<=n;i++)
	{
		string g;
		getline(cin,g);
		int l=g.size();
		int a[l][20];
		for (int j=0;j<l;j++)
			for (int k=0;k<20;k++)
				a[j][k]=0;
		for (int j=0;j<l;j++)
		{
			if (g[j]=='w')
				a[j][0]=1;
			for (int k=1;k<19;k++)
				if (g[j]==u[k])
				{
					for (int z=0;z<j;z++)
						a[j][k]=(a[j][k]+a[z][k-1])%10000;
				}
		}
		cout<<"Case #"<<i<<": ";
		int r=0;
		for (int j=0;j<l;j++)
			r=(r+a[j][18])%10000;
		if (r<10)
			cout<<0;
		if (r<100)
			cout<<0;
		if (r<1000)
			cout<<0;
		cout<<r<<endl;
	}
	return 0;
}