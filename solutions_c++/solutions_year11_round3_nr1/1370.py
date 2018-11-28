#include<iostream.h>
#include<stdio.h>
#include<string.h>
#include<cstring>
#include<cmath>
#include<math.h>

void main()

{	
	int n,f=1;
	int r,c,count=0;
	char a[100][100];
	freopen("A-large.in","r",stdin);
    freopen("A-lop.out","w",stdout);
	cin>>n;
	for(int i=0;i<n;i++)
	{	count=0;
		f=1;
		cin>>r>>c;
		for(int j=0;j<r;j++)
		{
			cin>>a[j];
		}
		for(int k=0;k<r;k++)
		{
			for(int l=0;l<c;l++)
			{
				if(a[k][l]=='#')
					count++;
			}
		}
		if(count%4!=0)
			f=0;
		if(f==0)
			goto here;
		for(k=0;k<r;k++)
		{
			for(int l=0;l<c;l++)
			{
				if(a[k][l]=='#')
				{
					a[k][l]='/';
					if(a[k][l+1]=='#')
					{l++;
						a[k][l]='\\';	
						if(a[k+1][l-1]=='#')
						{
							a[k+1][l-1]='\\';
								if(a[k+1][l]=='#')
									a[k+1][l]='/';
								else
									f=0;
						}
						else
						{
							f=0;
							
						}
					}
					else
					{
						f=0;
					
					}
				}
			}
		}
	here:
		cout<<"Case #"<<i+1<<":"<<endl;
		if(f==0)
		{
			cout<<"Impossible";
		}
		else
		{
			for(int q=0;q<r;q++)
			{
				for(int w=0;w<c;w++)
				{
					cout<<a[q][w];
				}
				cout<<endl;
			}
		}
		cout<<endl;
			

	}
}