#include<iostream>
using namespace std;

int a[1005],b[1005];

int main()
{
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	int t;
	int cas=1;
	cin>>t;
	while(t--)
	{
		int n;
		cin>>n;
		for(int i=0;i<n;i++)
			cin>>a[i]>>b[i];

		int res=0;
		for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)
		{
			if( (a[i]<a[j]&&b[i]>b[j]) || (a[i]>a[j]&&b[i]<b[j]))
				res++;
		}
		cout<<"Case #"<<cas++<<": "<<res<<'\n';
	}
	return 0;
}