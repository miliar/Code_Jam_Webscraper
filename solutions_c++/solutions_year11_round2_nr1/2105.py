#include<iostream>
using namespace std;

#include<stdio.h>

int main()
{
	int t,n,i,j,k,l,c;
	double wp[100],owp[100],oowp[100],w,p,rpi[100];
	char a[100][100];
	cin>>t;
	for(i=1;i<=t;i++)
	{
		cin>>n;
		for(j=0;j<n;j++)
		{
			p=n;
			w=0;
			for(k=0;k<n;k++)
			{
				cin>>a[j][k];
				if(a[j][k]=='.')
					p--;
				else if(a[j][k]=='1')
					w++;
			}
			wp[j]=(w/p);
		}
		for(j=0;j<n;j++)
		{
			owp[j]=0;
			c=0;
			for(k=0;k<n;k++)
			{
				 p=n;
				 w=0;
				if(a[j][k]!='.')
				{
					for(l=0;l<n;l++)
					{
						if(l!=j)
						{
							if(a[k][l]=='.')
								p--;
							else if(a[k][l]=='1')
								w++;
						}
						else
							p--;
					}
					owp[j]=owp[j]+(w/p);
					c++;				
				}		
			}
			owp[j]=(owp[j])/c;
		}
		for(j=0;j<n;j++)
		{
			oowp[j]=0;
			p=n;
			for(k=0;k<n;k++)
			{
				if(a[j][k]!='.')
					oowp[j]+=owp[k];
				else
					p--;
			}
			oowp[j]=((oowp[j])/p);
			rpi[j]=(wp[j]*0.25)+(owp[j]*0.5)+(oowp[j]*0.25);
		}
		printf("Case #%d:\n",i);
		for(j=0;j<n;j++)
		{
			cout<<rpi[j]<<"\n";
			cout.precision(12);
		}
	}
	return 0;
}
