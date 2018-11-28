#include <iostream>
using namespace std;


//init
int a[l][20];

void init()
{
	for (int j=0;j<l;j++)
		for (int k=0;k<19;k++)
			a[j][k]=0;
}

int main()
{
	int nn;
	cin>>nn;
	string uu;

	
	//read 1st
	getline(cin,uu);
	uu="welcome to code jam";
	
	//for each
	for (int i=1;i<=nn;i++)
	{
		string g;
		getline(cin,g);
		int l=g.length();
		
		init();
		
		
		//calculate
		
		for (int j=0;j<l;j++)
		{
			if (g[j]=='w')
				a[j][0]=1;
			
			for (int k=1;k<19;k++)
				if (g[j]==uu[k])
				{
					for (int zq=0;zq<j;zq++)
						a[j][k]=(a[zq][k-1]+a[j][k])%10000;
				}
		}
		
		int r=0;
		for (int jg=0;jg<l;jg++)
			r=(r+a[jg][18])%10000;
		
		
		cout<<"Case #"<<i<<": ";
		
		if (r<10)
			cout<<"0";
		if (r<100)
			cout<<"0";
		if (r<1000)
			cout<<"0";
		
		cout<<r<<endl;
		
	}
	return 0;
}