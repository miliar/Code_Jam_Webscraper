#include<iostream>
#include<string>
#include<fstream>
using namespace std;

int x[41];

int main()
{
	
	ifstream cin("A.in");
	ofstream cout("A.out");
	
	int T;
	cin>>T;
	for(int c=1;c<=T;c++)
	{
	int n;
	cin>>n;
	for(int i=1;i<=n;i++)
	{
		int m=0;
		string t;
		cin>>t;
		for(int j=0;j<n;j++)
			if(t[j] == '1')
				m=j+1;
		x[i]=m;	
	}
	int r=0;
	for(int i=1;i<=n;i++)
		if(x[i] > i)
		{
			int last = 0;
			for(int j=i+1;j<=n;j++)
				if(x[j] <= i)
				{
					last = j;
					break;
				}
			for(int j=last-1 ;j>=i;j--)
			{
				r++;
				swap(x[j],x[j+1]);
			}
				
		}
	cout<<"Case #"<<c<<": "<<r<<endl;
	}
	return 0;
}
