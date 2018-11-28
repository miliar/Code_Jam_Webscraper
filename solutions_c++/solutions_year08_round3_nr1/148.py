#include<iostream>
#include<vector>
using namespace std;
bool myfunc(int a,int b)
{
	if(a>b)	
	return true;
	return false;
}
main()
{
	int t,c=1;
	cin>>t;
	while(t--)
	{
		int i,max,keys,let;
		cin>>max>>keys>>let;
		vector<int> freq;
		for(i=0;i<let;i++)
		{freq.push_back(i);cin>>freq[i];}
		sort(freq.begin(),freq.end(),myfunc);
		long long int now=1,ans=0;
		for(i=0;i<freq.size();i++)
		{
		ans=ans+now*freq[i];
		if((i+1)%keys==0)
		now++;
		}
		cout<<"Case #"<<c<<": "<<ans<<endl;
		c++;
		freq.clear();
	}
}
		

