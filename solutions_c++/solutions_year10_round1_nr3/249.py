#include<stdio.h>
#include<iostream>
#include<algorithm>
#define ll long long
using namespace std;
int a[1000100];
ll ft(int a1,int a2,int b1,int b2)
{
	ll ans=0;
	for(int i=a1;i<=a2;i++)
		{
			int k=a[i];
			if(k<b1)
			{
				continue;
			}
			else if(k<=b2&&k>=b1)
			{
				ans+=k-b1+1;
			}
			else ans+=b2-b1+1;
		}
	return ans;
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int i;
	memset(a,0,sizeof(a));
	for(i=1;i<1000010;i++)
	{
		for(int j=a[i-1];j<=1000010;j++)
		{
			int flag=0;
			for(int k=1;j<=i/k;k++)
			{
				if(i-k*j>a[j])
				{
					flag=1;
					break;
				}
			}
			if(flag)
				a[i]=j;
			else
				break;
		}
	}
	int T;
	scanf("%d",&T);
	int ca=0;
	while(T--)
	{
            printf("Case #%d: ",++ca);
		int a1,a2,b1,b2;
		scanf("%d%d%d%d",&a1,&a2,&b1,&b2);
		ll ans=0;
		ans+=ft(a1,a2,b1,b2);
		ans+=ft(b1,b2,a1,a2);

		printf("%lld\n",ans);
	}
}