#include<iostream.h>
#include<stdio.h>
#include<string.h>
#include<cstring>
#include<cmath>
#include<math.h>

void main()

{	
	int n,no,c,w,count=0;
	double wp[100],owp[100],oowp[100],t,res[100];
	char a[50][50];
	freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small.out","w",stdout);

	cin>>n;
	for(int i=0;i<n;i++)
	{	
		cin>>no;
		for(int j=0;j<no;j++)
		{
			cin>>a[j];
		}
	/*	for(int k=0;k<no;k++)
		{
			cout<<a[k][2]<<endl;
		}*/
		for(int k=0;k<no;k++)
		{	c=w=0;
			for(int l=0;l<no;l++)
			{
				if(a[k][l]!='.')
					c++;
				if(a[k][l]=='1')
					w++;
			}
			wp[k]=(double)w/c;//cout<<wp[k]<<endl;

		}
		for( k=0;k<no;k++)
		{	count=0;
		t=0;
			for(int l=0;l<no;l++)
			{
				if(a[k][l]!='.')
				{
					c=w=0;
					count++;
					for(int m=0;m<no;m++)
					{	
						if(k!=m)
						{
							if(a[l][m]!='.')
								c++;
							if(a[l][m]=='1')
								w++;
						}	
					}
					if(c!=0&&w!=0)
						t+=(double)w/c;
				}

			}
			owp[k]=(double)t/count;
			//cout<<owp[k]<<endl;
		}
		for(k=0;k<no;k++)
		{	t=0;count=0;
			for(int l=0;l<no;l++)
			{
				if(a[k][l]!='.')
				{
					count++;
					t+=owp[l];
				}
			}
			oowp[k]=(double)t/count;
		//	cout<<oowp[k]<<endl;
		}
		cout<<"Case #"<<i+1<<":"<<endl;
		for(k=0;k<no;k++)
		{
			res[k]=(double)(0.25*wp[k]+0.50 * owp[k] + 0.25 * oowp[k]);	
		
				cout<<res[k]<<endl;
		}
	}
}
