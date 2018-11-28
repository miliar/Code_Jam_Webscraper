#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;


int num[1000005];
int C[1005];
int cmp(int a,int b)
{
	return a>b;
}

int main()
{
	int cas=1;
	freopen("B-large.in","r",stdin);
	freopen("outBL.txt","w",stdout);
	int T;scanf("%d",&T);
	while(T--)
	{
		int i,j;
		long long l,t,n,c;
		long long ans=0;
		scanf("%lld%lld%lld%lld",&l,&t,&n,&c);
		for(i=0;i<c;++i)
			scanf("%d",&C[i]);
		int pt=0;
		t/=2;
		for(i=0;i<n;++i)
		{
			int kl=C[i%c];
			if(t-kl<0)
			{
				ans+=t*2;
				num[pt++]=kl-t;
				break;
			}
			ans+=kl*2;
			t-=kl;
		}
		for(i=i+1;i<n;++i)
		{
			num[pt++]=C[i%c];
		}
		sort(num,num+pt,cmp);
		for(i=0;i<l&&i<pt;++i)
			ans+=num[i];
		for(i=l;i<pt;++i)
			ans+=2*num[i];
		printf("Case #%d: %lld\n",cas++,ans);
	}
}