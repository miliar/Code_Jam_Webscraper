#include<iostream>
#include<cmath>
#include<vector>
#include<cstring>
#include<stdio.h>
using namespace std;
char mat[123][123];
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,cas=1,n;
	cin>>t;
	while(t--)
	{
		cin>>n;
		for(int i=0;i<n;i++)
			for(int q=0;q<n;q++)
				cin>>mat[i][q];
		double wp[123]={0},owp[123]={0},oowp[123]={0};
		for(int i=0;i<n;i++)
		{
			double a=0,b=0;
			for(int q=0;q<n;q++)
			{
				if(mat[i][q]=='.')continue;
				b++;
				a+=mat[i][q]-'0';
			}

			wp[i]=a/b;
		}
		for(int i=0;i<n;i++)
		{
			double a=0,b=0;
			for(int q=0;q<n;q++)
			{
				if(mat[i][q]-'.'==0)continue;
				b++;
				double aa=0,bb=0;
				for(int z=0;z<n;z++)
				{
					if(i==z)continue;
					if(mat[q][z]-'.')
					{
						bb++;
						aa+=mat[q][z]-'0';
					}
				}
				a+=aa/bb;
			//	cout<<i<<"  "<<q<<"   "<<aa/bb<<endl; 
			}
			owp[i]=a/b;
		}
		for(int i=0;i<n;i++)
		{
			double a=0,b=0;
			for(int q=0;q<n;q++)
			{
				if(mat[i][q]-'.')
				{
					b++;
					a+=owp[q];
				}
			}
			oowp[i]=a/b;
		}
	//	for(int i=0;i<n;i++)
	//		cout<<owp[i]<<endl;
		printf("Case #%d:\n",cas++);
		for(int i=0;i<n;i++)
			printf("%.12lf\n",wp[i]*0.25+owp[i]*0.5+oowp[i]/4);
	}
}