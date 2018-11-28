#include<iostream>
#include<vector>
#include<string>
#include<utility>
#include<algorithm>
#include<cmath>
 using namespace std;
 int main()
{
	int t,r,c,flag;
	string ar[50];
	cin>>t;
	for(int i=0;i<t;i++)
	{
		cin>>r>>c;
		for(int j=0;j<r;j++)
		{
			cin>>ar[j];
		}
		flag=0;
		for(int j=0;j<r;j++)
		{	
			for(int k=0;k<c;k++)
			{
				if(ar[j][k]=='#')
				{
					if(j+1>r||k+1>c||ar[j+1][k]!='#'||ar[j][k+1]!='#'||ar[j+1][k+1]!='#')
					{
						flag=1;break;
					}
					ar[j][k]='/';
					ar[j][k+1]='\\';
					ar[j+1][k+1]='/';
					ar[j+1][k]='\\';
				}
				
			}
			if(flag){break;}
		}
		if(flag){cout<<"Case #"<<i+1<<": \nImpossible"<<endl;continue;}
		cout<<"Case #"<<i+1<<": "<<endl;
		for(int j=0;j<r;j++)
		{	
			for(int k=0;k<c;k++)
			{
				cout<<ar[j][k];
			}cout<<endl;
		}
		
	}
	return 0;
} 
