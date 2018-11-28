#include <iostream>

using namespace std;

int main()
{
	int m;
	cin>>m;
	for (int q=1;q<=m;q++)
	{
		string x;
		cin>>x;
		cout<<"Case #"<<q<<": ";
		char a[50]={'0'};
		long long b=0;
		a[1]=x[0];
		for (int i=0;i<x.size();i++)
			if (x[i]!=a[1])
		{
			a[0]=x[i];
			i=99999;
			break;
		}
		b=2;
		
		for (int i=0;i<x.size();i++)
		{
			bool xd=1;
			for (int j=0;j<b;j++)
				if (x[i]==a[j])
					xd=0;
			if (xd)
				a[b++]=x[i];
		}
		
		long long g=0;
		for (int i=0;i<x.size();i++)
		{
			for(int j=0;j<b;j++)
				if (x[i]==a[j])
					g=g*b+j;
		}
		cout<<g<<endl;
		
	}
	return 0;
}
