#include<iostream>
#include<cmath>
#include<algorithm>
#include<string>
using namespace std;

typedef long long LL;

int main()
{
	int T,cs;
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&T);
	for(cs=1;cs<=T;cs++)
	{
		printf("Case #%d: ",cs);
		
		int n,i,t,ans;
		scanf("%d",&n);
		ans=0;
		for(i=0;i<n;i++)
		{
			scanf("%d",&t);
			if(t==i+1)
				continue;
			ans++;
		}
		printf("%lf\n",double(ans));
	}
	/*
	LL d[105]={1,1,2};
	LL f[105]={1,0,1};
	int i,j;
	for(i=3;i<20;i++)
	{
		d[i]=d[i-1]*i;
		f[i]=(i-1)*(f[i-2]+f[i-1]);
	}
	double ans[105]={0,0,2};
	for(i=3;i<20;i++)
	{
		ans[i]=double(f[i])/d[i];
		for(j=0;j<i;j++)
			ans[i]+=double(f[j])*(ans[j]+1)/d[j]/d[i-j];
		ans[i]/=1.0-double(f[i])/d[i];
	}
	*/
}