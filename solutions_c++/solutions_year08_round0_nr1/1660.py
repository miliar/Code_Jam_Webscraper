#include <iostream>

using namespace std;

int main()
{
	int n,s,q,z=0;
	cin>>n;
	while (cin>>s)
	{
		//cout<<s<<endl;
		int m=0;
		string a[2000];
		getline(cin,a[0]);
		for (int i=0;i<s;i++)
			getline(cin,a[i]);
		bool u[1000]={0};
		cin>>q;
		//cout<<q<<endl;
		string b[2000];
		getline(cin,b[0]);
		for (int i=0;i<q;i++)
			getline(cin,b[i]);
		//cout<<b[0]<<endl;
		int c[q];
		for (int i=0;i<q;i++)
			for (int j=0;j<s;j++)
			{
				//cout<<i<<' '<<j<<b[i]<<a[j]<<endl;
				if (b[i]==a[j])
					c[i]=j;
			}
		/*for (int i=0;i<q;i++)
			cout<<c[i]<<' '<<b[i]<<endl;*/
		for (int i=0;i<q;i++)
		{
			u[c[i]]=1;
			bool xd=1;
			for (int j=0;j<s;j++)
				if (!u[j])
					xd=0;
			if (xd)
			{
				m++;
				for (int j=0;j<s;j++)
					u[j]=0;
			}
			//for (int i=0;i<s;i++)
			//	cout<<u[i];
			//cout<<endl;
			u[c[i]]=1;
		}
		cout<<"Case #"<<++z<<": "<<m<<endl;
	}
	return 0;
}