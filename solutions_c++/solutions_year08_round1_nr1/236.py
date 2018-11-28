#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string>
using namespace std;

int n,a[1000],b[1000];
long long ans;

int main()
{
	int T,kase=0;
	cin>>T;
	while (T--)
	{
		cin>>n;
		for (int i=0;i<n;i++)
			scanf("%d",&a[i]);
		for (int i=0;i<n;i++)
			scanf("%d",&b[i]);
		sort(a,a+n);
		sort(b,b+n);
		ans=0;
		for (int i=0;i<n;i++)
			ans+=(long long)a[i]*b[n-1-i];
		cout<<"Case #"<<++kase<<": "<<ans<<endl;
	}
	return 0;
}
