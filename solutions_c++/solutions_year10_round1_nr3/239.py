#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<string>
using namespace std;
const double tau=(1+sqrt(5))/2;
int a[1000001],f[1000001];
int i,n,t,casenum,T,A1,A2,B1,B2;
long long ans;
int solve(int x,int l,int r)
{
	if (x<l) return 0;
	if (x<=r) return (x-l+1);
	return (r-l+1);
}
int main()
{
	freopen("problem.in","r",stdin);
	freopen("problem.out","w",stdout);
	for (i=0;i<=1000000;i++)
		a[i]=floor(i*tau)+i+1;
	f[1]=f[2]=0;
	t=1;
	for (i=3;i<=1000000;i++)
	{
		if (i==a[t])
		{
			f[i]=f[i-1]+1;
			t++;
		}
		else f[i]=f[i-1];
	}
	cin>>T;
	for (casenum=1;casenum<=T;casenum++)
	{
		cout<<"Case #"<<casenum<<": ";
		cin>>A1>>A2>>B1>>B2;
		ans=0;
		for (i=B1;i<=B2;i++)
			ans+=solve(i-f[i]-1,A1,A2);
		for (i=A1;i<=A2;i++)
			ans+=solve(i-f[i]-1,B1,B2);
		cout<<ans<<endl;
	}
	return 0;
}
