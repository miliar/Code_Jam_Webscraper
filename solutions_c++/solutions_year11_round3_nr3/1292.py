#include<iostream.h>
#include<stdio.h>
#include<string.h>
#include<cstring>
#include<cmath>
#include<math.h>

void main()

{	
	freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small.out","w",stdout);
	int n,l,h,no,r;
	int o[100];
	cin>>n;

	for(int i=0;i<n;i++)
	{	r=1;
		cin>>no>>l>>h;
		for(int j=0;j<no;j++)
			cin>>o[j];
		for(int k=l;k<=h;k++)
		{	r=1;
			for(int m=0;m<no;m++)
			{	
				if(k%o[m]==0||o[m]%k==0)
					r=r*1;
				else
					r=0;
			}
			if(r==1)
			{
				r=k;
				k=h+1;
			}
			else
				r=0;
		}
		cout<<"Case #"<<i+1<<": ";
			if(r==0)
				cout<<"NO"<<endl;
			else
				cout<<r<<endl;


	}


}