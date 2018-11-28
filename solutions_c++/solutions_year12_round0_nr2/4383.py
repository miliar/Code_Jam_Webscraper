#include <iostream>
using namespace std;
int n,s,t,p,k;

int solve()
{
	int ans=0;
	cin>>n>>s>>p;
	for(int i=0;i<n && s >= 0;++i)
	{
		cin>>k;
		if(max(p-1,0) + max(p-1,0) + p <= k)
		{
			++ans;
		}
		else if(max(p - 2,0) + max(p - 2,0) + p <= k && s > 0)
		{
			--s;
			ans++;
		}
	} 
	return ans;
}

int main()
{
	cin>>t;
	for(int i=1;i<=t;++i)
	{
		cout<<"Case #"<<i<<": "<<solve()<<endl;
	}
	return 0;
}