#include <iostream>
#include <algorithm>
#include <stdio.h>

using namespace std;

int main()
{
	int n;
	
	cin>>n;
	
	for(int i=0;i<n;i++)
	{
		long p,k,l;
		long long count=0;
		
		cin>>p>>k>>l;
		
		long *freq = new long[l];
		for(long j=0;j<l;j++)
			cin>>freq[j];
		
		sort(freq,freq+l);
		
		int fact=1;
		int linv=0;
		for(long j=l-1;j>=0;j--)
		{
			count += (freq[j]*fact);
			linv++;
			if(linv>=k)
			{
				linv=0;
				fact++;
				//cout<<" j = "<<j<<" k = "<<k<<" freq = "<<freq[j]<<endl;
			} 
		}
		cout<<"Case #"<<i+1<<": "<<count<<endl;
	}
}
			
		
