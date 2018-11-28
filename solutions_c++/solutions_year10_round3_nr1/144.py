#include<iostream>
#include<cmath>
#include<cstdio>
#include<string.h>
using namespace std;


int main()
{
	freopen("c:\\2.in","r",stdin);
	freopen("c:\\out2.txt","w",stdout);


	int t;
	cin>>t;
	int i;
	for(i=1;i<=t;i++)
	{
		long long ans=0;
		int n;
		cin>>n;
		int a[1005],b[1005];
		int j;
		for(j=0;j<n;j++)
		{
			cin>>a[j]>>b[j];
			int t;
			for(t=j-1;t>=0;t--)
			{
				if((a[t]>a[j])&&(b[t]>b[j])||(a[t]<a[j])&&(b[t]<b[j]))
				{
				}
				else
					ans++;

			}
			
		}


		cout<<"Case #"<<i<<": "<<ans<<endl;
	}

return 0;
}
