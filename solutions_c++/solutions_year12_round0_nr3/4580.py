#include<iostream>
#include<fstream>
#include<cstdio>
#include<vector>
#include<cmath>
using namespace std;
int Neworder(int x,int b)
{
	int a=0;
	a=x%10;
	return (int)pow(10,(double)b-1)*a+x/10;
}
int main()
{
	ifstream cin("a.in");
	ofstream cout("b.out");
	//vector<int>s;
	int n,l=1;
	cin>>n;
	for(int ii=0;ii<n;ii++)
	{
		int x,y,ans=0;
		cin>>x>>y;
		int a=0,b=0;
		a=x;
		for(int iii=0;a>0;iii++)
		{
			a/=10;
			b++;
		}
		for(int i=x;i<=y;i++)
		{
			int c;
			c=i;
			for(int j=1;j<=b;j++)
			{
				c=Neworder(c,b);
				if(c>=i&&c<=y&&c!=i)
				{
					ans++;
				}
			}
		}
		cout<<"Case #"<<l<<": "<<ans<<endl;
		l++;
	}
}