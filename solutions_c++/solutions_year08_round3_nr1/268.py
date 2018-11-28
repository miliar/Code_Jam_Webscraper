#include<iostream>
#include<vector>
#include<string>
#include<algorithm>

using namespace std;

int main()
{
	long long int n;
	cin>>n;
	
	for(int i=1;i<=n;i++)
	{
		long long int p,k,l,mkp=0,j,m,letter,f;
		cin>>p>>k>>l;
		
		vector<long long int> freq;				
		freq.clear();
		for(j=1;j<=l;j++)
		{
			cin>>f;
			freq.push_back(f);
		}
		if(p*k<l)
		{
			cout<<"Case #"<<i<<": Impossible"<<endl;
			continue;
		}	
		
		sort(freq.begin(),freq.end(),greater<long long int>());
		letter=0;
		for(j=1;j<=p && letter<l;j++)
		{
			for(m=1;m<=k && letter<l;m++)
			{	
				mkp+=freq[letter]*j;
				letter++;
			}	
		}
		cout<<"Case #"<<i<<": "<<mkp<<endl;
	}
}
