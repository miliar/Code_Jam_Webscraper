// Jam_B_R1.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include <iostream>
using namespace std;

int main()
{
	freopen("large.in", "r", stdin);
	freopen("large.out", "w", stdout);

	long long tx;
	cin>>tx;
	for(long long tt=1; tt<=tx; tt++)
	{
		long long n, k, t;
		double b;
		cin>>n>>k>>b>>t;
		long long res=0, all=0;
		long long x[55];
		for(int i=0; i<n; i++) cin>>x[i];
		long long speeds[55];
		for(int i=0; i<n; i++) cin>>speeds[i];
		long long fl=1;
		cout<<"Case #"<<tt<<": ";
		while(res<k)
		{
			if((b-x[n-1])<=t*speeds[n-1])
			{
				res++;
				n--;
			}
			else
			{
				int i;
				for(i=n-2; i>=0; i--)
				{
					if((b-x[i])<=t*speeds[i])
					{
						all+=n-i-1;
						for(int j=i; j<n; j++) { speeds[j]=speeds[j+1]; x[j]=x[j+1]; }
						n--;
						res++;
						break;
					}
				}
				if(i==-1)
				{
					fl=-1;
					cout<<"IMPOSSIBLE"<<endl;
					break;
				}
			}
		}
		if(fl!=-1)
			cout<<all<<endl;

	}
 	

	return 0;
}

