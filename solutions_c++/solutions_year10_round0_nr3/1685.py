// Jam_C.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include <iostream>
using namespace std;



int main()
{
	freopen("large.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	long long t;
	cin>>t;
	for(long long a=0; a<t; a++)
	{
		long long r,k,n;
		cin>>r>>k>>n;
		long long mas[1005];
		long long i=0;
		for(i=0; i<n; i++)
		{
			cin>>mas[i];
		}
		long long d[1005], dd[1005];
		long long j=0, tsum=0;
		for(i=0; i<n; i++)
		{
			if(tsum+mas[i]>k) break;
			tsum+=mas[i];
		}
		j=i;
		dd[0]=j;
		for(i=0; i<=n-1; i++)
		{
			d[i]=tsum;
			if(i==n-1) break;
			tsum-=mas[i];
			long long u=0;
			while(tsum+mas[j%n]<=k && ((j%n)!=i+1)||(j==i+1))
			{
				u++;
				tsum+=mas[j%n];
				j++;
			}
			dd[i+1]=dd[i]-1+u;

		}
		long long t1=0, res=0;
		for(i=0; i<r; i++)
		{
			res+=d[t1];
			t1=(t1+dd[t1])%n;
		}	
		cout<<"Case #"<<a+1<<": "<<res<<endl;
	}

}

