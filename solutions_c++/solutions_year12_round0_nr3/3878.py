#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<iostream>
#include<queue>
using namespace std;
long long s[2000005];
int Min(int a,int b)
{
	return a<b?a:b;
}
int f(int i)
{
	int j=1,ret,k,t;
	ret=i;
	while(i/j>=10)
		j*=10;
	for(k=0;k<7;++k)
	{
		t=i%10;
		i=i/10;
		i+=t*j;
		if(t!=0)
			ret=Min(ret,i);
	}
	return ret;
}
int main()
{
	int t,cas=0;
	int a,b,i,j,k;
	long long ans;
	freopen("C-large.in","r",stdin);
	freopen("3.out","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		cas++;
		scanf("%d%d",&a,&b);
		memset(s,0,sizeof(s));
		for(i=a;i<=b;++i)
		{
			k=f(i);
			s[k]++;
		}
		ans=0;
		for(i=0;i<=b;++i)
		{
			ans+=(s[i]*(s[i]-1))/2;
		}
		printf("Case #%d: %lld\n",cas,ans);
	}
}