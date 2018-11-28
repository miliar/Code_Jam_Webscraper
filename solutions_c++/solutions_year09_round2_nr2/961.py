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

		int a=s.length();
		int last=0;
		int m;
		for(m=0;m<a;m++)
		{
			if(s[a-m-1] >= last)
			{
				last=s[a-m-1];
				continue;
			}
			break;
		}
				cout<<"Case #"<<i+1<<": ";
		if(m!=a)
		{


			int p=s[a-m-1];
			int n;
			for(n=0;n<a;n++)
			{
				if(s[a-n-1]>p)
					break;
			}
			int tt=s[a-n-1];
			s[a-n-1]=s[a-m-1];
			s[a-m-1]=tt;
			for(int l=0;l<=a-m-1;l++)
			{
					cout<<s[l];
			}
			for(int l=0;l<m;l++)
			{
					cout<<s[a-l-1];
			}
			cout<<endl;			


		}
		else
		{
		
					int pp=0;
			while(s[a-pp-1]=='0')
			{
					pp++;			
			}
			cout<<s[a-pp-1];
			for(int cc=0;cc<=pp;cc++)
			{
				cout<<"0";
			}
			for(int m=pp+2;m<=a;m++)
			{
					cout<<s[a-m];
			}
			cout<<endl;

		
		
				}
	}
}
