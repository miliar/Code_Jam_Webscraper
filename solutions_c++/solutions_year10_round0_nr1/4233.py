#include<iostream>
#include<stdio.h>
using namespace std;

bool ak[50];
int main()
{
	freopen("c:\\111.in","r",stdin);
freopen("c:\\out.txt","w",stdout);
	int t;
	cin>>t;
	int i;
	for(i=1;i<=t;i++)
	{
		int n;
		long long k,j;
		cin>>n>>k;
		for(j=1;j<=n;j++)
			ak[j]=false;
		for(j=1;j<=k;j++)
		{
			int h=1;
			while((ak[h]==true)&&(h<n))
				h++;
			if(h>n) h=n;
			int temp;
			for(temp=1;temp<=h;temp++)
				if(ak[temp]==true)
					ak[temp]=false;
				else
					ak[temp]=true;

			
		}
		bool yes=true;
		for(j=1;j<=n;j++)
			if(ak[j]==false)
			{
				yes=false;
				break;
			}
		if(yes==false)
		cout<<"Case #"<<i<<": OFF"<<endl;
		else
		cout<<"Case #"<<i<<": ON"<<endl;


	}






return 0;
}