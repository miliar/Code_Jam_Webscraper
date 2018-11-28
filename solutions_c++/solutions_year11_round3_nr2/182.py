#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cstring>
#define inf 0x3f3f3f3f
using namespace std;
int s[1000005];
long long ans,tmp[1000005];
int res[1000005];
bool cmp(int a,int b)
{return a>b;}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("Cout.out","w",stdout);
	int t,cas;
	scanf("%d",&t);
	for(cas=1;cas<=t;cas++)
	{
		memset(s,0,sizeof(s));
		memset(tmp,0,sizeof(tmp));
		memset(res,0,sizeof(res));
		int m,n,k;
		long long ti;
		scanf("%d%lld%d%d",&m,&ti,&n,&k);
		int i,j;
		for(i=1;i<=k;i++)
			scanf("%d",&s[i]);
		s[0]=s[k];
		for(j=k+1;j<=n;j++)
			s[j]=s[j%k];
		for(i=1;i<=n;i++)
			tmp[i]=tmp[i-1]+2*s[i];
		if(m==0||ti>=tmp[n])
			printf("Case #%d: %lld\n",cas,tmp[n]);
		else
		{
			int p,j;
			for(i=1;i<=n;i++)
				if(tmp[i]>ti)
				{
					p=i;
					s[i]=s[i]-(ti-tmp[i-1])/2;
					break;
				}
			int num=0;
			for(i=p;i<=n;i++)
				res[num++]=s[i];
			sort(res,res+num,cmp);
			for(i=0;i<min(m,num);i++)
				tmp[n]-=res[i];
			printf("Case #%d: %lld\n",cas,tmp[n]);
		}
	}
	return 0;
}
