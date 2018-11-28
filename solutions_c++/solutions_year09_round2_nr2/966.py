#include<iostream>
#include<string.h>
using namespace std;
int main()
{
	int n;
	cin>>n;
	for(int i=0;i<n;i++)
	{
		string s;
		cin>>s;
		cout<<"Case #"<<i+1<<": ";
		int a=s.length();
		int last=0;
		int j;
		for(j=0;j<a;j++)
		{
			if(s[a-j-1] >= last)
			{
				last=s[a-j-1];
				continue;
			}
			break;
		}
		if(j==a)
		{
			int pp=0;
			while(s[a-pp-1]=='0')
			{
					pp++;			
			}
			//cout<<pp<<endl;
			cout<<s[a-pp-1];
			for(int cc=0;cc<=pp;cc++)
			{
				cout<<"0";
			}
			for(int j=pp+2;j<=a;j++)
			{
					cout<<s[a-j];
			}
			cout<<endl;
		}
		else
		{
			//cout<<j<<endl;
			int p=s[a-j-1];
			int k;
			for(k=0;k<a;k++)
			{
				if(s[a-k-1]>p)
					break;
			}
			//cout<<k<<endl;
			int temp=s[a-k-1];
			s[a-k-1]=s[a-j-1];
			s[a-j-1]=temp;
			//cout<<s<<endl;
			for(int l=0;l<=a-j-1;l++)
			{
					cout<<s[l];
			}
			for(int l=0;l<j;l++)
			{
					cout<<s[a-l-1];
			}
			cout<<endl;			
		}
	}
}
