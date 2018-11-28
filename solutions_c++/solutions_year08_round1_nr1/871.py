#include<iostream>
#include<algorithm>
using namespace std;
int v1[801],v2[801];
int main()
{
	int t,n,i,res,flag=1;
	cin>>t;
	while(t--)
	{
		cin>>n;
		for(i=0;i<n;i++)cin>>v1[i];
		for(i=0;i<n;i++)cin>>v2[i];
		sort(v1,v1+n);sort(v2,v2+n);
		res=0;
		for(i=0;i<n;i++)res+=v1[i]*v2[n-i-1];
		cout<<"Case #"<<flag++<<": ";
		cout<<res<<endl;
	}
	return 0;
}