#include<iostream>
#include<stdio.h>
#include<vector>
#include<algorithm>
#include<math.h>

using namespace std;

int main()
{
	int t,m=0;
	cin>>t;
	while(t--)
	{
		int p,q,i,j,k,mincoins=10000000,rel,coins;
		cin>>p>>q;
		int a[q],b[p+1];
		for(i=0;i<q;i++)
			cin>>a[i];
		m++;	
		
		do
		{
			for(i=1;i<=p;i++)
				b[i]=1;
			j=0;
			coins=0;		
			while(j<q)
			{
				rel=a[j];
				j++;
				for(k=rel-1;k>=1;k--)
				{
					if(b[k]==1)
						coins++;
					else
						break;
				
				}
				for(k=rel+1;k<=p;k++)
				{
					if(b[k]==1)
						coins++;
					else
						break;
				
				}
				b[rel]=0;
				
			
			
			}
			if(coins<mincoins)
			{
					mincoins=coins;
					
			}
			
		}while(next_permutation(a,a+q));
		
		
		cout<<"Case #"<<m<<": "<<mincoins<<endl;
		
	}
}
